import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure GenerativeAI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get Gemini response


def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    response = model.generate_content(input)
    return response.text

# Function to extract text from PDF


def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text


# Prompt Template
input_prompt = """
Hey, I'm applying for the position of {job_role}.
Here's a brief description of the job:
{description}

Can you evaluate my CV based on this role and provide feedback?
"""

# Streamlit app title and description
st.title("Smart ATS")
st.markdown("Improve Your Resume with AI")

# Job application form
st.sidebar.header("Job Application")
job_role = st.sidebar.text_input("Job Role You're Applying For")
description = st.sidebar.text_area("Job Description")
uploaded_file = st.sidebar.file_uploader(
    "Upload Your Resume (PDF)", type="pdf", help="Please upload your CV in PDF format")

# Submit button
submit = st.sidebar.button("Submit")

# Display result
if submit:
    if job_role and description and uploaded_file:
        # Read uploaded PDF file
        reader = pdf.PdfReader(uploaded_file)
        text = ""
        for page in range(len(reader.pages)):
            page = reader.pages[page]
            text += str(page.extract_text())

        # Check if the uploaded document is a CV based on CV format
        cv_keywords = ["education", "experience", "skills", "summary"]
        is_cv = all(keyword in text.lower() for keyword in cv_keywords)

        if is_cv:
            st.success("CV successfully uploaded and validated.")
            response = get_gemini_response(input_prompt.format(
                job_role=job_role, description=description))
            st.subheader(response)
        else:
            st.error(
                "The uploaded document does not appear to be a CV. Please upload a valid CV.")
    else:
        st.error("Please fill in all the required fields.")
