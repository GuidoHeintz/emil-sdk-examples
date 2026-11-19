# 📦 Kunden-Wissens-Container: Werksnorm WN-104 Hochdruck-Flanschmontage

* **Container-ID:** `vault.customer.knowledge.flange_assembly_wn104`
* **Container-Klasse:** `KNOWLEDGE_SOP` (`KNOWLEDGE_BRAIN` | `INTERNAL`)
* **Branche:** `MECHANICAL_ENGINEERING`
* **Protokolle & Standards:** `DIN EN 1591`, `VDI 2230`, `SOP`, `Torque Table`

## Beschreibung
Deklarativer Wissens- & SOP-Container für Drehmomentstufen, Dichtungsauswahl und Prüfdrücke nach Werksnorm WN-104 (0 Zeilen Python-Code erforderlich).

## Enthaltene Pflicht-Dateien in diesem Vorlagen-Ordner
1. `passport.json` — Store-Passierschein, 5-Dimensionen-Klassifizierung & Abnahme-Szenarien
2. `vault_manifest.json` — Vollständiges v2.0.0 Lizenz-, DRM-, Node-Lock- & Capability-Manifest
3. `knowledge_graph.json` — Typisierte Faktenknoten & Kausalkanten
4. `smt_rules.json` — Formale Z3/SMT-Invarianten für deterministisches Veto
5. `sources/domain_reference.md` — Mensch- und maschinenlesbare Referenzdokumentation

## Kompilieren zur signierten `.emp` Datei
```bash
python ../build_customer_container_example.py --source . --output ../dist
```
