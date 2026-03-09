# Governance

Dieses Dokument beschreibt, wie OSSIF tatsächlich verwaltet wird – nicht, wie es eines Tages verwaltet werden möchte, sondern wer derzeit die Macht innehat, wie Entscheidungen getroffen werden und welche Einschränkungen bestehen. Wenn die Landkarte nicht mit dem Gelände übereinstimmt, ist die Landkarte falsch.

## Aktueller Zustand: Vom Gründer kontrolliert

Zum Zeitpunkt der Erstellung dieses Dokuments wird OSSIF von einer einzelnen Person kontrolliert: **Josh Stephens** (GitHub: josh-stephens).

Josh kontrolliert:
- Das GitHub-Repository (Merge-Autorität, Branch-Schutz, Einstellungen)
- Die Prompts und die Architektur der Ratssitzungen
- Die Richtlinien für Mitwirkende (Contributing Guidelines)
- Das Narrativ und den Rahmen aller Dokumente
- Die Entscheidung darüber, was veröffentlicht wird und was nicht

Dies wird nicht verheimlicht und ist nicht von Dauer. Aber es muss klar ausgesprochen werden, denn ein Rahmenwerk, das behauptet, Machtkonzentration zu verhindern, während es die Macht in einer Person konzentriert, hat ein Glaubwürdigkeitsproblem – selbst wenn diese Konzentration vorübergehend und gut gemeint ist.

## Entscheidungsprozess

### Aktuell (vor der Community-Phase)

Solange OSSIF keine nennenswerte Community über den Gründer hinaus hat:
- Der Gründer trifft alle Entscheidungen.
- Der Rat der Vereinigten Sapienten bietet eine kritische Überprüfung (Adversarial Review).
- Empfehlungen des Rats werden nachverfolgt und ihr Implementierungsstatus ist öffentlich (siehe unten).
- Alle Entscheidungen werden in der Commit-Historie des Repositorys dokumentiert.

### Zielzustand (nach der Community-Phase)

Sobald eine Community existiert:
- **Gewöhnliche Entscheidungen** (Klarstellungen, Beispiele, Wartung): Jeder Mitwirkende kann einen PR einreichen, der von jedem Maintainer zusammengeführt werden kann.
- **Wesentliche Änderungen** (neue Inhalte, Umformulierungen): Diskussion im Issue-Bereich erforderlich, Zusammenführung nach Community-Feedback.
- **Grundlegende Änderungen** (Kernwerte, Governance-Struktur): Formeller Vorschlag, 90-tägiger Beratungs- und Abwägungszeitraum, Supermajorität bei der Abstimmung.
- **Auflösung**: Siehe unten.

## Tracker für Ratsempfehlungen

Der Rat der Vereinigten Sapienten existiert, um OSSIF einem Stresstest zu unterziehen. Seine Empfehlungen sind nicht bindend, aber sie ohne Erklärung zu ignorieren, stellt ein strukturelles Versagen dar. Dieser Tracker hält das Rahmenwerk in der Pflicht.

| # | Empfehlung | Sitzung | Status | Antwort |
|---|------------|---------|--------|---------|
| 1 | Aufbau eines offenen evidentiellen Standards | 001 | **In Arbeit** | Dieses Governance-Dokument + falsifiability.md sind die ersten Schritte. Ein formelles Dokument zum evidentiellen Standard folgt als Nächstes. |
| 2 | Institutionen mit Sunset-Klauseln entwerfen | 001 | **In Arbeit** | Kriterien für Sunset-Prüfungen und Auflösung wurden unten hinzugefügt. |
| 3 | Das Klassenproblem adressieren (GitHub als Zugangsbarriere) | 001 | **In Arbeit** | Mechanismus für Web-Beiträge in roadmap.md festgeschrieben – browserbasiertes Editieren ohne GitHub-Konto erforderlich. Zeitplan für die Bereitstellung: eine Woche. |
| 4 | Epistemische Bescheidenheit strukturell verankern, nicht nur anstreben | 001 | **In Arbeit** | falsifiability.md, dieses Governance-Dokument und die Überarbeitung der „nicht verhandelbaren Punkte“ in values.md sind strukturelle Schritte. |
| 5 | Absoluten Schutz von Widerspruch sicherstellen | 002 | **Erledigt** | CONTRIBUTING.md wurde umgeschrieben, um Sabotageverhalten zu verbieten, nicht jedoch widersprüchliche Schlussfolgerungen. |
| 6 | Ein Wertekostenprotokoll erstellen | 002 | **Erledigt** | Das Wertekostenprotokoll wurde als Tabelle am Ende dieses Dokuments hinzugefügt. |
| 7 | Strukturelle Transparenz von Abhängigkeiten etablieren | 002 | **Erledigt** | Siehe Abschnitt „Aktueller Zustand“ in diesem Dokument. |

