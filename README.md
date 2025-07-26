# Wallet Risk Scoring – Assignment

## Overview
This project assigns a **risk score (0–1000)** to each wallet based on its transaction behavior on the **Compound V2/V3 lending protocol**.  
The scoring is derived from on-chain transaction data and highlights risk factors such as liquidations and repayment behavior.

---

## Objectives
1. **Fetch Transaction History**  
   Retrieve on-chain transaction data for each provided wallet address using the **Covalent API** (or mock data for testing).  
   
2. **Data Preparation**  
   Preprocess and organize transactions to compute key lending/borrowing features.  
   
3. **Risk Scoring**  
   Develop a scoring model that assigns each wallet a risk score ranging from **0 to 1000**.

---

## Data Collection Method
We used the **Covalent API** to fetch transaction histories for all given wallet addresses.  
This API provides detailed on-chain transaction data for Ethereum, including interactions with DeFi protocols such as **Compound V2 and V3**.  
For testing and demonstration, we also implemented a **mock mode** that generates synthetic transaction data when API keys are unavailable.  
Each wallet's transactions were retrieved and stored in structured form using **Pandas DataFrames**.

---

## Feature Selection Rationale
The risk profile of a wallet was derived from the following features:  
- **Borrow Count** → number of borrow transactions (higher borrow → higher risk).  
- **Repay Count** → number of repayments (lower repayments → higher risk).  
- **Liquidations** → indicates failed positions or defaults (high liquidations → very high risk).  
- **Total Transaction Count** → activity level (inactive wallets with loans may be riskier).  

These features were chosen because they directly reflect lending/borrowing behaviors and potential repayment reliability.

---

## Scoring Methodology
1. All features were normalized on a **0–1 scale** to handle different value ranges.  
2. We applied weighted aggregation:  
   - **40% Liquidations** (most important)  
   - **30% (1 - normalized Repay Count)** (lack of repayments adds risk)  
   - **20% Borrow Count** (loan exposure risk)  
   - **10% Transaction Count** (activity signal)  
3. The final score was scaled from **0 to 1000**, where:  
   - **0 = lowest risk**  
   - **1000 = highest risk**  

---

## Justification of Risk Indicators
The selected indicators are widely used in DeFi risk assessments because:  
- **Liquidations** are a direct result of loan defaults.  
- **Borrow vs. Repay ratio** reflects creditworthiness.  
- **Wallet activity** gives additional context (e.g., dormant borrowers may pose repayment risk).  

This approach allows easy scalability to other DeFi protocols and future integration of additional risk features (e.g., collateral ratio, token volatility exposure).

---

## Sample Output
Below is a sample of the risk scoring output for the first 5 wallet addresses:  

| wallet_id                                   | score |
|--------------------------------------------|-------|
| 0x0039f22efb07a647557c7c5d17854cfd6d489ef3 | 732   |
| 0x06b51c6882b27cb05e712185531c1f74996dd988 | 645   |
| 0x0795732aacc448030ef374374eaae57d2965c16c | 812   |
| 0x0aaa79f1a86bc8136cd0d1ca0d51964f4e3766f9 | 503   |
| 0x0fe383e5abc200055a7f391f94a5f5d1f844b9ae | 920   |

The full dataset with all 100 wallets is saved as `data/wallet_risk_scores.csv`.

---
  ```bash
## Project Structure
project/
├── data/
│ ├── wallets.csv # Provided wallet addresses
│ └── wallet_risk_scores.csv # Final risk scores
├── notebooks/
│ └── wallet_risk_scoring.ipynb # Code + explanation
├── main.py # Optional script version
├── requirements.txt
└── README.md # Project overview

  ```
  ```bash
Wallets CSV → Fetch Transactions → Feature Engineering → Risk Scoring → Output CSV
  ```

---

## How to Run
1. Clone the repository and navigate to the folder.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
  ```bash
  python main.py
