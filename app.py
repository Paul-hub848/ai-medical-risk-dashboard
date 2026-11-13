import streamlit as st
import pandas as pd

# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="AI Medical Device Cybersecurity Toolkit",
    page_icon="🏥",
    layout="wide"
)

# ---------------------------------------------------------
# DATA: RISKS (R1-R10) & MITIGATIONS FROM YOUR PROPOSAL
# ---------------------------------------------------------
RISKS_DATA = [
    {
        "Risk ID": "R1",
        "Risk Name": "Patient Data Breach",
        "Category": "Data Confidentiality",
        "Default Likelihood": 5,
        "Default Impact": 5,
        "Control Questions": ["q_enc", "q_dlp"],
        "Mitigation Strategy": "Strategy 1: Patient Data Protection",
        "Controls": "AES-256 Encryption, Secure Cloud Storage, Data Loss Prevention (DLP), Data Classification",
        "Regulatory Alignment": "FDA Section 524B / HIPAA / NHS DSPT"
    },
    {
        "Risk ID": "R2",
        "Risk Name": "Ransomware on Device Network",
        "Category": "Service Availability",
        "Default Likelihood": 4,
        "Default Impact": 5,
        "Control Questions": ["q_seg", "q_ir"],
        "Mitigation Strategy": "Strategy 4 & 6: Network Security & Incident Response",
        "Controls": "Network Segmentation, Zero Trust Architecture, Firewalls, Offline Backups, Playbooks",
        "Regulatory Alignment": "NIST CSF / NHS Cyber Security Guidance"
    },
    {
        "Risk ID": "R3",
        "Risk Name": "Adversarial AI Attack (Evasion)",
        "Category": "AI Model Integrity",
        "Default Likelihood": 3,
        "Default Impact": 5,
        "Control Questions": ["q_ai_input", "q_ai_out"],
        "Mitigation Strategy": "Strategy 3: AI Model Security",
        "Controls": "Input Validation, Anomaly Detection, AI Output Verification, Human-in-the-Loop",
        "Regulatory Alignment": "FDA AI-Enabled Device Guidance / NIST AI RMF"
    },
    {
        "Risk ID": "R4",
        "Risk Name": "Software Update Compromise",
        "Category": "Supply Chain",
        "Default Likelihood": 3,
        "Default Impact": 5,
        "Control Questions": ["q_patch", "q_sbom"],
        "Mitigation Strategy": "Strategy 5: Device Security",
        "Controls": "Cryptographically Signed Updates, SBOM Verification, Vulnerability Scanning",
        "Regulatory Alignment": "FDA Premarket Guidance (SBOM) / ENISA"
    },
    {
        "Risk ID": "R5",
        "Risk Name": "Insider Threat",
        "Category": "Access & Governance",
        "Default Likelihood": 3,
        "Default Impact": 3,
        "Control Questions": ["q_rbac", "q_pam"],
        "Mitigation Strategy": "Strategy 2: Access Control",
        "Controls": "Role-Based Access Control (RBAC), Privileged Access Management (PAM), Audit Logging",
        "Regulatory Alignment": "NIST SP 800-53 / ISO 27001"
    },
    {
        "Risk ID": "R6",
        "Risk Name": "Poor Access Controls",
        "Category": "Access & Governance",
        "Default Likelihood": 4,
        "Default Impact": 4,
        "Control Questions": ["q_mfa", "q_rbac"],
        "Mitigation Strategy": "Strategy 2: Access Control",
        "Controls": "Multi-Factor Authentication (MFA), Least Privilege Access, Strong Device Identity",
        "Regulatory Alignment": "FDA Cyber Device Controls / NIST Zero Trust"
    },
    {
        "Risk ID": "R7",
        "Risk Name": "Cloud Service Compromise",
        "Category": "Infrastructure",
        "Default Likelihood": 3,
        "Default Impact": 5,
        "Control Questions": ["q_enc", "q_seg"],
        "Mitigation Strategy": "Strategy 1 & 4: Data & Network Security",
        "Controls": "End-to-End TLS/AES-256 Encryption, Zero Trust API Gateways, Cloud Posture Management",
        "Regulatory Alignment": "ENISA Cloud Security / NIST AI RMF"
    },
    {
        "Risk ID": "R8",
        "Risk Name": "Device Misconfiguration",
        "Category": "Device Hardening",
        "Default Likelihood": 3,
        "Default Impact": 3,
        "Control Questions": ["q_base", "q_patch"],
        "Mitigation Strategy": "Strategy 5: Device Security",
        "Controls": "Secure Configuration Baselines, Hardened OS Images, Endpoint Detection & Response (EDR)",
        "Regulatory Alignment": "FDA Quality Management System (QMSR)"
    },
    {
        "Risk ID": "R9",
        "Risk Name": "AI Model Manipulation / Poisoning",
        "Category": "AI Pipeline Integrity",
        "Default Likelihood": 3,
        "Default Impact": 5,
        "Control Questions": ["q_ai_data", "q_ai_input"],
        "Mitigation Strategy": "Strategy 3: AI Model Security",
        "Controls": "Dataset Validation, Model Integrity Monitoring, Cryptographic Model Hashing",
        "Regulatory Alignment": "FDA AI Lifecycle Guidance / OWASP AI Top 10"
    },
    {
        "Risk ID": "R10",
        "Risk Name": "Denial of Service (DoS) Attack",
        "Category": "Service Availability",
        "Default Likelihood": 3,
        "Default Impact": 4,
        "Control Questions": ["q_seg", "q_ir"],
        "Mitigation Strategy": "Strategy 4 & 6: Network & Incident Response",
        "Controls": "Intrusion Detection/Prevention Systems (IDS/IPS), Rate Limiting, Fail-Safe Manual Mode",
        "Regulatory Alignment": "FDA Patient Safety & Availability Guidance"
    }
]

