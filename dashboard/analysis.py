import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

URL_DATASET = 'https://raw.githubusercontent.com/anazantoro/dicoding-dataset-bikesharing/refs/heads/main/update_day.csv'
df = pd.read_csv(URL_DATASET)

def display_analysis(analysis_choice):
    if analysis_choice == 'Pola Rental Berdasarkan Musim':
        display_season_analysis(df)
    elif analysis_choice == 'Distribusi Rental Hari Libur vs Hari Kerja':
        display_holiday_workday_analysis(df)
    elif analysis_choice == 'Hubungan antara Kondisi Cuaca dan Jumlah Rental':
        display_weather_analysis(df)
    
def display_season_analysis(df):
    st.header('Pola Rental Berdasarkan Musim')
    season_mapping = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
    df['season_name'] = df['season'].map(season_mapping)

    for season, season_name in season_mapping.items():
        season_data = df[df['season'] == season]
        st.subheader(season_name)
        st.line_chart(season_data.set_index('dteday')['cnt'])

    st.header('Distribusi Rental Berdasarkan Musim')

    season_names = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}

    df['season_name'] = df['season'].map(season_names)

    sales_by_season = df.groupby('season_name')['cnt'].sum().reset_index()

    fig = px.bar(sales_by_season, x='season_name', y='cnt', title='Total Rental Berdasarkan Musim')
    fig.update_xaxes(title='Musim')
    fig.update_yaxes(title='Total Rental')
    st.plotly_chart(fig)

def display_holiday_workday_analysis(df):
    st.header('Distribusi Rental pada Hari Libur dan Hari Kerja')

    sales_by_day_type = df.groupby(['holiday', 'workingday'])['cnt'].sum().reset_index()

    sales_by_day_type['holiday'] = sales_by_day_type['holiday'].map({0: 'Non-Holiday', 1: 'Holiday'})
    sales_by_day_type['workingday'] = sales_by_day_type['workingday'].map({0: 'Non-Working Day', 1: 'Working Day'})

    fig = px.bar(sales_by_day_type, x='holiday', y='cnt', color='workingday', barmode='group',
                 title='Distribusi Rental pada Hari Libur dan Hari Kerja',
                 labels={'holiday': 'Jenis Hari', 'cnt': 'Jumlah Rental', 'workingday': 'Status Hari'})

    st.plotly_chart(fig)
    
def display_weather_analysis(df):
    st.header('Hubungan antara Kondisi Cuaca dan Jumlah Rental')

    weather_categories = {1: 'Clear', 2: 'Mist', 3: 'Light Rain/Snow'}

    df['weather_condition'] = df['weathersit'].map(weather_categories)

    sales_by_weather = df.groupby('weather_condition')['cnt'].sum().reset_index()

    st.subheader('Jumlah Rental Berdasarkan Kondisi Cuaca')
    st.write("Visualisasi hubungan antara Kondisi Cuaca dan Jumlah Rental")

    st.bar_chart(sales_by_weather.set_index('weather_condition'))