import streamlit as st
from tools.summarizer import summarize_text
from tools.info_extractor import extract_info
from tools.email_generator import generate_email

st.set_page_config(page_title="Recruiter AI Toolbox", layout="centered")

st.title("🧠 Recruiter AI Toolbox (Groq Powered)")

task = st.sidebar.selectbox("Select Task", ["Summarize Text", "Extract Info", "Generate Email"])

if task == "Summarize Text":
    text = st.text_area("Paste the text to summarize:")
    if st.button("Summarize"):
        summary = summarize_text(text)
        st.subheader("Summary")
        st.write(summary)

elif task == "Extract Info":
    text = st.text_area("Paste the text for information extraction:")
    if st.button("Extract"):
        info = extract_info(text)
        st.subheader("Extracted Information")
        st.write(info)

elif task == "Generate Email":
    email_type = st.selectbox("Email Type", ["Job Application", "Follow-up", "Thank You"])
    context = st.text_area("Enter context for the email:")
    if st.button("Generate Email"):
        email = generate_email(email_type, context)
        st.subheader("Generated Email")
        st.write(email)