# Preset Device Profiles for Quick Live Demos
PRESETS = {
    "Custom Assessment (Manual)": None,
    "Scenario A: Unsecured Cloud-Connected AI Radiology System": {
        "name": "NeuroScan AI Radiology v2.1",
        "type": "AI-Powered Radiology / Diagnostic Imaging",
        "connectivity": "Cloud-Connected + Hospital PACS/LAN",
        "controls": {
            "q_enc": False, "q_dlp": False, "q_mfa": False, "q_rbac": True, "q_pam": False,
            "q_ai_data": False, "q_ai_input": False, "q_ai_out": True,
            "q_seg": False, "q_patch": False, "q_base": True, "q_sbom": False, "q_ir": False
        }
    },
    "Scenario B: Hardened AI ICU Patient Monitoring System": {
        "name": "CardioGuard AI Vitals Monitor",
        "type": "AI Patient Monitoring System",
        "connectivity": "Segmented Hospital VLAN Only",
        "controls": {
            "q_enc": True, "q_dlp": True, "q_mfa": True, "q_rbac": True, "q_pam": True,
            "q_ai_data": True, "q_ai_input": True, "q_ai_out": True,
            "q_seg": True, "q_patch": True, "q_base": True, "q_sbom": True, "q_ir": True
        }
    }
}

def get_rating(score):
    if score >= 17:
        return "Critical"
    elif score >= 10:
        return "High"
    elif score >= 5:
        return "Medium"
    else:
        return "Low"

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------
st.title("🏥 AI-Powered Medical Device Cybersecurity Risk Assessment Toolkit")
st.markdown(
    "**Research Artefact:** Decision-support framework for evaluating patient safety, data confidentiality, "
    "and AI integrity risks prior to clinical deployment."
)
st.divider()

# ---------------------------------------------------------
# SIDEBAR: DEVICE PROFILE & CONTROL QUESTIONNAIRE
# ---------------------------------------------------------
with st.sidebar:
    st.header("1. Device Profile & Demo Presets")
    selected_preset = st.selectbox("Load Demo Scenario:", list(PRESETS.keys()))
    preset_data = PRESETS[selected_preset]

    device_name = st.text_input(
        "Medical Device Name",
        value=preset_data["name"] if preset_data else "AI Diagnostic Workstation"
    )
    device_type = st.selectbox(
        "Clinical Category",
        [
            "AI-Powered Radiology / Diagnostic Imaging",
            "AI Patient Monitoring System",
            "Clinical Decision Support System (CDSS)",
            "Connected Infusion / Therapeutic Device"
        ],
        index=0 if not preset_data else 0
    )
    connectivity = st.selectbox(
        "Network Architecture",
        [
            "Cloud-Connected + Hospital PACS/LAN",
            "Segmented Hospital VLAN Only",
            "Standalone / Air-Gapped"
        ],
        index=0 if not preset_data else (1 if "VLAN" in preset_data["connectivity"] else 0)
    )

    st.divider()
    st.header("2. Existing Security Controls")
    st.caption("Check all controls currently verified for this device:")

    def default_val(key):
        return preset_data["controls"][key] if preset_data else False

    with st.expander("🔐 Strategy 1 & 2: Data & Access Control", expanded=True):
        q_enc = st.checkbox("AES-256 / TLS Encryption at rest & transit", value=default_val("q_enc"))
        q_dlp = st.checkbox("Data Loss Prevention (DLP) & Classification", value=default_val("q_dlp"))
        q_mfa = st.checkbox("Multi-Factor Authentication (MFA)", value=default_val("q_mfa"))
        q_rbac = st.checkbox("Role-Based Access Control (RBAC)", value=default_val("q_rbac"))
        q_pam = st.checkbox("Privileged Access Management (PAM)", value=default_val("q_pam"))

    with st.expander("🧠 Strategy 3: AI Model Security", expanded=True):
        q_ai_data = st.checkbox("Training Dataset Validation & Provenance", value=default_val("q_ai_data"))
        q_ai_input = st.checkbox("Adversarial Input Validation / Filtering", value=default_val("q_ai_input"))
        q_ai_out = st.checkbox("AI Output Verification / Clinician Override", value=default_val("q_ai_out"))

    with st.expander("🛡️ Strategy 4, 5 & 6: Network, Device & IR", expanded=True):
        q_seg = st.checkbox("Network Segmentation / Zero Trust VLAN", value=default_val("q_seg"))
        q_patch = st.checkbox("Signed Software Updates & Patching", value=default_val("q_patch"))
        q_base = st.checkbox("Hardened Configuration Baselines & EDR", value=default_val("q_base"))
        q_sbom = st.checkbox("Verified SBOM (Software Bill of Materials)", value=default_val("q_sbom"))
        q_ir = st.checkbox("Tested Incident Response & Offline Backups", value=default_val("q_ir"))

