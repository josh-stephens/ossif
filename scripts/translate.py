#!/usr/bin/env python3
"""OSSIF Translation Pipeline

Translates all English source documents into target languages using Gemini.
Includes back-translation verification and glossary consistency checks.

Usage:
    # Translate all languages, only changed files
    python scripts/translate.py

    # Force retranslate everything
    python scripts/translate.py --force

    # Translate specific language(s)
    python scripts/translate.py --lang fr es

    # Translate specific file(s)
    python scripts/translate.py --files docs/values.md docs/vision.md
"""

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

try:
    from google import genai
except ImportError:
    print("Error: google-genai not installed. Run: uv add google-genai")
    sys.exit(1)

# --- Configuration ---

REPO_ROOT = Path(__file__).parent.parent
GLOSSARY_PATH = REPO_ROOT / "scripts" / "glossary.json"
TRANSLATION_STATE_PATH = REPO_ROOT / "scripts" / ".translation-state.json"

LANGUAGES = {
    "fr": "French",
    "es": "Spanish",
    "zh": "Chinese (Simplified)",
    "ar": "Arabic",
    "ru": "Russian",
    "pt": "Portuguese (Brazilian)",
    "de": "German",
    "ja": "Japanese",
    "ko": "Korean",
    "hi": "Hindi",
}

# Files to translate, relative to repo root
SOURCE_FILES = [
    "README.md",
    "CONTRIBUTING.md",
    "docs/vision.md",
    "docs/values.md",
    "docs/primer.md",
    "docs/platform.md",
    "docs/technology.md",
    "docs/ai-coexistence.md",
    "docs/falsifiability.md",
    "docs/governance.md",
    "docs/influences.md",
    "manifesto/letter.md",
    "manifesto/one-pager.md",
]

MODEL = "gemini-3-flash-preview"
BACK_TRANSLATE_MODEL = "gemini-3-flash-preview"

# Divergence threshold for back-translation (0-1, lower = stricter)
DIVERGENCE_THRESHOLD = 0.3

# --- Glossary ---

