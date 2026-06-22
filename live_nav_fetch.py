import requests
import pandas as pd

# HDFC Top 100 Direct Growth
url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

if response.status_code == 200:

    data = response.json()

    scheme_name = data['meta']['scheme_name']

    nav_data = data['data']

    df = pd.DataFrame(nav_data)

    print("Scheme Name:", scheme_name)
    print(df.head())

    df.to_csv("data/raw/HDFC_Top100_NAV.csv", index=False)

    print("\nNAV data saved successfully!")

else:
    print("Failed to fetch data")