#!/usr/bin/env python3
"""Generate an HTML report of OSSIF translation token usage and costs.

Usage:
    python scripts/translation-report.py          # All runs
    python scripts/translation-report.py --last 5  # Last 5 runs
    python scripts/translation-report.py --open     # Open in browser
"""

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
LOGS_DIR = REPO_ROOT / "scripts" / "logs"

# Gemini 3 Flash pricing (per 1M tokens) — update when pricing changes
PRICING = {
    "gemini-3.7-flash": {"prompt": 0.75, "completion": 3.75},
    "gemini-3-flash-preview": {"prompt": 0.10, "completion": 0.40},
    "default": {"prompt": 0.10, "completion": 0.40},
}


def load_logs(limit=None):
    if not LOGS_DIR.exists():
        return []
    files = sorted(LOGS_DIR.glob("translate-*.json"), reverse=True)
    if limit:
        files = files[:limit]
    logs = []
    for f in reversed(files):  # chronological order
        try:
            logs.append(json.loads(f.read_text()))
        except (json.JSONDecodeError, OSError):
            continue
    return logs


def calc_cost(tokens, model="gemini-3-flash-preview"):
    p = PRICING.get(model, PRICING["default"])
    prompt_cost = (tokens.get("prompt_tokens", 0) / 1_000_000) * p["prompt"]
    completion_cost = (tokens.get("completion_tokens", 0) / 1_000_000) * p["completion"]
    return prompt_cost + completion_cost


