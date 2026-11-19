# 📦 Kunden-Aktorik-Container: Closed-Loop Cobot-Palettierer (ISO/TS 15066)

* **Container-ID:** `vault.customer.actuator.cobot_safe_palletizer`
* **Container-Klasse:** `ACTUATOR_ACTION` (`ACTUATOR_MOTOR` | `BIDIRECTIONAL`)
* **Branche:** `ROBOTICS_AUTOMATION`
* **Protokolle & Standards:** `ISO/TS 15066`, `CiA 402`, `Closed-Loop Reflex`, `Zero Roundtrip`

## Beschreibung
Closed-Loop Sensorik- & Aktorik-Container: Verarbeitet Laser-Schutzfeld und Greifkraft-Telemetrie in Echtzeit (< 1,5 ms) und begrenzt Kontaktkräfte nach ISO/TS 15066 auf <= 65 N.

## Enthaltene Pflicht-Dateien in diesem Vorlagen-Ordner
1. `passport.json` — Store-Passierschein, 5-Dimensionen-Klassifizierung & Abnahme-Szenarien
2. `vault_manifest.json` — Vollständiges v2.0.0 Lizenz-, DRM-, Node-Lock- & Capability-Manifest
3. `knowledge_graph.json` — Typisierte Faktenknoten & Kausalkanten
4. `smt_rules.json` — Formale Z3/SMT-Invarianten für deterministisches Veto
5. `sources/domain_reference.md` — Mensch- und maschinenlesbare Referenzdokumentation
6. `vault_runtime.py` — Aktive Python-Runtime (`BaseVaultRuntime` kompatibel)

## Kompilieren zur signierten `.emp` Datei
```bash
python ../build_customer_container_example.py --source . --output ../dist
```
