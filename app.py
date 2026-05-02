import streamlit as st
from analysis import load_data, clean_data, get_country_data, get_summary_stats
from visualizations import (plot_cases_over_time, plot_deaths_over_time, 
                             plot_top_countries, plot_death_rate)

# Page config
st.set_page_config(
    page_title="COVID-19 Dashboard",
    page_icon="🦠",
    layout="wide"
)

# Title
st.title("🦠 COVID-19 Global Data Analysis Dashboard")
st.markdown("Analyzing global COVID-19 trends using real-world data")

# Load and clean data
@st.cache_data
def get_data():
    df = load_data()
    return clean_data(df)

df = get_data()

# Sidebar
st.sidebar.header("Filters")
countries = sorted(df['location'].unique().tolist())
selected_country = st.sidebar.selectbox("Select Country", countries, 
                                         index=countries.index("India"))
compare_countries = st.sidebar.multiselect(
    "Compare Countries (Death Rate)",
    countries,
    default=["India", "United States", "Brazil", "United Kingdom"]
)

# Summary stats
st.subheader(f"📊 Summary — {selected_country}")
stats = get_summary_stats(df, selected_country)
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Cases", f"{stats['Total Cases']:,}")
col2.metric("Total Deaths", f"{stats['Total Deaths']:,}")
col3.metric("Peak Daily Cases", f"{stats['Peak New Cases']:,}")
col4.metric("Death Rate", f"{stats['Death Rate (%)']}%")

# Charts
st.subheader("📈 Cases Over Time")
country_df = get_country_data(df, selected_country)
st.plotly_chart(plot_cases_over_time(country_df, selected_country), 
                use_container_width=True)

col_a, col_b = st.columns(2)
with col_a:
    st.subheader("💀 Deaths Over Time")
    st.plotly_chart(plot_deaths_over_time(country_df, selected_country), 
                    use_container_width=True)

with col_b:
    st.subheader("🌍 Top 10 Countries")
    st.plotly_chart(plot_top_countries(df), use_container_width=True)

st.subheader("⚖️ Death Rate Comparison")
if compare_countries:
    st.plotly_chart(plot_death_rate(df, compare_countries), 
                    use_container_width=True)

st.caption("Data Source: Our World in Data | Built with Python, Pandas, Plotly & Streamlit")