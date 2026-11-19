# Geräte-Treiber Spezifikation: Fertigungszelle S7-1500 (OPC-UA & Modbus-TCP)

## 1. Hardware-Lock & Capability-Modell
Solange dieser Container nicht aktiv gemountet ist, blockiert das `HardwareCapabilityGate` von EMIL jeden Socket-Zugriff auf die Steuerung (`plc_s7_1500_cell_read`, `plc_s7_1500_cell_write`).

## 2. Adress- und Register-Mapping
| Signalname | OPC-UA NodeID | Modbus-TCP Register | Datentyp | Grenzwert (Z3/SMT) |
| :--- | :--- | :--- | :--- | :--- |
| `target_spindle_rpm` | `ns=4;s=Cell1.Spindle.TargetRPM` | `40102` | `UINT16` | `0 .. 12.000 RPM` |
| `coolant_pressure_bar` | `ns=4;s=Cell1.Coolant.PressureBar` | `40108` | `FLOAT32` | `>= 4,5 bar` |
| `watchdog_heartbeat_ms` | `ns=4;s=Cell1.Safety.WatchdogMs` | `40001` | `UINT16` | `<= 50 ms` |
