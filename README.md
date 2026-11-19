# 📦 AxonGraph EMIL — Official SDK & AI Container Examples

[![AxonGraph DevHub](https://img.shields.io/badge/Docs-AxonGraph%20DevHub-38bdf8?style=for-the-badge)](https://axongraph.ai/devhub.html)
[![AI Container Store](https://img.shields.io/badge/Store-219%2B%20AI%20Containers-34d399?style=for-the-badge)](https://axongraph.ai/container_store.html)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-a78bfa?style=for-the-badge)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/Starter-Zero%20External%20Deps-f59e0b?style=for-the-badge)](#quick-start)

Official, runnable reference templates for building **deterministic, air-gapped `.emp` AI Containers** for the **AxonGraph EMIL** verification & orchestration engine — including **0-code Knowledge & Guardrail containers**, **Hardware/Fieldbus Drivers**, **Symmetric Domain Codecs**, **Closed-Loop Robotics Actuators**, **Interactive EPL 2.0 HTML5 UIs**, and **Auto-Sync / Push Triggers**.

> **IP & Patent Notice:** This repository contains exclusively the public SDK interfaces, declarative container schemas (`vault_manifest.json` v2.0.0, `passport.json`, `smt_rules.json`, EPL 2.0), and runnable developer examples. The internal EMIL cognitive core, geometric kernels, and production root signing keys remain proprietary protected intellectual property of AxonGraph.

---

## ⚡ Quick Start (Runs Out-of-the-Box in 10 Seconds)

No GPU, no Docker, no external Python packages required — pure Python 3.9+:

```bash
# 1. Clone the repository
git clone https://github.com/GuidoHeintz/emil-sdk-examples.git
cd emil-sdk-examples

# 2. Compile all 6 reference templates into `.emp` AI Containers (in dist/)
python build_customer_container_example.py --all

# 3. Launch the interactive EPL 2.0 HTML5 Cockpit UI straight from the compiled `.emp` container!
python build_customer_container_example.py --serve-ui

# 4. Run the Auto-Sync, Push-Webhook & 6-Trigger self-test
python example_container_triggers_and_autosync.py
```

---

## 🧩 The 6 Container Archetypes Included

| # | Folder | Container Class | Code Needed | Use Case |
| :--- | :--- | :--- | :--- | :--- |
| **01** | [`01_knowledge_sop_container/`](./01_knowledge_sop_container/) | `KNOWLEDGE_SOP` | **0 lines** | Factory standard WN-104 high-pressure flange assembly & torque tables. |
| **02** | [`02_guardrail_veto_container/`](./02_guardrail_veto_container/) | `GUARDRAIL_VETO` | **0 lines** | SAP/ERP procurement compliance & 4-eyes FIDO2 Segregation of Duties (> 10,000 EUR). |
| **03** | [`03_device_driver_container/`](./03_device_driver_container/) | `DEVICE_DRIVER` | `vault_runtime.py` | Siemens S7-1500 manufacturing cell (OPC-UA / Modbus HAL) with `HardwareCapabilityGate`. |
| **04** | [`04_perception_codec_container/`](./04_perception_codec_container/) | `PERCEPTION_CODEC` | `vault_runtime.py` | Symmetric `.qdf` metrology codec (`decode` & `encode`, 0 bytes cloud egress). |
| **05** | [`05_actuator_action_container/`](./05_actuator_action_container/) | `ACTUATOR_ACTION` | `vault_runtime.py` | Closed-loop Cobot palletizer with ISO/TS 15066 65 N safety veto (< 1.5 ms). |
| **06** | [`06_interactive_ui_hud_container/`](./06_interactive_ui_hud_container/) | `WORKPLACE_UI_CONTAINER` | `vault_runtime.py` + `ui/` | Interactive HTML5 press-line cockpit ([`ui/cockpit.html`](./06_interactive_ui_hud_container/ui/cockpit.html)) with proof-gated EPL 2.0 buttons (`release_trigger: "on_proof_success"`). |

---

## 🔄 Auto-Sync, Push Notifications & All 6 Container Triggers

See [`example_container_triggers_and_autosync.py`](./example_container_triggers_and_autosync.py) for a complete runnable reference showing:
1. **Cyclic Pull (`DATA_TTL_SECONDS`)** — separated from immutable license TTL (`licensee.valid_until`), guarded by the **100 % Zero-Loss Gate**
2. **External Push (`on_external_push`)** — Webhooks, MQTT, SSE
3. **Local File Drop (`on_file_drop`)** — Air-gapped hot-folder ingestion
4. **Inter-Vault Mesh (`on_mesh_event` / `emit_mesh_event`)** — Signed container-to-container events
5. **System-2 Belnap Escalation (`on_belnap_verdict`)** — Handling `PROVEN`, `DISPROVEN`, `UNDECIDABLE`, `CONTRADICTORY`
6. **Live EPL 2.0 Output (`orchestrate_epl`)** — Real-time cards & proof-gated actuators

---

## 🔐 Production Signing & Partner PKI

Local development builds use a placeholder demo signing key (`build_customer_container_example.py`). For production deployment on an EMIL Appliance, `.emp` containers must be signed via the **2-tier AxonGraph Partner PKI** (`AxonGraph Root CA -> Partner Publisher Certificate -> Container Signature`, NIST FIPS 204 **ML-DSA-65**).

---

## 🔗 Resources
* **Full Developer Documentation & API Reference:** [https://axongraph.ai/devhub.html](https://axongraph.ai/devhub.html)
* **AI Container Store (219+ Certified Modules):** [https://axongraph.ai/container_store.html](https://axongraph.ai/container_store.html)
* **Machine-Readable AI Summary (`llms.txt`):** [https://axongraph.ai/llms.txt](https://axongraph.ai/llms.txt)
