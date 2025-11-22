import requests
import pandas as pd

# ---------- CONFIG ----------
LAT, LON = 23.2167, 72.6833
URL = (f"https://api.open-meteo.com/v1/forecast?"
       f"latitude={LAT}&longitude={LON}"
       f"&hourly=temperature_2m,relative_humidity_2m,"
       f"cloud_cover,wind_speed_10m,surface_pressure,shortwave_radiation"
       f"&forecast_days=1&timezone=auto")

print("📡 Fetching weather data ...")
data = requests.get(URL).json()["hourly"]
df = pd.DataFrame(data)

print("Data succesfully fetched")
print(df.head())