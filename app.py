import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Page config
st.set_page_config(page_title="Alumni Tracking System", layout="wide")

# Connect DB
engine = create_engine("sqlite:///alumni.db")
df = pd.read_sql("SELECT * FROM alumni", engine)

# Title
st.title("🎓 Alumni Tracking System Dashboard")

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Alumni", len(df))
col2.metric("Average Salary", int(df["salary"].mean()))
col3.metric("Max Salary", int(df["salary"].max()))

st.divider()

# Filters
st.sidebar.header("Filters")

dept = st.sidebar.selectbox("Department", ["All"] + list(df["department"].unique()))
year = st.sidebar.selectbox("Graduation Year", ["All"] + list(df["graduation_year"].unique()))

filtered_df = df.copy()

if dept != "All":
    filtered_df = filtered_df[filtered_df["department"] == dept]

if year != "All":
    filtered_df = filtered_df[filtered_df["graduation_year"] == year]

# Show data
st.subheader("Filtered Alumni Data")
st.dataframe(filtered_df)

# Charts
st.subheader("Salary by Department")
salary_chart = df.groupby("department")["salary"].mean()
st.bar_chart(salary_chart)

st.subheader("Alumni Distribution by Year")
year_chart = df["graduation_year"].value_counts()
st.bar_chart(year_chart)