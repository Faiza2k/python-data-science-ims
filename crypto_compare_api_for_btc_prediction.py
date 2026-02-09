import requests
import pandas as pd

url = "https://min-api.cryptocompare.com/data/v2/histoday"

params = {
    "fsym": "BTC",
    "tsym": "USDT",
    "limit": 365
}

response = requests.get(url, params=params)
data = response.json()["Data"]["Data"]

df = pd.DataFrame(data)
df["time"] = pd.to_datetime(df["time"], unit="s")

df = df.rename(columns={
    "time": "Date",
    "open": "Open",
    "high": "High",
    "low": "Low",
    "close": "Close",
    "volumeto": "Volume"
})

df["Liquidity"] = df["Close"] * df["Volume"]

print(df.head())
print("Total records:", len(df))

df_final = df[["Date", "Open", "High", "Low", "Close", "Volume", "Liquidity"]]
df_final.to_csv("C:/Users/Faiza/BB/proj2/btc_1y_daily.csv", index=False)