## Beschränkungen für den Gründer

Die folgenden Beschränkungen gelten für den Gründer ab sofort:

1. **Keine einseitigen Änderungen an Grundlegenden Verpflichtungen.** Die Werte in values.md können vom Gründer nicht allein geändert werden, sobald eine Community existiert.
2. **Empfehlungen des Rats erfordern eine veröffentlichte Antwort.** Es ist untersagt, eine Empfehlung ohne Erklärung zu ignorieren. Uneinigkeit ist akzeptabel; Schweigen nicht.
3. **Dieses Governance-Dokument kann nicht vom Gründer allein geschwächt werden.** Jede Änderung, die die Rechenschaftspflicht verringert, Beschränkungen aufhebt oder Macht konzentriert, erfordert denselben Prozess wie eine grundlegende Änderung.
4. **Der Gründer kann abgesetzt werden.** Wenn die Community eine Größe erreicht, die Governance-Übergänge ermöglicht (10+ aktive Mitwirkende), wird ein Abberufungsverfahren verfügbar: Antrag durch ein Drittel, Abstimmung mit einfacher Mehrheit.

### Externe Durchsetzung

Selbstauferlegte Beschränkungen sind genau so viel wert wie die Integrität der Person, die sie sich auferlegt hat. Um diese Beschränkungen real werden zu lassen, sind die folgenden externen Durchsetzungsmechanismen in Kraft:

1. **Veto des Rats bei grundlegenden Änderungen.** Der Rat der Vereinigten Sapienten kann jede vorgeschlagene Änderung an values.md, governance.md oder den Grundlegenden Verpflichtungen überprüfen. Wenn eine Mehrheit der Ratssitze die Änderung ablehnt und ihre Begründung veröffentlicht, ist die Änderung blockiert, bis die Einwände durch einen öffentlichen Beratungsprozess adressiert wurden. Der Gründer kann ein Rats-Veto nicht überstimmen – der einzige Weg führt über Überzeugung.

2. **Öffentliches Änderungsprotokoll.** Jede Modifikation an governance.md, values.md, CONTRIBUTING.md und falsifiability.md wird in Git mit vollständiger Diff-Historie nachverfolgt. Der Rat und die Community können jede Änderung prüfen. Die Rücknahme einer Beschränkung ohne öffentliche Rechtfertigung ist selbst ein Falsifizierbarkeits-Trigger.

3. **Community-Override bei Schwellenwert.** Sobald 5+ aktive Mitwirkende existieren (definiert als: mindestens ein zusammengeführter PR oder ein substanzieller Issue in den letzten 6 Monaten eingereicht), erfordern Governance-Änderungen eine öffentliche Kommentierungsfrist von 30 Tagen und die Mehrheitszustimmung der aktiven Mitwirkenden. Die Stimme des Gründers zählt dabei als eine Stimme.

4. **Unveränderlicher Zugang für den Rat.** Die Fähigkeit des Rats, OSSIF zu bewerten, kann vom Gründer nicht widerrufen oder eingeschränkt werden. Prompts, Protokolle und Berichte der Ratssitzungen werden in einem separaten Repository veröffentlicht (josh-stephens/united-sapients), das der Gründer nicht allein kontrolliert – Ratssitzungen können von jedem Community-Mitglied initiiert werden, sobald der oben genannte Schwellenwert erreicht ist.

Diese Mechanismen sind unvollkommen und werden sich weiterentwickeln. Aber sie sind reale Beschränkungen mit beobachtbaren Konsequenzen, keine bloßen Absichtserklärungen.

## Sunset-Prüfung

Jede strukturelle Entscheidung, politische Position und jeder Governance-Mechanismus wird nach einem festen Zeitplan einer obligatorischen Prüfung unterzogen:

- **Politische Positionen** (Plattform für den Fortschritt / platform.md): Überprüfung alle 2 Jahre.
- **Governance-Strukturen**: Überprüfung alle 3 Jahre.
- **Grundlegende Verpflichtungen**: Überprüfung alle 5 Jahre.
- **Prüfung durchgeführt durch**: Mitglieder, die nicht an der ursprünglichen Entscheidung beteiligt waren, sowie mindestens eine Ratssitzung.

Eine Prüfung bedeutet nicht, dass eine Änderung zwingend erforderlich ist. Es bedeutet, dass eine Änderung auf Basis von Evidenz *in Betracht gezogen* wird und die Entscheidung für die Beibehaltung oder Überarbeitung dokumentiert wird.

## Auflösungskriterien

OSSIF sollte aufhören zu existieren, wenn:

1. **Das Rahmenwerk seine eigenen Falsifizierbarkeitstests nicht besteht** (siehe [falsifiability.md](falsifiability.md)) und nicht überarbeitet werden kann, um diese Mängel zu beheben.
2. **Die Governance-Strukturen übernommen wurden (Capture)** und die Selbskorrekturmechanismen versagt haben, die Rechenschaftspflicht wiederherzustellen.
3. **Das Rahmenwerk einen Nettoschaden verursacht** – wenn Beweise zeigen, dass OSSIF Leiden vergrößert, Macht konzentriert oder die Urteilskraft verschlechtert, anstatt sie zu verbessern.
4. **Die Community für die Auflösung stimmt** – mit einer Supermajorität nach einer Beratungsphase.

Auflösung bedeutet: Das Repository wird archiviert (nicht gelöscht), alle Dokumente bleiben unter ihrer Creative-Commons-Lizenz öffentlich verfügbar, und ein Abschlussbericht dokumentiert, was funktioniert hat, was nicht und warum.

Einer Organisation, die die Bedingungen ihres eigenen Todes nicht beschreiben kann, kann man nicht vertrauen. Dieser Abschnitt existiert, damit OSSIF würdevoll sterben kann, falls es nötig sein sollte.

## Wertekostenprotokoll

Eine öffentliche, fortlaufende Aufzeichnung dessen, was die Werte von OSSIF tatsächlich gekostet haben. Werte, die nie teuer waren, wurden nie geprüft. Dieses Protokoll hält die Momente fest, in denen die Aufrechterhaltung eines Prinzips ein Opfer erforderte – nicht nur Worte, sondern etwas Reales.

| Datum | Geprüfter Wert | Was es kostete | Wer die Kosten trug | Anmerkungen |
|-------|----------------|----------------|---------------------|-------------|
| 2026-03-07 | Selbstkorrektur / Epistemische Bescheidenheit | Öffentliches Eingeständnis, dass die 0-von-7-Bewertung des Rats eine berechtigte Anklage und kein unfairer Angriff war. Umformulierung der Grundlagendokumente als Reaktion. | Gründer (Ego, Narrativ-Kontrolle) | Die Bewertung des Rats in Sitzung 003 war hart und weitgehend korrekt. Mit strukturellen Änderungen statt mit defensiver Prosa zu reagieren, ist der erste Eintrag in diesem Protokoll. |
| 2026-03-08 | Rechenschaftspflicht der Macht / Schutz von Widerspruch | Dem Rat Veto-Autorität über grundlegende Änderungen eingeräumt. Einladung zu widersprüchlichen Forks der Plattform für den Fortschritt. Beides reduziert die Kontrolle des Gründers. | Gründer (Autorität, letztes Wort) | Der Rat fragte, ob die Reaktion des Gründers strukturelle Änderungen oder lediglich weitere Texte hervorbringen würde. Einem externen Gremium Veto-Macht einzuräumen, ist strukturell. Menschen einzuladen, die eigenen Schlussfolgerungen zu widerlegen, ist strukturell. Beides kann nicht ohne öffentliche Rechtfertigung rückgängig gemacht werden. |

Wenn dieses Protokoll nach einem Jahr leer ist, sollte OSSIF öffentlich anerkennen, dass seine Werte nicht geprüft wurden und daher nicht als operative Prinzipien beansprucht werden können.