def generate_html(logs):
    # Aggregate data
    runs = []
    all_time = {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0, "api_calls": 0, "cost": 0}
    by_lang = {}
    by_pass = {}
    by_file = {}

    for log in logs:
        t = log.get("totals", {})
        model = log.get("model", "gemini-3-flash-preview")
        cost = calc_cost(t, model)
        all_time["prompt_tokens"] += t.get("prompt_tokens", 0)
        all_time["completion_tokens"] += t.get("completion_tokens", 0)
        all_time["total_tokens"] += t.get("total_tokens", 0)
        all_time["api_calls"] += t.get("api_calls", 0)
        all_time["cost"] += cost

        # Count languages in this run
        langs_in_run = set()
        files_in_run = set()
        for entry in log.get("files", []):
            lang = entry.get("lang", "?")
            pass_name = entry.get("pass", "?")
            fname = entry.get("file", "?")
            langs_in_run.add(lang)
            files_in_run.add(fname)

            if lang not in by_lang:
                by_lang[lang] = {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0, "api_calls": 0}
            by_lang[lang]["prompt_tokens"] += entry.get("prompt_tokens", 0)
            by_lang[lang]["completion_tokens"] += entry.get("completion_tokens", 0)
            by_lang[lang]["total_tokens"] += entry.get("total_tokens", 0)
            by_lang[lang]["api_calls"] += 1

            if pass_name not in by_pass:
                by_pass[pass_name] = {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0, "api_calls": 0}
            by_pass[pass_name]["prompt_tokens"] += entry.get("prompt_tokens", 0)
            by_pass[pass_name]["completion_tokens"] += entry.get("completion_tokens", 0)
            by_pass[pass_name]["total_tokens"] += entry.get("total_tokens", 0)
            by_pass[pass_name]["api_calls"] += 1

            if fname not in by_file:
                by_file[fname] = {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0, "api_calls": 0}
            by_file[fname]["prompt_tokens"] += entry.get("prompt_tokens", 0)
            by_file[fname]["completion_tokens"] += entry.get("completion_tokens", 0)
            by_file[fname]["total_tokens"] += entry.get("total_tokens", 0)
            by_file[fname]["api_calls"] += 1

        runs.append({
            "timestamp": log.get("timestamp", "?"),
            "model": model,
            "langs": len(langs_in_run),
            "files": len(files_in_run),
            "api_calls": t.get("api_calls", 0),
            "prompt_tokens": t.get("prompt_tokens", 0),
            "completion_tokens": t.get("completion_tokens", 0),
            "total_tokens": t.get("total_tokens", 0),
            "cost": cost,
        })

    # Sort breakdowns by total tokens descending
    by_lang_sorted = sorted(by_lang.items(), key=lambda x: x[1]["total_tokens"], reverse=True)
    by_pass_sorted = sorted(by_pass.items(), key=lambda x: x[1]["total_tokens"], reverse=True)
    by_file_sorted = sorted(by_file.items(), key=lambda x: x[1]["total_tokens"], reverse=True)

    lang_names = {
        "fr": "French", "es": "Spanish", "zh": "Chinese", "ar": "Arabic",
        "ru": "Russian", "pt": "Portuguese", "de": "German", "ja": "Japanese",
        "ko": "Korean", "hi": "Hindi", "en": "English (back-translate)",
    }
    pass_names = {
        "translate": "Pass 1: Translate",
        "back_translate": "Pass 2: Back-translate",
        "evaluate": "Pass 2b: Evaluate",
        "polish": "Pass 3: Polish",
    }

    def fmt(n):
        return f"{n:,}"

    def fmt_cost(c):
        return f"${c:.4f}" if c < 1 else f"${c:.2f}"

    # Build chart data
    run_labels = json.dumps([r["timestamp"][:10] for r in runs])
    run_tokens = json.dumps([r["total_tokens"] for r in runs])
    run_costs = json.dumps([round(r["cost"], 4) for r in runs])

    lang_labels = json.dumps([lang_names.get(k, k) for k, _ in by_lang_sorted])
    lang_tokens = json.dumps([v["total_tokens"] for _, v in by_lang_sorted])

    pass_labels = json.dumps([pass_names.get(k, k) for k, _ in by_pass_sorted])
    pass_tokens = json.dumps([v["total_tokens"] for _, v in by_pass_sorted])

    # Runs table rows
    run_rows = ""
    for r in reversed(runs):
        ts = r["timestamp"]
        if len(ts) >= 9:
            display_ts = f"{ts[:4]}-{ts[4:6]}-{ts[6:8]} {ts[9:11]}:{ts[11:13]} UTC"
        else:
            display_ts = ts
        run_rows += f"""<tr>
            <td>{display_ts}</td>
            <td>{r['model']}</td>
            <td>{r['langs']}</td>
            <td>{r['files']}</td>
            <td class="num">{fmt(r['api_calls'])}</td>
            <td class="num">{fmt(r['prompt_tokens'])}</td>
            <td class="num">{fmt(r['completion_tokens'])}</td>
            <td class="num">{fmt(r['total_tokens'])}</td>
            <td class="num cost">{fmt_cost(r['cost'])}</td>
        </tr>"""

    # Language breakdown rows
    lang_rows = ""
    for k, v in by_lang_sorted:
        c = calc_cost(v)
        lang_rows += f"""<tr>
            <td>{lang_names.get(k, k)}</td>
            <td class="num">{fmt(v['api_calls'])}</td>
            <td class="num">{fmt(v['prompt_tokens'])}</td>
            <td class="num">{fmt(v['completion_tokens'])}</td>
            <td class="num">{fmt(v['total_tokens'])}</td>
            <td class="num cost">{fmt_cost(c)}</td>
        </tr>"""

    # Pass breakdown rows
    pass_rows = ""
    for k, v in by_pass_sorted:
        c = calc_cost(v)
        pass_rows += f"""<tr>
            <td>{pass_names.get(k, k)}</td>
            <td class="num">{fmt(v['api_calls'])}</td>
            <td class="num">{fmt(v['prompt_tokens'])}</td>
            <td class="num">{fmt(v['completion_tokens'])}</td>
            <td class="num">{fmt(v['total_tokens'])}</td>
            <td class="num cost">{fmt_cost(c)}</td>
        </tr>"""

    # File breakdown rows
    file_rows = ""
    for k, v in by_file_sorted:
        c = calc_cost(v)
        fname = str(k).replace(str(REPO_ROOT) + "/", "")
        file_rows += f"""<tr>
            <td><code>{fname}</code></td>
            <td class="num">{fmt(v['api_calls'])}</td>
            <td class="num">{fmt(v['prompt_tokens'])}</td>
            <td class="num">{fmt(v['completion_tokens'])}</td>
            <td class="num">{fmt(v['total_tokens'])}</td>
            <td class="num cost">{fmt_cost(c)}</td>
        </tr>"""

    pricing_model = list(PRICING.keys())[0]
    pricing_info = PRICING[pricing_model]

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>OSSIF Translation — Token &amp; Cost Report</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4"></script>
<style>
  :root {{
    --bg: #0f1117;
    --surface: #1a1d27;
    --surface2: #232733;
    --border: #2d3140;
    --text: #e1e4ed;
    --text2: #8b90a0;
    --accent: #6c8cff;
    --accent2: #9f7aea;
    --green: #48bb78;
    --orange: #ed8936;
    --red: #fc8181;
  }}
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    font-family: 'Inter', -apple-system, system-ui, sans-serif;
    background: var(--bg);
    color: var(--text);
    line-height: 1.6;
    padding: 2rem;
    max-width: 1400px;
    margin: 0 auto;
  }}
  h1 {{
    font-size: 1.8rem;
    font-weight: 700;
    margin-bottom: 0.3rem;
    background: linear-gradient(135deg, var(--accent), var(--accent2));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }}
  .subtitle {{ color: var(--text2); margin-bottom: 2rem; font-size: 0.9rem; }}
  .cards {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
    margin-bottom: 2rem;
  }}
  .card {{
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.2rem;
  }}
  .card .label {{ color: var(--text2); font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.05em; }}
  .card .value {{ font-size: 1.8rem; font-weight: 700; margin-top: 0.3rem; }}
  .card .value.cost {{ color: var(--green); }}
  .card .value.tokens {{ color: var(--accent); }}
  .card .value.calls {{ color: var(--orange); }}
  .card .detail {{ color: var(--text2); font-size: 0.75rem; margin-top: 0.2rem; }}
  .charts {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5rem;
    margin-bottom: 2rem;
  }}
  .chart-box {{
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.2rem;
  }}
  .chart-box h3 {{ font-size: 0.95rem; color: var(--text2); margin-bottom: 0.8rem; }}
  canvas {{ max-height: 260px; }}
  h2 {{
    font-size: 1.1rem;
    font-weight: 600;
    margin: 2rem 0 0.8rem;
    padding-bottom: 0.4rem;
    border-bottom: 1px solid var(--border);
  }}
  table {{
    width: 100%;
    border-collapse: collapse;
    background: var(--surface);
    border-radius: 12px;
    overflow: hidden;
    margin-bottom: 1.5rem;
    font-size: 0.85rem;
  }}
  th {{
    background: var(--surface2);
    color: var(--text2);
    font-weight: 600;
    text-transform: uppercase;
    font-size: 0.7rem;
    letter-spacing: 0.05em;
    padding: 0.8rem 1rem;
    text-align: left;
  }}
  td {{ padding: 0.6rem 1rem; border-top: 1px solid var(--border); }}
  tr:hover td {{ background: var(--surface2); }}
  .num {{ text-align: right; font-variant-numeric: tabular-nums; }}
  .cost {{ color: var(--green); font-weight: 600; }}
  code {{ background: var(--surface2); padding: 0.15em 0.4em; border-radius: 4px; font-size: 0.8rem; }}
  .pricing-note {{
    color: var(--text2);
    font-size: 0.75rem;
    margin-top: 1rem;
    padding: 0.8rem;
    background: var(--surface);
    border-radius: 8px;
    border: 1px solid var(--border);
  }}
  @media (max-width: 800px) {{
    .charts {{ grid-template-columns: 1fr; }}
    body {{ padding: 1rem; }}
  }}
