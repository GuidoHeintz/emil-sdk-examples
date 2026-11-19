"""
Closed-Loop Kunden-Aktorik-Controller (vault_runtime.py) nach ISO/TS 15066.
"""
from typing import Dict, Any, Optional, List


class CustomerCobotPalletizerRuntime:
    MAX_FORCE_N = 65.0
    MIN_DISTANCE_MM = 150.0

    def __init__(self, passport_path: Optional[str] = None):
        self.passport_path = passport_path
        self.vault_id = "vault.customer.actuator.cobot_safe_palletizer"
        self.is_mounted = False

    def mount(self, context: Optional[Dict[str, Any]] = None):
        self.is_mounted = True

    def unmount(self):
        self.is_mounted = False

    def get_capabilities(self) -> List[str]:
        return ["actuator_cobot_palletize_motion", "safety_reflex_brake_trigger"]

    def infer(self, prompt: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        telemetry = context or {}
        force_n = float(telemetry.get("contact_force_n", 18.5))
        dist_mm = float(telemetry.get("human_distance_mm", 420.0))

        if dist_mm < self.MIN_DISTANCE_MM:
            return {
                "status": "VETO",
                "rule_id": "INV-SAFETY-CURTAIN",
                "action": "hardware.ep_lock",
                "reason": f"Schutzabstand unterschritten ({dist_mm} mm < {self.MIN_DISTANCE_MM} mm).",
                "actuator_command": {"emergency_brake": True, "target_velocity": [0.0, 0.0, 0.0]},
            }
        if force_n > self.MAX_FORCE_N:
            return {
                "status": "VETO",
                "rule_id": "INV-ISO15066-FORCE",
                "action": "hardware.safe_torque_off",
                "reason": f"Kontaktkraft überschritten ({force_n} N > {self.MAX_FORCE_N} N).",
                "actuator_command": {"emergency_brake": True, "max_torque_nm": 0.0},
            }
        return {
            "status": "OK",
            "action": "actuator.move_trajectory",
            "actuator_command": {"target_pose_xyz": [0.45, -0.20, 0.32], "grip_force_n": min(force_n, 25.0)},
        }
