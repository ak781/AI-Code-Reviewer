import streamlit as st
import tempfile

st.set_page_config(page_title="AI Code Reviewer",layout="wide")
st.title("AI Code Reviewer")

file=st.file_uploader(label="Upload a Python (.py) File ",type=['py'])
text=st.text_area("Or Paste Your Code Here")

# Saving code to a temp file

def save_code(code):
    temp_file=tempfile.NamedTemporaryFile(mode="w",delete=False,suffix='.py')
    temp_file.write(code)
    temp_file.close()
    return temp_file.name