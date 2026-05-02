import pandas as pd

def load_data():
    df = pd.read_csv("covid_data.csv")
    return df

def clean_data(df):
    cols = ['date', 'location', 'total_cases', 'new_cases',
            'total_deaths', 'new_deaths', 'population']
    df = df[cols]
    df = df.dropna(subset=['total_cases', 'total_deaths'])
    df['date'] = pd.to_datetime(df['date'])
    return df

def get_country_data(df, country):
    return df[df['location'] == country].reset_index(drop=True)

def get_summary_stats(df, country):
    country_df = get_country_data(df, country)
    stats = {
        "Total Cases": int(country_df['total_cases'].max()),
        "Total Deaths": int(country_df['total_deaths'].max()),
        "Peak New Cases": int(country_df['new_cases'].max()),
        "Death Rate (%)": round(
            country_df['total_deaths'].max() /
            country_df['total_cases'].max() * 100, 2
        )
    }
    return stats