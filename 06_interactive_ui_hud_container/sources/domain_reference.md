# Kunden-UI-Container: Smart Presswerk Leitstand & EPL 2.0 Cockpit

## 1. Wie stellt ein `.emp` AI Container in EMIL eine eigene UI bereit?
Ein Container kann auf **zwei sich ergänzenden Wegen** eine Benutzeroberfläche bereitstellen:
1. **Deklarativ über EPL 2.0 (`ui/epl_layout.emls.json` + `orchestrate_epl()` in `vault_runtime.py`):**
   Das EMIL Desktop Omni-HUD (`emil_desktop_hud.py`) und der Sovereign Workplace (`/workspace`) rendern die vom Container gelieferten EPL-Karten, Metriken und Aktuatoren nativ.
2. **Als eingebettetes HTML5-Cockpit (`ui/cockpit.html` direkt im `.emp`-Archiv):**
   Für komplexe Leitstände, R&I-Fließbilder oder Maschinen-Dashboards liefert der Container im Ordner `ui/` eine autarke HTML5-Oberfläche mit, die ohne externe Abhängigkeiten in jedem Browser oder eingebetteten WebView läuft.

## 2. Beweisgebundene UI-Elemente (`release_trigger: "on_proof_success"`)
In EMIL sind UI-Buttons keine ungeschützten Auslöser: Solange der Z3/SMT-Prüfkern eine Verletzung meldet (`UNSAT`), bleiben die Aktuatoren im UI gesperrt (`armed: false`).
