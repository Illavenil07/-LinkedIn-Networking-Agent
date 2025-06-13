import streamlit as st
from agent import generate_message

st.title("LinkedIn Networking Message Generator")

target_name = st.text_input("Target's Name")
target_role = st.text_input("Target's Role")
company_name = st.text_input("Company Name")
topic = st.text_input("Mutual Interest / Topic")

if st.button("Generate Message"):
    if target_name and target_role and company_name and topic:
        message = generate_message(target_name, target_role, company_name, topic)
        st.success(message)
    else:
        st.warning("Please fill in all fields.")
