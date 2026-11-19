# 📦 Kunden-Codec-Container: Symmetrischer QDF-Messmaschinen-Codec (Decode & Encode)

* **Container-ID:** `vault.customer.codec.qdf_quality_protocol`
* **Container-Klasse:** `PERCEPTION_CODEC` (`SENSOR_ORGAN` | `BIDIRECTIONAL`)
* **Branche:** `QUALITY_MANAGEMENT`
* **Protokolle & Standards:** `QDF Legacy`, `ISO 10360`, `Symmetric Codec`, `Zero Egress`

## Beschreibung
Symmetrischer Domain Codec für proprietäre Koordinatenmessmaschinen-Protokolle (.qdf): Liest Rohdaten verlustfrei in den Wissensgraphen ein (Decode) und erzeugt normkonforme Prüfberichte (Encode).

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
