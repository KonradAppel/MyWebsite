import streamlit as st
from streamlit import session_state as ss
import base64

def display_pdf(pdf_data):
    # Encode PDF as base64
    base64_pdf = base64.b64encode(pdf_data).decode('utf-8')
    pdf_display = f'''
    <style>
        .resizable-container {{
            resize: both;
            overflow: auto;
            border: 1px solid #ccc;
            padding: 10px;
            width: 100%;
            height: 500px;
        }}
        .resizable-container iframe {{
            width: 100%;
            height: 100%;
            border: none;
        }}
    </style>
    <div class="resizable-container">
        <iframe src="data:application/pdf;base64,{base64_pdf}" type="application/pdf"></iframe>
    </div>
    '''
    st.markdown(pdf_display, unsafe_allow_html=True)

def app():
    st.title("CV in English and German")

    # two columns for the language selection and download button
    col1, col2 = st.columns([3, 1], vertical_alignment="bottom")

    # Language selection
    language = col1.selectbox("Select Language", ["English", "Deutsch"], index=0)

    # Display the download button and PDF based on the selected language
    if language == "English":
        with open("data/cv_data/CV_eng.pdf", "rb") as file:
            pdf_data = file.read()
            col2.download_button(
                label="Download CV (English)",
                data=pdf_data,
                file_name="CV_English.pdf",
                mime="application/pdf"
            )
    else:
        with open("data/cv_data/CV_de.pdf", "rb") as file:
            pdf_data = file.read()
            col2.download_button(
                label="Download CV (Deutsch)",
                data=pdf_data,
                file_name="CV_Deutsch.pdf",
                mime="application/pdf"
            )

    # Display the PDF
    display_pdf(pdf_data)

app()