import streamlit as st
import pandas as pd
from backend.analysis import load_data, run_analysis

st.title("InsightForge – AI-Powered BI")
st.markdown("**Author: Jon Hembree**")

uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])
if uploaded_file:
    df = load_data(uploaded_file)
    st.subheader("Data Preview")
    st.dataframe(df.head())

    st.subheader("Analysis Summary")
    summary = run_analysis(df)
    st.dataframe(summary)
