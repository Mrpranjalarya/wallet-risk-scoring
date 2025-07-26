import pandas as pd
import numpy as np

def score_wallets(df):
    for col in ["borrow_count", "repay_count", "liquidations", "tx_count"]:
        df[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min() + 1e-6)
    df["score"] = (0.4 * df["liquidations"] +
                   0.3 * (1 - df["repay_count"]) +
                   0.2 * df["borrow_count"] +
                   0.1 * df["tx_count"]) * 1000
    return df[["wallet_id", "score"]]
