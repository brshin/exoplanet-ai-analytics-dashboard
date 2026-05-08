import requests
import pandas as pd
import plotly.express as px
import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

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

    dfUnique = df.drop_duplicates(subset='pl_name')
    print(dfUnique)

    x_data = dfUnique['pl_bmasse']
    y_data = dfUnique['pl_orbper']

    fig = px.scatter(
        dfUnique,
        x='pl_bmasse',
        y='pl_orbper',
        hover_name='pl_name',
        log_x=True,
        log_y=True,
        title="Planet Mass vs Orbital Period"
    )

    selectedPlanet = st.selectbox("Select a planet to analyze:", dfUnique['pl_name'])

    selectedPlanetMass = dfUnique.loc[dfUnique['pl_name'] == selectedPlanet, 'pl_bmasse'].values[0]
    print(selectedPlanetMass)

    selectedPlanetOrbitalPeriod = dfUnique.loc[dfUnique['pl_name'] == selectedPlanet, 'pl_orbper'].values[0]
    print(selectedPlanetOrbitalPeriod)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Name", selectedPlanet)
    
    with col2:
        st.metric("Mass (Earth Masses)", selectedPlanetMass)
    
    with col3:
        st.metric("Orbital Period (Days)", selectedPlanetOrbitalPeriod)

    if st.button('Generate AI Analysis'):

        with st.spinner("Connecting to AI..."):

            prompt = f"Act as a NASA astrophysicist. I am analyzing exoplanet {selectedPlanet}. It has a mass of {selectedPlanetMass} Earth masses and an orbital period of {selectedPlanetOrbitalPeriod} days. Give me a 2-sentence scientific hypothesis of what its climate or environment might be like."

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            
            aiSummary = response.choices[0].message.content
            st.success(aiSummary)




    st.plotly_chart(fig)


else:
    print("Failed to connect.")

