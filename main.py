import pandas as pd
import plotly.express as px
import streamlit as st

st.title('DASHCOVID')

df = pd.read_csv('WHO_time_series.csv')

df['Date_reported'] = pd.to_datetime(df['Date_reported'])

fig1 = px.line(df, x = 'Date_reported', y = 'Cumulative_cases', title = 'Número de casos acumulados de COVID-19')

st.plotly_chart(fig1, use_container_width = True)
