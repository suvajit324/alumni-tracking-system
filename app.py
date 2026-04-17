import streamlit as st
import pandas as pd


# Page config
st.set_page_config(page_title="Alumni Tracking System", layout="wide")

# ===== LOAD DATA (BULLETPROOF PATH) =====

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "data", "raw", "alumni.csv")
df = pd.read_csv("alumni.csv")  

# ===== TITLE =====
st.title("🎓 Alumni Tracking System Dashboard")

# ===== METRICS =====
col1, col2, col3 = st.columns(3)
col1.metric("👨‍🎓 Total Alumni", len(df))
col2.metric("💰 Avg Salary", f"₹{int(df['salary'].mean())}")
col3.metric("🚀 Highest Salary", f"₹{int(df['salary'].max())}")

st.divider()

# ===== SIDEBAR FILTERS =====
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

# ===== APPLY FILTERS =====
filtered_df = df.copy()

if dept != "All":
    filtered_df = filtered_df[filtered_df["department"] == dept]

if year != "All":
    filtered_df = filtered_df[filtered_df["graduation_year"] == year]

filtered_df = filtered_df[
    (filtered_df["salary"] >= salary_range[0]) &
    (filtered_df["salary"] <= salary_range[1])
]

# ===== DISPLAY DATA =====
st.subheader("📋 Filtered Alumni Data")
st.dataframe(filtered_df, use_container_width=True)

# ===== CHARTS =====
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Average Salary by Department")
    salary_chart = df.groupby("department")["salary"].mean()
    st.bar_chart(salary_chart)

with col2:
    st.subheader("📈 Alumni Distribution by Year")
    year_chart = df["graduation_year"].value_counts()
    st.bar_chart(year_chart)

# ===== SEARCH =====
st.subheader("🔎 Search Alumni by Name")

search = st.text_input("Enter name")

if search:
    result = df[df["name"].str.contains(search, case=False)]
    st.write(result)

# ===== DOWNLOAD =====
st.subheader("⬇ Download Data")

csv = df.to_csv(index=False).encode("utf-8")
st.download_button("Download CSV", csv, "alumni_data.csv", "text/csv")

# ===== FOOTER =====
st.markdown("---")
st.markdown("<center>Made with ❤️ using Streamlit</center>", unsafe_allow_html=True)
