import streamlit as st
from analysis.formatter import run_black_format
from analysis.linter import run_flake8
from analysis.complexity import run_radon_complexity
from utils.file_ops import save_code
from analysis.time_complexity import estimate_time_complexity
from analysis.complexity_chart import estimate_big_o, generate_big_o_curve
import plotly.graph_objs as go



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
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["🔍 Style", "📊 Complexity", "🎨 Formatting", "📥 Export", "⏱️ Time Estimation","📋 Big-O Chart"])

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
    
    with tab5:
        st.subheader("Estimated Time Complexity (AST-based)")
        time_result = estimate_time_complexity(code)
        st.code(time_result, language="text")
    with tab6:
        st.subheader("📋 Big-O Time and Space Complexity Table (Heuristic)")
        table_data = estimate_big_o(code)

        if isinstance(table_data, str):
            st.error(table_data)
        elif not table_data:
            st.info("No functions found.")
        else:
            st.table(table_data)

            # Select a function to graph
            selected_function = st.selectbox("Select a function to plot Big-O curve", [f["Function"] for f in table_data])
            selected_entry = next(f for f in table_data if f["Function"] == selected_function)

            # Get complexity and generate curve
            complexity = selected_entry["Average"]
            n_vals, y_vals = generate_big_o_curve(complexity.split()[0])  # strip extras like + recursion

            fig = go.Figure()
            fig.add_trace(go.Scatter(x=n_vals, y=y_vals, mode="lines", name=complexity))
            fig.update_layout(
                title=f"Theoretical Growth of {complexity} for `{selected_function}`",
                xaxis_title="Input Size (N)",
                yaxis_title="Steps (arbitrary units)",
                template="plotly_dark",
                height=400
            )
            st.plotly_chart(fig)


else:
    st.info("Please upload a Python file or paste some code to begin analysis.")

    