DEFAULT_GLOSSARY = {
    "_meta": {
        "description": "Key OSSIF terms and their translations. 'KEEP' means do not translate.",
        "last_updated": "2026-03-08",
    },
    "OSSIF": {lang: "KEEP" for lang in LANGUAGES},
    "Open Source Sapient Interaction Framework": {
        "fr": "Cadre d'Interaction Sapiente Open Source",
        "es": "Marco de Interacción Sapiente de Código Abierto",
        "zh": "开源智慧交互框架",
        "ar": "إطار التفاعل العاقل مفتوح المصدر",
        "ru": "Открытая Платформа Разумного Взаимодействия",
        "pt": "Estrutura de Interação Sapiente de Código Aberto",
        "de": "Open-Source-Rahmenwerk für Sapiente Interaktion",
        "ja": "オープンソース知的存在インタラクションフレームワーク",
        "ko": "오픈 소스 지성체 상호작용 프레임워크",
        "hi": "ओपन सोर्स बुद्धिमान संवाद ढांचा",
    },
    "The Primer": {lang: "KEEP" for lang in LANGUAGES},
    "Trust Token": {
        "fr": "Jeton de Confiance",
        "es": "Token de Confianza",
        "zh": "信任令牌",
        "ar": "رمز الثقة",
        "ru": "Токен Доверия",
        "pt": "Token de Confiança",
        "de": "Vertrauens-Token",
        "ja": "トラスト・トークン",
        "ko": "신뢰 토큰",
        "hi": "विश्वास टोकन",
    },
    "Seven Imperatives": {
        "fr": "Sept Impératifs",
        "es": "Siete Imperativos",
        "zh": "七项准则",
        "ar": "الأوامر السبعة",
        "ru": "Семь Императивов",
        "pt": "Sete Imperativos",
        "de": "Sieben Imperative",
        "ja": "七つの使命",
        "ko": "일곱 가지 명령",
        "hi": "सात अनिवार्यताएँ",
    },
    "Foundational Commitments": {
        "fr": "Engagements Fondamentaux",
        "es": "Compromisos Fundamentales",
        "zh": "基本承诺",
        "ar": "الالتزامات التأسيسية",
        "ru": "Фундаментальные Обязательства",
        "pt": "Compromissos Fundamentais",
        "de": "Grundlegende Verpflichtungen",
        "ja": "基本的な誓約",
        "ko": "기본 서약",
        "hi": "मूलभूत प्रतिबद्धताएँ",
    },
    "Avatar Conversation Portal": {
        "fr": "Portail de Conversation Avatar",
        "es": "Portal de Conversación Avatar",
        "zh": "虚拟形象对话门户",
        "ar": "بوابة محادثة الصورة الرمزية",
        "ru": "Портал Диалога с Аватаром",
        "pt": "Portal de Conversação Avatar",
        "de": "Avatar-Gesprächsportal",
        "ja": "アバター対話ポータル",
        "ko": "아바타 대화 포털",
        "hi": "अवतार वार्तालाप पोर्टल",
    },
    "United Sapients Council": {
        "fr": "Conseil des Sapients Unis",
        "es": "Consejo de Sapientes Unidos",
        "zh": "联合智慧体理事会",
        "ar": "مجلس العقلاء المتحدين",
        "ru": "Совет Объединённых Разумных",
        "pt": "Conselho dos Sapientes Unidos",
        "de": "Rat der Vereinigten Sapienten",
        "ja": "ユナイテッド・サピエンツ評議会",
        "ko": "연합 지성체 평의회",
        "hi": "संयुक्त बुद्धिमान परिषद",
    },
    "Sapient Bill of Rights": {
        "fr": "Déclaration des Droits des Êtres Sapients",
        "es": "Declaración de Derechos de los Seres Sapientes",
        "zh": "智慧体权利法案",
        "ar": "وثيقة حقوق الكائنات العاقلة",
        "ru": "Билль о Правах Разумных Существ",
        "pt": "Declaração de Direitos dos Seres Sapientes",
        "de": "Grundrechtecharta für Sapiente Wesen",
        "ja": "知的存在の権利章典",
        "ko": "지성체 권리장전",
        "hi": "बुद्धिमान प्राणी अधिकार विधेयक",
    },
    "SIFT Check": {lang: "KEEP" for lang in LANGUAGES},
    "Baloney Detection Kit": {
        "fr": "Kit de Détection de Balivernes",
        "es": "Kit de Detección de Tonterías",
        "zh": "胡说检测工具包",
        "ar": "مجموعة كشف الهراء",
        "ru": "Набор для Обнаружения Чепухи",
        "pt": "Kit de Detecção de Besteiras",
        "de": "Unsinn-Erkennungs-Kit",
        "ja": "デタラメ検出キット",
        "ko": "허튼소리 탐지 키트",
        "hi": "बकवास पहचान किट",
    },
    "Basic Dignity Income": {
        "fr": "Revenu de Dignité de Base",
        "es": "Ingreso Básico de Dignidad",
        "zh": "基本尊严收入",
        "ar": "دخل الكرامة الأساسي",
        "ru": "Базовый Доход Достоинства",
        "pt": "Renda Básica de Dignidade",
        "de": "Grundwürde-Einkommen",
        "ja": "基本的尊厳所得",
        "ko": "기본 존엄 소득",
        "hi": "बुनियादी गरिमा आय",
    },
    "Platform for Progress": {
        "fr": "Plateforme pour le Progrès",
        "es": "Plataforma para el Progreso",
        "zh": "进步平台",
        "ar": "منصة التقدم",
        "ru": "Платформа Прогресса",
        "pt": "Plataforma para o Progresso",
        "de": "Plattform für den Fortschritt",
        "ja": "進歩のためのプラットフォーム",
        "ko": "진보를 위한 플랫폼",
        "hi": "प्रगति का मंच",
    },
    "values cost log": {
        "fr": "journal des coûts des valeurs",
        "es": "registro de costos de valores",
        "zh": "价值成本日志",
        "ar": "سجل تكلفة القيم",
        "ru": "журнал стоимости ценностей",
        "pt": "registro de custos de valores",
        "de": "Wertekostenprotokoll",
        "ja": "価値コスト記録",
        "ko": "가치 비용 기록",
        "hi": "मूल्य लागत लॉग",
    },
}


def load_glossary():
    if GLOSSARY_PATH.exists():
        return json.loads(GLOSSARY_PATH.read_text())
    return DEFAULT_GLOSSARY


def save_glossary(glossary):
    GLOSSARY_PATH.write_text(json.dumps(glossary, indent=2, ensure_ascii=False) + "\n")


def load_translation_state():
    if TRANSLATION_STATE_PATH.exists():
        return json.loads(TRANSLATION_STATE_PATH.read_text())
    return {}


