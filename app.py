import streamlit as st

st.set_page_config(page_title="AI Medical Device Risk Dashboard", layout="wide")

st.title("AI Medical Device Cybersecurity & Risk Assessment Dashboard")
st.subheader("Aligned with NIST AI RMF & FDA Premarket Cybersecurity Guidance")

st.write("Welcome! Use the inputs below to evaluate the security posture of an AI-enabled Medical Device (SaMD).")
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="AI Medical Device Risk Dashboard",
    page_icon="🛡️",
    layout="wide"
)

# App Header
st.title("🛡️ AI Medical Device Cybersecurity & Risk Assessment Dashboard")
st.markdown("### Designed for Software as a Medical Device (SaMD) Compliance")
st.markdown("---")

# Sidebar for System Configuration
st.sidebar.header("📋 Device Profile Setup")
device_name = st.sidebar.text_input("AI Device Name", "CardioAI Diagnostic Assistant")
deployment_type = st.sidebar.selectbox("Deployment Environment", ["Cloud Server", "Local Hospital Server", "Embedded Medical Hardware"])
data_type = st.sidebar.selectbox("Inpusted Data Type", ["Medical Imaging (DICOM)", "Electronic Health Records (EHR)", "Patient Vital Sensor Feeds"])

st.sidebar.markdown("---")
st.sidebar.info("Frameworks Aligned: **NIST AI RMF 1.0** & **FDA Premarket Cybersecurity Guidance**")

# Main Dashboard Layout
tab1, tab2, tab3 = st.tabs(["🔍 1. Threat Identification", "📊 2. Risk Scoring Matrix", "📋 3. NIST/FDA Mitigation Report"])

with tab1:
    st.subheader("AI-Specific Threat Modeling")
    st.write("Select the potential security threats applicable to your AI Medical Device:")
    
    t1 = st.checkbox("Data Poisoning (Tampering with training/input datasets)")
    t2 = st.checkbox("Adversarial Input Manipulation (Altering medical scans to fool AI)")
    t3 = st.checkbox("Model Extraction / Intellectual Property Theft")
    t4.checkbox = st.checkbox("Unauthorized Access & Patient Data Breach (Confidentiality risk)")

    if st.button("Save Threat Profile"):
        st.success("Threat profile updated successfully!")

with tab2:
    st.subheader("Qualitative Risk Assessment (Likelihood x Impact)")
    
    likelihood = st.slider("Select Threat Likelihood (1 = Rare, 5 = Frequent)", 1, 5, 3)
    impact = st.slider("Select Potential Patient / System Impact (1 = Low, 5 = Critical)", 1, 5, 4)
    
    risk_score = likelihood * impact
    
    st.metric(label="Calculated Risk Score", value=risk_score)
    
    if risk_score >= 15:
        st.error("🚨 **Risk Level: CRITICAL** - Immediate mitigation controls required before clinical deployment.")
    elif risk_score >= 8:
        st.warning("⚠️ **Risk Level: MODERATE** - Enhanced monitoring and security safeguards needed.")
    else:
        st.info("✅ **Risk Level: LOW** - Standard controls sufficient.")

with tab3:
    st.subheader("Compliance & Mitigation Recommendations")
    st.write("Based on your selections, here are the required regulatory actions:")
    
    st.markdown("""
    * **Govern & Map (NIST AI RMF):** Establish clear accountability lines for model updates and monitor data drift.
    * **FDA Premarket Requirements:** Maintain an up-to-date **Software Bill of Materials (SBOM)** tracking all open-source libraries.
    * **Vulnerability Management Plan:** Implement patch management procedures and secure communication protocols (TLS 1.3 encryption).
    """)
    
    if st.button("Generate Downloadable Summary Report"):
        st.balloons()
        st.success("Report generated successfully! (Ready to include in your 601IT Technical Report)")
