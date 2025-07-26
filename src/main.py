import pandas as pd
from data_fetch import fetch_wallet_transactions
from feature_engineering import compute_features
from risk_scoring import score_wallets

def main():
    # --- Load wallet IDs from CSV ---
    try:
        wallet_df = pd.read_csv("data/wallets.csv")   # path to your wallet list
    except FileNotFoundError:
        print("Error: data/wallets.csv not found. Please add your wallet CSV file.")
        return
    
    wallets = wallet_df["wallet_id"].tolist()
    print(f"Loaded {len(wallets)} wallet addresses")

    features = []
    for w in wallets:
        print(f"Processing wallet: {w}")
        try:
            tx_df = fetch_wallet_transactions(w)
            feat = compute_features(tx_df)
            feat["wallet_id"] = w
            features.append(feat)
        except Exception as e:
            print(f"Error processing wallet {w}: {e}")
            # Add empty/default data for this wallet
            features.append({
                "wallet_id": w,
                "borrow_count": 0,
                "repay_count": 0,
                "liquidations": 0,
                "tx_count": 0
            })

    # --- Convert features to DataFrame ---
    df = pd.DataFrame(features)
    print("Feature extraction completed.")

    # --- Compute risk scores ---
    scored_df = score_wallets(df)
    print("Risk scoring completed.")

    # --- Save output ---
    output_path = "data/wallet_risk_scores.csv"
    scored_df.to_csv(output_path, index=False)
    print(f"Results saved to {output_path}")
    print(scored_df.head())

if __name__ == "__main__":
    main()
