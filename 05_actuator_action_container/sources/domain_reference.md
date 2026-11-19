# Closed-Loop Aktorik-Container: Cobot-Palettierer nach ISO/TS 15066

## 1. Sicherheitsarchitektur (Sense-to-Act in < 1,5 ms)
Dieser Container empfängt in jedem Zyklus die aktuellen Sensordaten (`contact_force_n`, `human_distance_mm`) und gibt nur nach bestandener Z3/SMT-Prüfung den nächsten Trajektorien-Sollwert (`target_pose_xyz`) frei.

## 2. Deterministische Veto-Schranken
* **Schutzabstand (`human_distance_mm < 150.0 mm`):** Sofortiges `VETO` -> `emergency_brake = True`.
* **Kontaktkraft (`contact_force_n > 65.0 N`):** Sofortiges `VETO` -> Drehmoment-Freischaltung (Safe Torque Off).
