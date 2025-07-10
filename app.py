import streamlit as st
from analysis.formatter import run_black_format
from analysis.linter import run_flake8
from analysis.complexity import run_radon_complexity
from utils.file_ops import save_code

st.set_page_config(page_title="AI Code Reviewer", layout="wide")
st.title("🧠 AI Code Reviewer")

# File uploader and text area
file = st.file_uploader("Upload a Python (.py) file", type=["py"])
text = st.text_area("Or Paste Your Python Code Here")

# Get code from uploaded file or textarea
if file or text.strip():
    code = file.read().decode("utf-8") if file else text

    file_path = save_code(code)

    # Tabs for each analysis section
    tab1, tab2, tab3, tab4 = st.tabs(["🔍 Style (flake8)", "📊 Complexity (radon)", "🎨 Formatting (black)", "📥 Export"])

    with tab1:
        st.subheader("Style Issues (flake8)")
        flake8_result = run_flake8(file_path)
        st.code(flake8_result, language="bash")

    with tab2:
        st.subheader("Code Complexity (radon)")
        complexity_result = run_radon_complexity(code)
        st.code(complexity_result, language="text")

    with tab3:
        st.subheader("Formatted Code (black)")
        formatted_code = run_black_format(code)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Original Code**")
            st.code(code, language="python")
        with col2:
            st.markdown("**Formatted Code**")
            st.code(formatted_code, language="python")

    with tab4:
        st.subheader("Download Full Report")
        report = f"""
STYLE ISSUES (flake8):
-----------------------
{flake8_result}

COMPLEXITY REPORT (radon):
--------------------------
{complexity_result}

FORMATTED CODE (black):
------------------------
{formatted_code}
        """
        st.download_button("📥 Download Report", report, file_name="code_analysis_report.txt")

else:
    st.info("Please upload a Python file or paste some code to begin analysis.")
