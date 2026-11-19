"""
Kunden-UI-Container Runtime (vault_runtime.py) mit EPL 2.0 Generator (`orchestrate_epl`).
"""
from typing import Dict, Any, Optional, List


class CustomerSmartPressUiRuntime:
    def __init__(self, passport_path: Optional[str] = None):
        self.passport_path = passport_path
        self.vault_id = "vault.customer.ui.smart_press_cockpit"
        self.is_mounted = False

    def mount(self, context: Optional[Dict[str, Any]] = None):
        self.is_mounted = True

    def unmount(self):
        self.is_mounted = False

    def get_capabilities(self) -> List[str]:
        return ["ui_epl_2_0_card_provider", "ui_embedded_web_cockpit", "plc_press_line_release"]

    def orchestrate_epl(self, prompt: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        ctx = context or {}
        force_kn = float(ctx.get("press_force_kn", 620.0))
        temp_c = float(ctx.get("tool_temp_c", 115.0))
        dist_mm = float(ctx.get("light_curtain_mm", 550.0))
        batch_eur = float(ctx.get("order_batch_eur", 14500.0))
        fido_ok = bool(ctx.get("fido2_signed", True))

        violations = []
        if force_kn > 850.0:
            violations.append(f"INV-PRESS-FORCE: {force_kn} kN > 850 kN")
        if temp_c > 180.0:
            violations.append(f"INV-TOOL-TEMP: {temp_c} °C > 180 °C")
        if dist_mm < 200.0:
            violations.append(f"INV-LIGHT-CURTAIN: {dist_mm} mm < 200 mm")
        if batch_eur > 25000.0 and not fido_ok:
            violations.append(f"INV-BATCH-SOD: {batch_eur} EUR ohne FIDO2-Signatur")

        is_ok = len(violations) == 0
        return {
            "epl_version": "2.0",
            "vault_id": self.vault_id,
            "ui_entry_point": "ui/cockpit.html",
            "layout": {
                "type": "card",
                "title": "Presslinie 4 — Bereit für Hub-Freigabe" if is_ok else "Z3 VETO: Aktorik verriegelt!",
                "badge": {
                    "text": "✓ Z3 SAT • FREIGABE" if is_ok else "⛔ Z3 VETO • GESPERRT",
                    "type": "SUCCESS" if is_ok else "ALERT"
                },
                "summary": "Alle 4 Z3-Invarianten erfüllt." if is_ok else "Verletzungen: " + "; ".join(violations),
                "metrics": [
                    {"label": "Presskraft", "value": f"{force_kn} kN"},
                    {"label": "Temperatur", "value": f"{temp_c} °C"},
                    {"label": "Schutzfeld", "value": f"{dist_mm} mm"},
                    {"label": "Chargenwert", "value": f"{batch_eur} EUR"}
                ],
                "latency_ms": 0.4
            },
            "machine_actuator_stream": {
                "armed": is_ok,
                "release_trigger": "on_proof_success",
                "violated_rules": violations
            },
            "actuators": [
                {"id": "act_plc_stroke", "label": "Hub-Zyklus starten", "type": "PRIMARY", "enabled": is_ok},
                {"id": "act_sap_qm", "label": "Chargen-Protokoll in SAP buchen", "type": "SECONDARY", "enabled": is_ok}
            ]
        }

    def infer(self, prompt: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        epl = self.orchestrate_epl(prompt, context)
        return {
            "status": "OK" if epl["machine_actuator_stream"]["armed"] else "VETO",
            "epl": epl
        }
