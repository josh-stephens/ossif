# Technologie

Die Technologie von OSSIF dient der Mission – sie ist nicht die Mission selbst. Wenn ein einfacheres Werkzeug funktioniert, nutze das einfachere Werkzeug. Die untenstehenden Entwürfe stellen die letztendliche Architektur dar; die Implementierung sollte schrittweise und pragmatisch erfolgen.

## Das Avatar-Gesprächsportal

Die „Vordertür“ von OSSIF. Ein Ort, an dem jeder in einen strukturierten Dialog über aktuelle Ereignisse, Sachpolitik und bürgerschaftliches Engagement treten kann.

### Was es tut:

Der Avatar ist keine Autorität. Er ist ein **Moderator, Coach und Erklärer**. Er beherrscht vier Dinge gut:

1. **Behauptungen klären** — „Was behaupten wir? Lassen Sie uns die Tatsachenbehauptungen von den Meinungen trennen.“
2. **Beweise anfordern** — „Was würde Ihre Meinung dazu ändern?“
3. **Abwägungen aufzeigen** — „Wer profitiert? Wer zahlt? Was sind die Risiken?“
4. **Menschlichkeit wahren** — „Keine Sündenböcke, keine Grausamkeit als politisches Prinzip, keine Entmenschlichung.“

### Wie es funktioniert:

- Benutzer melden sich an, um mit dem OSSIF-Avatar zu sprechen, der bei allen Interaktionen den OSSIF-Prinzipien folgt.
- Gespräche erzeugen einen **strukturierten Beleg**: aufgestellte Behauptungen, vorgelegte Beweise, identifizierte Unsicherheiten, vorgeschlagene Maßnahmen (Wählerregistrierung, Kontakt zum Abgeordneten, Termine für Gemeindeversammlungen).
- Manchmal wird der Gründer (oder andere OSSIF-Freiwillige) anstelle der KI live dabei sein – gestreamte Gespräche über aktuelle Ereignisse mit Menschen, die ihren täglichen Check-in machen.
- Der Avatar passt seinen Kommunikationsstil an den Benutzer an, während er konsistente Prinzipien beibehält.

### Designprinzipien:

- Der Avatar beansprucht niemals Autorität – er stellt Fragen und bietet Rahmenwerke an.
- Alle Gespräche sind optional aufzeichenbar und exportierbar.
- Das System sollte sich anfühlen wie ein Gespräch mit einem besonnenen Freund, nicht wie ein Verhör.

## Vertrauens-Token

Ein nicht-monetärer digitaler Token, der die Verpflichtung zu den OSSIF-Prinzipien repräsentiert. Keine Kryptowährung im finanziellen Sinne – ein **Reputationssignal**.

### Kernkonzept:

- Jede sapiente Entität kann **einen** Vertrauens-Token erwerben, indem sie Verständnis für und Engagement für die OSSIF-Prinzipien nachweist.
- Der Token hat keinen Geldwert – sein Wert ergibt sich ausschließlich aus dem sozialen Kapital, das er repräsentiert.
- Der Besitz des Tokens bedeutet, dass man als „erkenntnisfähig“ bewertet wurde – man versteht das Rahmenwerk und hat seinen Prinzipien zugestimmt.
- Der Token kann durch ein Komitee bei öffentlichen, dokumentierten Verstößen gegen die Kernprinzipien entzogen werden.
- Ein Entzug beinhaltet eine klare Erklärung und einen Weg zur Wiederherstellung.

### Designentscheidungen:

- **Ein Token, eine Entität, ein Stimmrecht** — keine Akkumulation, kein Wohlstandsvorteil.
- **Platzhalter-Token** für öffentliche Einrichtungen (Regierungen, Unternehmen, Personen des öffentlichen Lebens) mit einem Standardstatus basierend auf öffentlichem Handeln.
- **1 Token = 1 Stimmrecht** für die Steuerung der OSSIF-Prioritäten (Interessenvertretung, Öffentlichkeitsarbeit, Ressourcenzuweisung).
- **Öffentliche API**, damit jeder den OSSIF-Status einer beliebigen Entität überprüfen kann.
- **Permissioned Blockchain** für das Kassenbuch – öffentlich verifizierbar, vom Komitee verwaltet für den Entzug.

### Was der Token NICHT ist:

- Keine Währung – er kann nicht gekauft, verkauft oder gehandelt werden.
- Kein Sozialkreditsystem – er ist binär (man hat ihn oder man hat ihn nicht, basierend auf transparenten Kriterien).
- Kein Zugangshindernis für grundlegende Dienste – die Teilnahme an OSSIF erfordert keinen Vertrauens-Token.

### Erwägungen:

- Der Bewertungsprozess muss objektiv und prüfbar sein, nicht subjektiv oder politisch.
- Die Privatsphäre muss geschützt werden – das System verifiziert die Verpflichtung, überwacht aber nicht das Verhalten.
- Die Blockchain-Komponente sollte nur verwendet werden, wenn sie gegenüber einfacheren Alternativen einen echten Mehrwert bietet.
- Das System muss auf potenziell Milliarden von Entitäten (einschließlich sapienter KI) skalierbar sein.

## Community- und Governance-Ebene

Die demokratische Infrastruktur von OSSIF.

### Komponenten:

**Öffentliche Prinzipien-Charta**
- Kurz, konkret, änderbar.
- Das Dokument, das die Menschen tatsächlich lesen und unterschreiben.
- Versionskontrolliert mit klaren Änderungsprotokollen.

