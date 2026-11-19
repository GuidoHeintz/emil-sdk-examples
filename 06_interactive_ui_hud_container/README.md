# 📦 Kunden-UI-Container: Smart Presswerk Leitstand & EPL 2.0 Cockpit

* **Container-ID:** `vault.customer.ui.smart_press_cockpit`
* **Container-Klasse:** `ACTUATOR_ACTION` (`ACTUATOR_MOTOR` | `BIDIRECTIONAL`)
* **Branche:** `INDUSTRIAL_AUTOMATION`
* **Protokolle & Standards:** `EPL 2.0`, `Omni-HUD`, `HTML5 Cockpit`, `Proof-Gated UI`

## Beschreibung
Vollständiger AI Container mit eingebetteter HTML5-Leitstand-UI (ui/cockpit.html) und deklarativer EPL 2.0 Oberfläche (epl_layout.emls.json): Koppelt UI-Schalter direkt an den Z3/SMT-Beweisstatus (release_trigger: on_proof_success).

## Enthaltene Pflicht-Dateien in diesem Vorlagen-Ordner
1. `passport.json` — Store-Passierschein, 5-Dimensionen-Klassifizierung & Abnahme-Szenarien
2. `vault_manifest.json` — Vollständiges v2.0.0 Lizenz-, DRM-, Node-Lock- & Capability-Manifest
3. `knowledge_graph.json` — Typisierte Faktenknoten & Kausalkanten
4. `smt_rules.json` — Formale Z3/SMT-Invarianten für deterministisches Veto
5. `sources/domain_reference.md` — Mensch- und maschinenlesbare Referenzdokumentation
6. `vault_runtime.py` — Aktive Python-Runtime (`BaseVaultRuntime` kompatibel)
7. `ui/cockpit.html` — Interaktives HTML5-Leitstand-Dashboard (direkt im Browser oder via `--serve-ui` nutzbar)
8. `ui/epl_layout.emls.json` — Deklaratives EPL 2.0 Layout-Schema für das EMIL Omni-HUD

## Kompilieren zur signierten `.emp` Datei
```bash
python ../build_customer_container_example.py --source . --output ../dist
```