controls_state = {
    "q_enc": q_enc, "q_dlp": q_dlp, "q_mfa": q_mfa, "q_rbac": q_rbac, "q_pam": q_pam,
    "q_ai_data": q_ai_data, "q_ai_input": q_ai_input, "q_ai_out": q_ai_out,
    "q_seg": q_seg, "q_patch": q_patch, "q_base": q_base, "q_sbom": q_sbom, "q_ir": q_ir
}

# ---------------------------------------------------------
# RISK CALCULATION ENGINE (Likelihood x Impact)
# ---------------------------------------------------------
results = []
for r in RISKS_DATA:
    inherent_l = r["Default Likelihood"]
    impact = r["Default Impact"]

    if connectivity == "Standalone / Air-Gapped" and r["Risk ID"] in ["R2", "R7", "R10"]:
        inherent_l = max(1, inherent_l - 2)

    active_controls = sum(1 for q in r["Control Questions"] if controls_state[q])
    residual_l = max(1, inherent_l - active_controls)

    inherent_score = inherent_l * impact
    residual_score = residual_l * impact
    rating = get_rating(residual_score)

    results.append({
        "Risk ID": r["Risk ID"],
        "Risk Name": r["Risk Name"],
        "Category": r["Category"],
        "Inherent Score": inherent_score,
        "Residual Likelihood": residual_l,
        "Impact": impact,
        "Residual Score": residual_score,
        "Risk Rating": rating,
        "Mitigation Strategy": r["Mitigation Strategy"],
        "Recommended Controls": r["Controls"],
        "Regulatory Alignment": r["Regulatory Alignment"]
    })

df = pd.DataFrame(results)

# ---------------------------------------------------------
# TOP KPI METRICS
# ---------------------------------------------------------
critical_count = len(df[df["Risk Rating"] == "Critical"])
high_count = len(df[df["Risk Rating"] == "High"])
avg_residual = round(df["Residual Score"].mean(), 1)
avg_inherent = round(df["Inherent Score"].mean(), 1)
risk_reduction = round(((avg_inherent - avg_residual) / avg_inherent) * 100, 1)

st.subheader(f"📊 Assessment Overview: {device_name}")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Critical Risks", critical_count)
col2.metric("High Risks", high_count)
col3.metric("Mean Residual Score", f"{avg_residual} / 25")
col4.metric("Risk Reduction", f"{risk_reduction}%")

st.divider()

# ---------------------------------------------------------
# TABS: RISK REGISTER & REMEDIATION PLAN
# ---------------------------------------------------------
tab1, tab2 = st.tabs([
    "📋 Risk Assessment Matrix & Register",
    "🛠️ Prioritized Mitigation Roadmap"
])

with tab1:
    st.markdown("#### Complete AI Medical Device Risk Register")
    st.dataframe(df[["Risk ID", "Risk Name", "Category", "Inherent Score", "Residual Score", "Risk Rating"]], use_container_width=True, hide_index=True)

    csv_data = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Export Full Risk Assessment Report (CSV)",
        data=csv_data,
        file_name=f"{device_name.replace(' ', '_')}_Risk_Assessment.csv",
        mime="text/csv"
    )

with tab2:
    st.markdown("#### Actionable Remediation Plan")
    priority_df = df.sort_values(by="Residual Score", ascending=False)

    for _, row in priority_df.iterrows():
        badge = "🔴 CRITICAL" if row["Risk Rating"] == "Critical" else ("🟠 HIGH" if row["Risk Rating"] == "High" else "🟡/🟢")
        with st.expander(f"{badge} | {row['Risk ID']}: {row['Risk Name']} (Score: {row['Residual Score']}/25)"):
            st.write(f"**Mapped Mitigation:** {row['Mitigation Strategy']}")
            st.write(f"**Required Technical Controls:** {row['Recommended Controls']}")
            st.caption(f"**Regulatory Alignment:** {row['Regulatory Alignment']}")
