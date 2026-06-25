import pandas as pd

# Load dataset
transactions = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

print("Original Shape:", transactions.shape)

# Convert date column
transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"]
)

# Standardize transaction type values
transactions["transaction_type"] = (
    transactions["transaction_type"]
    .str.strip()
    .str.title()
)

# Keep only positive transaction amounts
transactions = transactions[
    transactions["amount_inr"] > 0
]

# Check KYC status values
print("\nKYC Status Values:")
print(transactions["kyc_status"].unique())

# Remove duplicates
transactions = transactions.drop_duplicates()

print("\nCleaned Shape:", transactions.shape)

# Save cleaned file
transactions.to_csv(
    "data/processed/08_investor_transactions_cleaned.csv",
    index=False
)

print("\nInvestor transactions cleaned successfully.")