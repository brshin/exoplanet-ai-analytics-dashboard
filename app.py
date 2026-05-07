import requests
import pandas as pd
import plotly.express as px
import streamlit as st

st.title("NASA Exoplanet Dashboard")
st.write("Hover over the dots to see the name of the planet!")

targetUrl = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+pl_name,pl_bmasse,pl_orbper+from+ps&format=json"

response = requests.get(targetUrl)

if response.status_code == 200:
    print("Connection successful!")

    raw_data = response.json()

    df = pd.DataFrame(raw_data)

    # print(df.head())

    df['pl_bmasse'] = pd.to_numeric(df['pl_bmasse'], errors='coerce')
    df['pl_orbper'] = pd.to_numeric(df['pl_orbper'], errors='coerce')

    df = df.dropna()

    print(df)

    x_data = df['pl_bmasse']
    y_data = df['pl_orbper']

    fig = px.scatter(
        df,
        x='pl_bmasse',
        y='pl_orbper',
        hover_name='pl_name',
        log_x=True,
        log_y=True,
        title="Planet Mass vs Orbital Period"
    )

    st.plotly_chart(fig)


else:
    print("Failed to connect.")

