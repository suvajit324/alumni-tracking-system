import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="Alumni Tracking System", layout="wide")

# Load data from CSV (IMPORTANT CHANGE)
df = pd.read_csv("data/processed/alumni_cleaned.csv")

# Title
st.title("🎓 Alumni Tracking System Dashboard")

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Alumni", len(df))
col2.metric("Average Salary", int(df["salary"].mean()))
col3.metric("Max Salary", int(df["salary"].max()))

st.divider()

# Sidebar Filters
st.sidebar.header("🔍 Filters")

dept = st.sidebar.selectbox(
    "Department", ["All"] + sorted(df["department"].unique())
)

year = st.sidebar.selectbox(
    "Graduation Year", ["All"] + sorted(df["graduation_year"].unique())
)

salary_range = st.sidebar.slider(
    "Salary Range",
    int(df["salary"].min()),
    int(df["salary"].max()),
    (int(df["salary"].min()), int(df["salary"].max()))
)

# Apply filters
filtered_df = df.copy()

if dept != "All":
    filtered_df = filtered_df[filtered_df["department"] == dept]

if year != "All":
    filtered_df = filtered_df[filtered_df["graduation_year"] == year]

filtered_df = filtered_df[
    (filtered_df["salary"] >= salary_range[0]) &
    (filtered_df["salary"] <= salary_range[1])
]

# Show data
st.subheader("📋 Filtered Alumni Data")
st.dataframe(filtered_df, use_container_width=True)

# Charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Average Salary by Department")
    salary_chart = df.groupby("department")["salary"].mean()
    st.bar_chart(salary_chart)

with col2:
    st.subheader("📈 Alumni Distribution by Year")
    year_chart = df["graduation_year"].value_counts()
    st.bar_chart(year_chart)

# Search feature
st.subheader("🔎 Search Alumni by Name")
search = st.text_input("Enter name")

if search:
    result = df[df["name"].str.contains(search, case=False)]
    st.write(result)

# Download button
st.subheader("⬇ Download Data")
csv = df.to_csv(index=False).encode('utf-8')
st.download_button("Download CSV", csv, "alumni_data.csv", "text/csv")

# Footer
st.markdown("---")
st.markdown("<center>Made with ❤️ using Streamlit</center>", unsafe_allow_html=True)
