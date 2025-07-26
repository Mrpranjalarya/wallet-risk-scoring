import requests
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()
API_KEY = os.getenv("COVALENT_API_KEY")
CHAIN_ID = 1  # Ethereum mainnet

def fetch_wallet_transactions(wallet):
    url = f"https://api.covalenthq.com/v1/{CHAIN_ID}/address/{wallet}/transactions_v3/"
    params = {"key": API_KEY}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()["data"]["items"]
        return pd.DataFrame(data)
    else:
        print(f"Error fetching {wallet}: {response.status_code}")
        return pd.DataFrame()
