# Symmetrischer Domain Codec: Proprietäres QDF-Messprotokoll (`.qdf`)

## 1. Zweck des Containers
Viele Qualitätsabteilungen besitzen Koordinatenmessmaschinen (KMG), die Ergebnisse in einem hausinternen Textformat (`.qdf`) ausgeben:
```text
PART_ID=B-9920|FEATURE=BOHRUNG_D42|NOMINAL_MM=42.000|ACTUAL_MM=42.008|TOL_MM=0.015
```

## 2. Symmetrische Verarbeitung (`decode` & `encode`)
* **Sensorik (`decode`):** Parst `.qdf`-Zeilen verlustfrei in typisierte Wissensknoten und prüft sofort `|ACTUAL_MM - NOMINAL_MM| <= TOL_MM`.
* **Motorik (`encode`):** Synthetisiert aus verifizierten Graphenknoten wieder ein 100 % standardkonformes `.qdf`-Protokoll auf die lokale Festplatte (0 Bytes Cloud-Egress).
