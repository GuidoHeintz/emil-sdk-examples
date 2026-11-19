# 📦 Kunden-Wächter-Container: Einkaufs-Compliance & 4-Augen-Freigabe (SoD)

* **Container-ID:** `vault.customer.guardrail.procurement_four_eyes_sod`
* **Container-Klasse:** `GUARDRAIL_VETO` (`SAFETY_GUARD` | `INTERNAL`)
* **Branche:** `FINANCE_ERP`
* **Protokolle & Standards:** `SAP MM`, `Segregation of Duties`, `Z3 SMT Veto`, `FIDO2`

## Beschreibung
Deterministischer Z3/SMT-Compliance-Wächter für SAP/ERP-Bestellanforderungen: Erzwingt 4-Augen-FIDO2-Signatur ab 10.000 EUR und blockiert gesperrte Lieferanten.

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
