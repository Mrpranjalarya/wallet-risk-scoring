import pandas as pd

def compute_features(tx_df):
    if tx_df.empty:
        return {"borrow_count": 0, "repay_count": 0, "liquidations": 0, "tx_count": 0}

    borrow_count = tx_df[tx_df['to_address'].str.contains("compound", case=False, na=False)].shape[0]
    repay_count = tx_df[tx_df['from_address'].str.contains("compound", case=False, na=False)].shape[0]
    liquidations = tx_df[tx_df['log_events'].notnull()].shape[0]  # crude proxy
    return {
        "borrow_count": borrow_count,
        "repay_count": repay_count,
        "liquidations": liquidations,
        "tx_count": len(tx_df)
    }
