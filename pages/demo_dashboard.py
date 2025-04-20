# pages/projects/demo_dashboard.py

import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="Lake's Demo Dashboard", layout="wide")

st.title("Lake's Demo Dashboard")
st.markdown("This is a simple interactive dashboard using CSV data.")

# 1️⃣ Upload CSV
uploaded_file = st.file_uploader("Upload your CSV", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # 2️⃣ Sidebar: Column Type Inspector
    with st.sidebar:
        st.header("🔧 Adjust Column Types")
        converted_types = {}

        with st.form("column_type_form"):
            for col in df.columns:
                inferred = str(df[col].dtype)
                option = st.selectbox(
                    f"{col} (Inferred: {inferred})",
                    options=["Auto", "Date", "Number", "Text", "Category"],
                    key=f"type_{col}"
                )
                converted_types[col] = option
            submit = st.form_submit_button("Apply Conversions")

    if submit:
        for col, dtype in converted_types.items():
            try:
                if dtype == "Date":
                    df[col] = pd.to_datetime(df[col], errors='coerce')
                elif dtype == "Number":
                    df[col] = pd.to_numeric(df[col], errors="coerce")
                elif dtype == "Category":
                    df[col] = df[col].astype("category")
                elif dtype == "Text":
                    df[col] = df[col].astype(str)
                # "Auto" = do nothing
            except Exception as e:
                st.warning(f"⚠️ Could not convert {col} to {dtype}: {e}")

        st.success("✅ Column types updated!")

    # 3️⃣ Main Area: DataFrame + Chart
    st.subheader("🔍 Data Preview")
    st.dataframe(df)

    st.subheader("📊 Simple Line Chart Example")
    # Choose x and y from dropdowns
    col1, col2 = st.columns(2)
    with col1:
        x_axis = st.selectbox("Select X-axis", df.columns)
    with col2:
        y_axis = st.selectbox("Select Y-axis", df.columns)

    try:
        chart = alt.Chart(df).mark_line(point=True).encode(
            x=alt.X(x_axis, title=x_axis),
            y=alt.Y(y_axis, title=y_axis),
            tooltip=[x_axis, y_axis]
        ).interactive()

        st.altair_chart(chart, use_container_width=True)
    except Exception as e:
        st.error(f"Could not create chart: {e}")
else:
    st.info("📤 Upload a CSV file to get started.")