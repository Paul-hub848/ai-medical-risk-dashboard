import streamlit as st
import scanner
import sbom_generator
import pandas as pd
import json

st.title("AI Medical Device Cybersecurity & SBOM Dashboard")

tab1, tab2 = st.tabs(["Static Code Scanner", "SBOM (Software Bill of Materials)"])

with tab1:
    st.header("Python Source Code Security Scan")
    uploaded_file = st.file_uploader("Upload Python Code File (.py)", type=["py"], key="code_uploader")

    if uploaded_file is not None:
        code_content = uploaded_file.read().decode("utf-8")
        st.subheader("Scan Results")
        
        vulnerabilities = scanner.run_scan(code_content)
        
        if vulnerabilities:
            st.warning(f"Found {len(vulnerabilities)} potential security vulnerabilities!")
            for vuln in vulnerabilities:
                st.error(f"Line {vuln['line']} [{vuln['severity']}]: {vuln['type']} — {vuln['description']}")
        else:
            st.success("No security vulnerabilities detected in this file!")

with tab2:
    st.header("Software Bill of Materials (SBOM) Generator")
    req_file = st.file_uploader("Upload requirements.txt file", type=["txt"], key="sbom_uploader")

    if req_file is not None:
        req_content = req_file.read().decode("utf-8")
        st.subheader("Generated SBOM Inventory")
        
        sbom_data = sbom_generator.parse_requirements(req_content)
        
        if sbom_data:
            df = pd.DataFrame(sbom_data)
            st.dataframe(df, use_container_width=True)
            
            json_sbom = json.dumps(sbom_data, indent=4)
            st.download_button(
                label="📥 Download SBOM Report (JSON)",
                data=json_sbom,
                file_name="medical_ai_sbom_report.json",
                mime="application/json"
            )
        else:
            st.info("The uploaded requirements file is empty.")