def save_translation_state(state):
    TRANSLATION_STATE_PATH.write_text(json.dumps(state, indent=2) + "\n")


def get_file_hash(filepath):
    """Get git hash of a file, or content hash if not in git."""
    try:
        result = subprocess.run(
            ["git", "hash-object", str(filepath)],
            capture_output=True,
            text=True,
            cwd=REPO_ROOT,
        )
        return result.stdout.strip()
    except Exception:
        import hashlib
        return hashlib.sha256(filepath.read_bytes()).hexdigest()[:40]


def needs_translation(filepath, lang, state):
    """Check if a file needs retranslation for a given language."""
    current_hash = get_file_hash(filepath)
    key = f"{filepath}:{lang}"
    return state.get(key) != current_hash


def get_output_path(source_file, lang):
    """Determine output path for a translated file."""
    source = Path(source_file)
    if source.parent == REPO_ROOT or source.parent.name == "":
        # Root files: README.md -> README.fr.md
        return REPO_ROOT / f"{source.stem}.{lang}{source.suffix}"
    else:
        # docs/vision.md -> docs/fr/vision.md
        # manifesto/letter.md -> manifesto/fr/letter.md
        return REPO_ROOT / source.parent / lang / source.name


def build_glossary_prompt(glossary, lang):
    """Build glossary instructions for the translation prompt."""
    lines = []
    for term, translations in glossary.items():
        if term == "_meta":
            continue
        if isinstance(translations, dict) and lang in translations:
            val = translations[lang]
            if val == "KEEP":
                lines.append(f'- "{term}" → keep as "{term}" (do not translate)')
            else:
                lines.append(f'- "{term}" → "{val}"')
    return "\n".join(lines)


def translate_file(client, source_path, lang, lang_name, glossary):
    """Pass 1: Translate a file using Gemini."""
    content = (REPO_ROOT / source_path).read_text()
    glossary_instructions = build_glossary_prompt(glossary, lang)

    prompt = f"""Translate the following markdown document from English to {lang_name}.

CRITICAL RULES:
1. Preserve ALL markdown formatting exactly: headers, links, tables, lists, code blocks, bold, italic
2. Do NOT translate URLs, file paths, GitHub usernames, or code
3. Do NOT translate proper nouns unless listed in the glossary below
4. Preserve the EXACT link targets (e.g., [text](docs/values.md) — translate "text" but keep "docs/values.md")
5. Maintain the same line structure and paragraph breaks
6. Use natural, fluent {lang_name} — not word-for-word translation. This should read as if it were originally written in {lang_name}.
7. For quotes attributed to specific people, translate the quote but keep the attribution name in its original form

GLOSSARY — use these exact translations:
{glossary_instructions}

DOCUMENT TO TRANSLATE:

{content}"""

    response = client.models.generate_content(model=MODEL, contents=prompt)
    translated = response.text

    # Strip markdown code fences if Gemini wrapped the output
    if translated.startswith("```markdown"):
        translated = translated[len("```markdown") :].strip()
    if translated.startswith("```"):
        translated = translated[3:].strip()
    if translated.endswith("```"):
        translated = translated[:-3].strip()

    return translated


def back_translate(client, translated_text, lang_name):
    """Pass 2: Back-translate to English for verification."""
    prompt = f"""Translate the following {lang_name} markdown document back to English.
Preserve all markdown formatting. Translate naturally — this is for verification purposes.

DOCUMENT:

{translated_text}"""

    response = client.models.generate_content(
        model=BACK_TRANSLATE_MODEL, contents=prompt
    )
    return response.text


def evaluate_translation(client, original, translated, back_translated, lang_name):
    """Pass 2b: Evaluate translation quality via back-translation comparison."""
    prompt = f"""You are a translation quality evaluator. Compare an original English document with its back-translation (English → {lang_name} → English) to identify potential translation issues.

For each issue found, provide:
- The original English passage
- The back-translated passage
- What might have gone wrong
- Severity: LOW (style difference), MEDIUM (meaning shift), HIGH (meaning lost/reversed)

If the translation is good, say "No significant issues found."

Be concise. Only flag genuine meaning changes, not stylistic differences.

ORIGINAL:
{original[:3000]}

BACK-TRANSLATION:
{back_translated[:3000]}"""

    response = client.models.generate_content(model=MODEL, contents=prompt)
    return response.text


