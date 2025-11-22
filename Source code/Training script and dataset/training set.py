import requests
import pandas as pd
import datetime

# ---------- CONFIGURATION ----------
LATITUDE = 23.2167     # Gandhinagar, India
LONGITUDE = 72.6833
START_YEAR = 2023
END_YEAR = 2024
OUTPUT_FILE = "nasa_solar_data.csv"

# ---------- NASA POWER API ----------
def fetch_nasa_data(lat, lon, start, end):
    url = (
        f"https://power.larc.nasa.gov/api/temporal/daily/point?"
        f"start={start}&end={end}"
        f"&latitude={lat}&longitude={lon}"
        f"&community=RE"
        f"&parameters=T2M,RH2M,WS2M,PS,ALLSKY_SFC_SW_DWN"
        f"&format=JSON"
    )

    print("📡 Fetching NASA POWER data...")
    r = requests.get(url)
    r.raise_for_status()
    data = r.json()["properties"]["parameter"]

    # Convert to DataFrame
    df = pd.DataFrame({
        "date": list(data["T2M"].keys()),
        "T2M": list(data["T2M"].values()),
        "RH2M": list(data["RH2M"].values()),
        "WS2M": list(data["WS2M"].values()),
        "PS": list(data["PS"].values()),
        "ALLSKY_SFC_SW_DWN": list(data["ALLSKY_SFC_SW_DWN"].values())
    })

    df["date"] = pd.to_datetime(df["date"], format="%Y%m%d")
    return df

# ---------- MAIN ----------
if __name__ == "__main__":
    start_date = f"{START_YEAR}0101"
    end_date = f"{END_YEAR}1231"

    df = fetch_nasa_data(LATITUDE, LONGITUDE, start_date, end_date)
    print(f"\n✅ Fetched {len(df)} days of data from {df['date'].min().date()} to {df['date'].max().date()}.")

    print("\n🧹 Cleaning data...")
    df = df.dropna()
    df = df.sort_values("date")

    # Save to CSV
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"\n💾 Saved dataset to {OUTPUT_FILE}")

    print("\n📊 Preview:")
    print(df.head())


    # ---------- Optional Visualization ----------
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10,5))
    plt.plot(df["date"], df["ALLSKY_SFC_SW_DWN"], label="Solar Irradiance (W/m²)")
    plt.title("Daily Solar Irradiance (NASA POWER Data)")
    plt.xlabel("Date")
    plt.ylabel("W/m²")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
