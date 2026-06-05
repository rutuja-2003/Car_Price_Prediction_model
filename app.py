import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(
    page_title="GitHub Repository Dashboard",
    page_icon="💻",
    layout="wide"
)

# ----------------------------
# LOAD DATA
# ----------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/github.csv")

df = load_data()

# ----------------------------
# SIDEBAR TITLE
# ----------------------------
st.sidebar.markdown("## 💻 GitHub Dashboard")

# ----------------------------
# GLOBAL FILTERS
# ----------------------------
st.sidebar.header("🔎 Global Filters")

owner_filter = st.sidebar.multiselect(
    "Select Owner",
    options=df["Owner"].unique(),
    default=df["Owner"].unique()
)

language_filter = st.sidebar.multiselect(
    "Select Language",
    options=df["Language"].unique(),
    default=df["Language"].unique()
)

# Apply filters
df = df[
    (df["Owner"].isin(owner_filter)) &
    (df["Language"].isin(language_filter))
]

# ----------------------------
# PAGE HEADER
# ----------------------------
st.markdown("""
    <h1 style="text-align:center; color:#22d3ee;">
        💻 GitHub Repository – Executive Summary
    </h1>
    <p style="text-align:center; font-size:18px; color:#e0f2fe;">
        A high-level overview of repository performance and activity.
    </p>
""", unsafe_allow_html=True)

st.write("")

# ----------------------------
# KPI CARDS
# ----------------------------
total_repos = len(df)
total_stars = int(df["Stars"].sum())
total_forks = int(df["Forks"].sum())
avg_issues = round(df["Issues"].mean(), 2)

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

kpi1.metric(
    label="📂 Total Repositories",
    value=f"{total_repos:,}"
)

kpi2.metric(
    label="⭐ Total Stars",
    value=f"{total_stars:,}"
)

kpi3.metric(
    label="🍴 Total Forks",
    value=f"{total_forks:,}"
)

kpi4.metric(
    label="🐞 Avg Issues per Repo",
    value=f"{avg_issues}"
)

st.write("---")

# ----------------------------
# LANGUAGE DISTRIBUTION
# ----------------------------
col1, col2 = st.columns([1.2, 1])

with col1:
    lang_df = df["Language"].value_counts().reset_index()
    lang_df.columns = ["Language", "Count"]

    fig = px.pie(
        lang_df,
        names="Language",
        values="Count",
        title="Repository Language Distribution",
        hole=0.45
    )

    fig.update_layout(title_x=0.25)

    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.markdown("""
        ### 📌 Key Insights
        
        • Most repositories are concentrated in a few programming languages.  
        
        • Star and fork counts highlight community engagement.  
        
        • Issue counts indicate maintenance needs and project health.  
        
        • Owners with consistently high stars/forks may represent **popular projects** worth deeper analysis.
    """)

st.write("---")

# ----------------------------
# DATA SUMMARY TABLE
# ----------------------------
summary_df = pd.DataFrame({
    "Metric": [
        "Total Repositories",
        "Total Stars",
        "Total Forks",
        "Average Issues"
    ],
    "Value": [
        total_repos,
        total_stars,
        total_forks,
        avg_issues
    ]
})

st.subheader("📋 Data Summary")

st.dataframe(summary_df, use_container_width=True)