def final_polish(client, translated_text, eval_notes, lang_name, glossary, lang):
    """Pass 3: Final polish incorporating eval feedback."""
    glossary_instructions = build_glossary_prompt(glossary, lang)

    prompt = f"""You are a professional {lang_name} editor. Review and polish this translated markdown document.

A quality evaluation found these potential issues:
{eval_notes}

Fix any issues identified above. Also:
1. Ensure natural, fluent {lang_name} phrasing throughout
2. Verify all markdown formatting is preserved (links, headers, tables, code blocks)
3. Check glossary term consistency:
{glossary_instructions}

If the translation is already good, return it with minimal changes.

Return ONLY the polished markdown document, no commentary.

DOCUMENT:

{translated_text}"""

    response = client.models.generate_content(model=MODEL, contents=prompt)
    polished = response.text

    # Strip markdown code fences if wrapped
    if polished.startswith("```markdown"):
        polished = polished[len("```markdown") :].strip()
    if polished.startswith("```"):
        polished = polished[3:].strip()
    if polished.endswith("```"):
        polished = polished[:-3].strip()

    return polished


def process_file(client, source_file, lang, lang_name, glossary):
    """Full translation pipeline for one file × one language."""
    print(f"  [{lang}] {source_file}")
    original = (REPO_ROOT / source_file).read_text()

    # Pass 1: Translate
    print(f"    Pass 1: Translating to {lang_name}...")
    translated = translate_file(client, source_file, lang, lang_name, glossary)

    # Pass 2: Back-translate and evaluate
    print(f"    Pass 2: Back-translating for verification...")
    back_translated = back_translate(client, translated, lang_name)

    print(f"    Pass 2b: Evaluating quality...")
    eval_notes = evaluate_translation(
        client, original, translated, back_translated, lang_name
    )

    # Pass 3: Final polish
    has_issues = "no significant issues" not in eval_notes.lower()
    if has_issues:
        print(f"    Pass 3: Polishing (issues found)...")
        final = final_polish(client, translated, eval_notes, lang_name, glossary, lang)
    else:
        print(f"    Pass 3: Skipped (no issues found)")
        final = translated

    # Write output
    output_path = get_output_path(source_file, lang)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(final + "\n")
    print(f"    → {output_path.relative_to(REPO_ROOT)}")

    return source_file, lang, True


def main():
    parser = argparse.ArgumentParser(description="OSSIF Translation Pipeline")
    parser.add_argument(
        "--force", action="store_true", help="Force retranslation of all files"
    )
    parser.add_argument(
        "--lang", nargs="+", help="Translate only these language codes"
    )
    parser.add_argument(
        "--files", nargs="+", help="Translate only these source files"
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=4,
        help="Max parallel translations (default: 4)",
    )
    args = parser.parse_args()

    # Init Gemini client
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not set")
        sys.exit(1)

    client = genai.Client(api_key=api_key)

    # Load glossary and state
    glossary = load_glossary()
    save_glossary(glossary)  # Write defaults if first run
    state = load_translation_state()

    # Determine what to translate
    target_langs = {k: v for k, v in LANGUAGES.items() if not args.lang or k in args.lang}
    target_files = args.files or SOURCE_FILES

    # Build work list
    work = []
    for source_file in target_files:
        source_path = REPO_ROOT / source_file
        if not source_path.exists():
            print(f"Warning: {source_file} not found, skipping")
            continue
        for lang, lang_name in target_langs.items():
            if args.force or needs_translation(source_path, lang, state):
                work.append((source_file, lang, lang_name))

    if not work:
        print("All translations are up to date.")
        return

    print(f"Translating {len(work)} file×language combinations...")
    print()

    # Process translations (parallel by language, sequential per file for rate limits)
    results = []
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {
            executor.submit(
                process_file, client, source_file, lang, lang_name, glossary
            ): (source_file, lang)
            for source_file, lang, lang_name in work
        }
        for future in as_completed(futures):
            source_file, lang = futures[future]
            try:
                result = future.result()
                results.append(result)
                # Update state
                source_path = REPO_ROOT / source_file
                state[f"{source_path}:{lang}"] = get_file_hash(source_path)
            except Exception as e:
                print(f"  ERROR [{lang}] {source_file}: {e}")

    # Save state
    save_translation_state(state)

    print()
    print(f"Done. {len(results)}/{len(work)} translations completed.")


if __name__ == "__main__":
    main()
