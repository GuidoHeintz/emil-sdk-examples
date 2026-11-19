"""
Public Authoring Interface (`BaseVaultRuntime`) for `.emp` AI Containers.
Dokumentation: https://axongraph.ai/devhub.html#api-reference
"""
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional


class BaseVaultRuntime(ABC):
    """Abstrakte Basisklasse für aktive `.emp` AI Container (Treiber, Codecs, Aktorik, UI, Auto-Sync)."""

    DATA_TTL_SECONDS: Optional[int] = None
    ON_STALE_POLICY: str = "MARK_STALE"

    def __init__(self, passport_path: Optional[str] = None):
        self.passport_path = passport_path
        self.vault_id: str = "vault.customer.generic"
        self.is_mounted: bool = False
        self.is_stale: bool = False

    def mount(self, context: Optional[Dict[str, Any]] = None):
        self.is_mounted = True

    def unmount(self):
        self.is_mounted = False

    @abstractmethod
    def infer(self, prompt: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        pass

    def get_capabilities(self) -> List[str]:
        return []

    def fetch_external_updates(self, last_cursor: Optional[str] = None) -> Optional[Dict[str, Any]]:
        return None

    def on_external_push(self, channel: str, payload: Dict[str, Any], sender_signature: Optional[str] = None) -> Dict[str, Any]:
        return {"request_core_reingest": False, "push_epl_update": False}

    def on_file_drop(self, file_path: str, event_type: str = "CREATED") -> Dict[str, Any]:
        return {"request_core_reingest": False, "push_epl_update": False}

    def on_mesh_event(self, source_vault_id: str, event_type: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        return {"trigger_revalidation": False, "push_epl_update": False}

    def emit_mesh_event(self, event_type: str, payload: Dict[str, Any], target_vault_id: str = "*"):
        return {"emitted": True, "event_type": event_type, "target": target_vault_id, "payload": payload}

    def on_belnap_verdict(self, verdict: str, unsat_core: List[str], missing_variables: List[str]) -> Dict[str, Any]:
        return {"push_epl_update": verdict in ("CONTRADICTORY", "UNDECIDABLE")}

    def on_stale_detected(self, reason: str):
        self.is_stale = True

    def orchestrate_epl(self, prompt: str = "", context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        return {
            "epl_version": "2.0",
            "vault_id": self.vault_id,
            "layout": {"type": "card", "title": self.vault_id, "badge": {"text": "✓ BEREIT", "type": "SUCCESS"}},
            "actuators": [],
        }
