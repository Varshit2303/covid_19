markdown# COVID-19 Global Data Analysis Dashboard

An interactive web dashboard that analyzes and visualizes 
global COVID-19 trends using real-world epidemiological data 
spanning 200+ countries from 2020 to 2023.

## Overview

This project builds a complete data analysis pipeline — 
from raw data ingestion and cleaning to interactive visual 
storytelling — helping users explore how the pandemic 
unfolded across different regions and time periods.

The dashboard allows users to compare countries, track 
case and death trends over time, and analyze death rates 
side by side — all through a clean, filter-driven interface.

## Features

- Country-wise daily case and death trend analysis
- Top 10 most affected countries comparison chart
- Death rate comparison across multiple selected countries
- Dynamic sidebar filters for country selection
- Summary metrics — total cases, total deaths, 
  peak daily cases, and death rate
- Interactive charts with hover details powered by Plotly

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.11 |
| Data Processing | Pandas |
| Visualization | Plotly, Matplotlib, Seaborn |
| Web Framework | Streamlit |
| Version Control | Git and GitHub |
| Hosting | Render |

## Project Structure
covid_19/
├── app.py                 # Main Streamlit dashboard
├── analysis.py            # Data loading and cleaning logic
├── visualizations.py      # Chart generation functions
├── requirements.txt       # Python dependencies
├── runtime.txt            # Python version specification
└── README.md              # Project documentation

## Dataset

Data sourced from Our World in Data — one of the most 
reliable and comprehensive public COVID-19 datasets, 
updated regularly with verified statistics from 
health ministries worldwide.

To run locally, download the dataset and save it 
as covid_data.csv in the project root:
https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv

## How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/Varshit2303/covid_19.git
cd covid_19
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate       # Mac/Linux
venv\Scripts\activate          # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Download the dataset
Save covid_data.csv in the project root folder
using the dataset link above

### 5. Run the dashboard
```bash
streamlit run app.py
```

Open your browser at http://localhost:8501

## Key Insights Uncovered

- Identified peak wave periods and their duration 
  across major countries
- Compared death rates between developed and 
  developing nations
- Visualized how population size correlates with 
  total case counts
- Tracked how daily new cases evolved differently 
  across regions

## Live Demo

Coming soon — deployed on Render

## Author

Varshit
B.Tech Computer Science (AI and ML) — 2026 Batch
GitHub: https://github.com/Varshit2303

## License

This project is licensed under the MIT License.
This project is built for educational purposes using 
publicly available data.

