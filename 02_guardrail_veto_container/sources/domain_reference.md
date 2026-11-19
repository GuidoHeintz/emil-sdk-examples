# Konzern-Einkaufsrichtlinie: Freigabegrenzen & 4-Augen-Prinzip (SoD)

## 1. Wertgrenzen für automatisierte und manuelle Bestellungen
* **Bis 10.000,00 EUR netto:** Einzelzeichnung durch autorisierten Einkäufer zulässig.
* **Ab 10.000,01 EUR netto:** Zwingendes **4-Augen-Prinzip** mit zweiter FIDO2-Hardware-Signatur (`fido2_second_approver_signed == True`).

## 2. Strikte Funktionstrennung (Segregation of Duties)
Die Benutzer-ID des Bestellanforderers (`requester_id`) darf unter keinen Umständen mit der Benutzer-ID des Freigebers (`approver_id`) übereinstimmen.
