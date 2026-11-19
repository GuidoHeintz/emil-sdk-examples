"""
Symmetrischer Kunden-Codec (vault_runtime.py) für proprietäre .qdf Qualitätsprotokolle.
"""
from typing import Dict, Any, Optional, List


class CustomerQdfCodecRuntime:
    FORMAT_ID = "quality.customer.qdf.v2"

    def __init__(self, passport_path: Optional[str] = None):
        self.passport_path = passport_path
        self.vault_id = "vault.customer.codec.qdf_quality_protocol"
        self.is_mounted = False

    def mount(self, context: Optional[Dict[str, Any]] = None):
        self.is_mounted = True

    def unmount(self):
        self.is_mounted = False

    def get_capabilities(self) -> List[str]:
        return ["codec_decode_qdf_v2", "codec_encode_qdf_v2"]

    @staticmethod
    def decode_qdf_line(raw_line: str) -> Dict[str, Any]:
        fields = {}
        for token in raw_line.strip().split("|"):
            if "=" in token:
                k, v = token.split("=", 1)
                fields[k.strip()] = v.strip()
        nominal = float(fields.get("NOMINAL_MM", 0.0))
        actual = float(fields.get("ACTUAL_MM", 0.0))
        tol = float(fields.get("TOL_MM", 0.0))
        dev = round(actual - nominal, 6)
        return {
            "part_id": fields.get("PART_ID", "UNKNOWN"),
            "feature": fields.get("FEATURE", "UNKNOWN"),
            "nominal_mm": nominal,
            "actual_mm": actual,
            "tolerance_mm": tol,
            "deviation_mm": dev,
            "status": "OK" if abs(dev) <= tol else "VETO_OUT_OF_TOLERANCE",
        }

    @staticmethod
    def encode_qdf_line(record: Dict[str, Any]) -> str:
        return (
            f"PART_ID={record['part_id']}|FEATURE={record['feature']}|"
            f"NOMINAL_MM={record['nominal_mm']:.3f}|ACTUAL_MM={record['actual_mm']:.3f}|"
            f"TOL_MM={record['tolerance_mm']:.3f}"
        )

    def infer(self, prompt: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        sample = (context or {}).get(
            "raw_qdf",
            "PART_ID=B-9920|FEATURE=BOHRUNG_D42|NOMINAL_MM=42.000|ACTUAL_MM=42.008|TOL_MM=0.015",
        )
        decoded = self.decode_qdf_line(sample)
        reencoded = self.encode_qdf_line(decoded)
        return {"status": decoded["status"], "decoded": decoded, "reencoded_qdf": reencoded}
