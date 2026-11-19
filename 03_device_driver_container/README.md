# 📦 Kunden-Treiber-Container: Fertigungszelle S7-1500 (OPC-UA / Modbus HAL)

* **Container-ID:** `vault.customer.driver.siemens_s7_opcua_cell`
* **Container-Klasse:** `DEVICE_DRIVER` (`HARDWARE_HAL` | `BIDIRECTIONAL`)
* **Branche:** `INDUSTRIAL_AUTOMATION`
* **Protokolle & Standards:** `OPC-UA`, `IEC 62541`, `Modbus-TCP`, `SPS HAL`

## Beschreibung
Autarker Hardware-Treiber-Container für eine Kunden-Fertigungszelle mit HardwareCapabilityGate, Register-Mapping und RAM-Zeroization beim Aushängen.

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