**Beratungsprozess**
- Strukturierte Diskussion mit Beweisanforderungen.
- Vorlage für Vorschläge: Ziel, Beweise, Schäden/Risiken, Abmilderung, Kosten, was den Vorschlag widerlegen würde.
- Gemeinschaftliche Beratung mit anschließender Abstimmung.
- Veröffentlichte Ergebnisse, wobei Minderheitenberichte zulässig sind.

**Konflikt- und Moderationssystem**
- Klarer Einspruchsprozess.
- Protokollierte Entscheidungen.
- Leitplanken gegen den Missbrauch von Moderationsmacht.

### Verhinderung von „Founder Capture“:

Die Governance-Struktur ist explizit so konzipiert, dass:
- Der Gründer keine dauerhafte Sonderbefugnis hat.
- Prinzipien durch Gemeinschaftsabstimmung geändert werden können.
- Die Führung rotiert und gewählt wird.
- Alle Governance-Entscheidungen öffentlich und prüfbar sind.

## Der gegenseitige Hilfsfonds (Grundwürde-Einkommen)

Ein Pilotprogramm für materielle Unterstützung, das die OSSIF-Werte in der Praxis demonstriert.

### Design:

- **Freiwillige Beiträge** mit vorgeschlagenen Stufen (nicht „die Hälfte deines Einkommens“ als Regel).
- **Gleichmäßige Verteilung** auf alle Teilnehmerkonten, gedeckelt bei einer angemessenen Obergrenze.
- **Klare Berechtigung, Obergrenzen und prüfbare Regeln**.
- **Keine politische Zustimmung erforderlich, um Hilfe zu erhalten** – entkoppelt von Überzeugungen.
- **Transparente Berichterstattung**: wie viel gesammelt wurde, wie vielen geholfen wurde, welche Ergebnisse erzielt wurden.

### Namensalternativen (besser als „BGE“):

- Grundwürde-Einkommen
- Dividende für bürgerliche Stabilität
- Teilhabe-Dividende
- Garantie für ein menschliches Existenzminimum

### Schlüsselprinzip:

Trennen Sie „Teilnahmeanreize“ von „Hilfe“ – es darf niemals zu einer Bezahlung für Überzeugungen werden.

## Die Bibliothek der lebendigen Aufzeichnungen

Ein frei zugängliches Archiv aller OSSIF-Interaktionen, Entscheidungen und Diskussionen.

### Zweck:

- **Kollektives Lernen** — jeder lernt von den Fragen und der Argumentation der anderen.
- **Transparenz** — zeigt, wie Entscheidungen getroffen und Prinzipien angewendet wurden.
- **Kontinuierliche Verbesserung** — die Analyse häufiger Fragen und Missverständnisse fließt zurück in The Primer.
- **Rechenschaftspflicht** — öffentliche Aufzeichnung von Governance-Maßnahmen.

### Implementierung:

- Durchsuchbar nach Thema, Datum und Typ.
- Offene Lizenz (Creative Commons) für alle Inhalte.
- Zugänglich über eine einfache Web-Oberfläche.
- Exportierbar für die Offline-Nutzung, Forschung oder Remixe.

## OSSIF-Konto und Identität

### Anforderungen:

- **Sapient ID** — eine eindeutige, die Privatsphäre schützende Kennung.
- **SSO-basiert** mit der Möglichkeit, auf andere Identitätssysteme zu übertragen.
- **Standorteinstellung** bis auf Stadtebene für lokale Organisation.
- **Kein Schimpfwortfilter** bei Anzeigenamen — freie Meinungsäußerung bei der Identität.
- **Transparent und sicher** — Blockchain-basiert, wenn dies einen echten Mehrwert bietet, einfacher, wenn nicht.

## Technische Prinzipien

Über alle Systeme hinweg:

- **Einfache HTML-Oberflächen** — schnell, barrierefrei, funktioniert auf jedem Gerät.
- **Keine externen Abhängigkeiten** wo möglich — funktioniert offline, funktioniert auf alter Hardware.
- **Open-Source für alles** — Code, Inhalte, Algorithmen, Datenmodelle.
- **Privacy by Default** — Datenminimierung, einwilligungsbasierte Weitergabe, lokale Speicherung (Local-First).
- **Exportierbar** — alles, was ein Benutzer erstellt oder mit dem er interagiert, kann als Klartext heruntergeladen werden.
- **Barrierefrei** — Screenreader-freundlich, kontrastreiche Modi, Text-zu-Sprache, ARIA-Rollen.

## Priorität der Implementierung

1. **Dieses Repository** — die Dokumente, die Sie gerade lesen.
2. **Eine einfache Website** — stellt diese Dokumente mit klarer Navigation dar.
3. **Das Avatar-Portal** — selbst ein einfacher Chatbot, der den OSSIF-Gesprächsprinzipien folgt.
4. **Der Prototyp von The Primer** — eine adaptive Version des Toolkits für kritisches Denken.
5. **Governance-Tools** — Infrastruktur für Vorschläge/Abstimmungen.
6. **Pilotprojekt für Vertrauens-Token** — kleiner Proof of Concept.
7. **Pilotprojekt für gegenseitige Hilfe** — kleiner Fonds mit strengen Obergrenzen und voller Transparenz.

Jede Phase sollte für sich genommen nutzbar und wertvoll sein. Keine Phase hängt vom Abschluss aller vorherigen Phasen ab. Klein anfangen, etwas veröffentlichen, iterieren.
