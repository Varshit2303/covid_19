import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def plot_cases_over_time(df, country):
    fig = px.line(
        df, 
        x='date', 
        y='new_cases',
        title=f'Daily New Cases - {country}',
        labels={'new_cases': 'New Cases', 'date': 'Date'}
    )
    return fig

def plot_deaths_over_time(df, country):
    fig = px.line(
        df,
        x='date',
        y='new_deaths',
        color_discrete_sequence=['red'],
        title=f'Daily New Deaths - {country}',
        labels={'new_deaths': 'New Deaths', 'date': 'Date'}
    )
    return fig

def plot_top_countries(df):
    # Get latest data per country
    latest = df.sort_values('date').groupby('location').last().reset_index()
    top10 = latest.nlargest(10, 'total_cases')[['location', 'total_cases']]
    
    fig = px.bar(
        top10,
        x='location',
        y='total_cases',
        title='Top 10 Countries by Total Cases',
        labels={'location': 'Country', 'total_cases': 'Total Cases'}
    )
    return fig

def plot_death_rate(df, countries):
    latest = df.sort_values('date').groupby('location').last().reset_index()
    filtered = latest[latest['location'].isin(countries)].copy()
    filtered['death_rate'] = (
        filtered['total_deaths'] / filtered['total_cases'] * 100
    )
    
    fig = px.bar(
        filtered,
        x='location',
        y='death_rate',
        title='Death Rate Comparison (%)',
        labels={'death_rate': 'Death Rate (%)', 'location': 'Country'}
    )
    return fig