</style>
</head>
<body>

<h1>OSSIF Translation Report</h1>
<p class="subtitle">{len(logs)} run{'s' if len(logs) != 1 else ''} &middot; Generated from scripts/logs/</p>

<div class="cards">
  <div class="card">
    <div class="label">Total Cost</div>
    <div class="value cost">{fmt_cost(all_time['cost'])}</div>
    <div class="detail">All-time across {len(logs)} runs</div>
  </div>
  <div class="card">
    <div class="label">Total Tokens</div>
    <div class="value tokens">{fmt(all_time['total_tokens'])}</div>
    <div class="detail">{fmt(all_time['prompt_tokens'])} prompt + {fmt(all_time['completion_tokens'])} completion</div>
  </div>
  <div class="card">
    <div class="label">API Calls</div>
    <div class="value calls">{fmt(all_time['api_calls'])}</div>
    <div class="detail">Across all passes</div>
  </div>
  <div class="card">
    <div class="label">Avg Cost / Run</div>
    <div class="value cost">{fmt_cost(all_time['cost'] / max(len(logs), 1))}</div>
    <div class="detail">{fmt(all_time['total_tokens'] // max(len(logs), 1))} tokens avg</div>
  </div>
</div>

<div class="charts">
  <div class="chart-box">
    <h3>Tokens per Run</h3>
    <canvas id="runTokensChart"></canvas>
  </div>
  <div class="chart-box">
    <h3>Cost per Run</h3>
    <canvas id="runCostChart"></canvas>
  </div>
  <div class="chart-box">
    <h3>Tokens by Language</h3>
    <canvas id="langChart"></canvas>
  </div>
  <div class="chart-box">
    <h3>Tokens by Pipeline Pass</h3>
    <canvas id="passChart"></canvas>
  </div>
</div>

<h2>Run History</h2>
<table>
  <thead><tr>
    <th>Timestamp</th><th>Model</th><th>Langs</th><th>Files</th>
    <th>Calls</th><th>Prompt</th><th>Completion</th><th>Total</th><th>Cost</th>
  </tr></thead>
  <tbody>{run_rows}</tbody>
</table>

<h2>By Language</h2>
<table>
  <thead><tr><th>Language</th><th>Calls</th><th>Prompt</th><th>Completion</th><th>Total</th><th>Cost</th></tr></thead>
  <tbody>{lang_rows}</tbody>
</table>

<h2>By Pipeline Pass</h2>
<table>
  <thead><tr><th>Pass</th><th>Calls</th><th>Prompt</th><th>Completion</th><th>Total</th><th>Cost</th></tr></thead>
  <tbody>{pass_rows}</tbody>
</table>

<h2>By Source File</h2>
<table>
  <thead><tr><th>File</th><th>Calls</th><th>Prompt</th><th>Completion</th><th>Total</th><th>Cost</th></tr></thead>
  <tbody>{file_rows}</tbody>
</table>

<div class="pricing-note">
  Costs estimated using <strong>{pricing_model}</strong> pricing: ${pricing_info['prompt']:.2f}/1M prompt tokens, ${pricing_info['completion']:.2f}/1M completion tokens.
  Update PRICING dict in <code>scripts/translation-report.py</code> if rates change.
</div>

<script>
const chartDefaults = {{
  responsive: true,
  maintainAspectRatio: false,
  plugins: {{ legend: {{ display: false }} }},
  scales: {{
    x: {{ ticks: {{ color: '#8b90a0', font: {{ size: 10 }} }}, grid: {{ color: '#2d3140' }} }},
    y: {{ ticks: {{ color: '#8b90a0', font: {{ size: 10 }} }}, grid: {{ color: '#2d3140' }} }}
  }}
}};

new Chart(document.getElementById('runTokensChart'), {{
  type: 'bar',
  data: {{
    labels: {run_labels},
    datasets: [{{ data: {run_tokens}, backgroundColor: '#6c8cff88', borderColor: '#6c8cff', borderWidth: 1, borderRadius: 4 }}]
  }},
  options: chartDefaults
}});

new Chart(document.getElementById('runCostChart'), {{
  type: 'bar',
  data: {{
    labels: {run_labels},
    datasets: [{{ data: {run_costs}, backgroundColor: '#48bb7888', borderColor: '#48bb78', borderWidth: 1, borderRadius: 4 }}]
  }},
  options: {{ ...chartDefaults, scales: {{ ...chartDefaults.scales, y: {{ ...chartDefaults.scales.y, ticks: {{ ...chartDefaults.scales.y.ticks, callback: v => '$' + v }} }} }} }}
}});

new Chart(document.getElementById('langChart'), {{
  type: 'doughnut',
  data: {{
    labels: {lang_labels},
    datasets: [{{ data: {lang_tokens}, backgroundColor: ['#6c8cff','#9f7aea','#48bb78','#ed8936','#fc8181','#63b3ed','#f6ad55','#b794f4','#68d391','#feb2b2','#90cdf4'] }}]
  }},
  options: {{ responsive: true, maintainAspectRatio: false, plugins: {{ legend: {{ position: 'right', labels: {{ color: '#8b90a0', font: {{ size: 11 }}, padding: 8 }} }} }} }}
}});

new Chart(document.getElementById('passChart'), {{
  type: 'doughnut',
  data: {{
    labels: {pass_labels},
    datasets: [{{ data: {pass_tokens}, backgroundColor: ['#6c8cff','#9f7aea','#48bb78','#ed8936'] }}]
  }},
  options: {{ responsive: true, maintainAspectRatio: false, plugins: {{ legend: {{ position: 'right', labels: {{ color: '#8b90a0', font: {{ size: 11 }}, padding: 8 }} }} }} }}
}});
</script>

</body>
</html>"""


def main():
    parser = argparse.ArgumentParser(description="OSSIF Translation Token Report")
    parser.add_argument("--last", type=int, help="Only show last N runs")
    parser.add_argument("--open", action="store_true", help="Open in browser")
    parser.add_argument("--output", type=str, help="Write to specific file instead of temp")
    args = parser.parse_args()

    logs = load_logs(limit=args.last)
    if not logs:
        print("No translation logs found in scripts/logs/")
        sys.exit(1)

    html = generate_html(logs)

    if args.output:
        out = Path(args.output)
    else:
        out = Path(tempfile.mktemp(suffix=".html", prefix="ossif-translation-report-"))

    out.write_text(html)
    print(f"Report: {out}")

    if args.open or not args.output:
        subprocess.run(["open", str(out)])


if __name__ == "__main__":
    main()
