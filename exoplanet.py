import requests
import pandas as pd
import matplotlib.pyplot as plt

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

    plt.scatter(x_data, y_data, color='blue', alpha=0.7)

    plt.title("Exoplanets: Planet Mass vs. Orbital Period")
    plt.xlabel("Planet Mass (Earth Masses)")
    plt.ylabel("Orbital Period (Days)")

    plt.xscale('log')
    plt.yscale('log')

    plt.show()


else:
    print("Failed to connect.")

