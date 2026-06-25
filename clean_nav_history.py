import pandas as pd

# Load dataset
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

print("Original Shape:", nav_history.shape)

# Convert date column to datetime
nav_history["date"] = pd.to_datetime(nav_history["date"])

# Sort data
nav_history = nav_history.sort_values(
    by=["amfi_code", "date"]
)

# Forward fill missing NAV values
nav_history["nav"] = nav_history.groupby(
    "amfi_code"
)["nav"].ffill()

# Remove duplicates
nav_history = nav_history.drop_duplicates()

# Keep only valid NAV values
nav_history = nav_history[
    nav_history["nav"] > 0
]

print("Cleaned Shape:", nav_history.shape)

# Save cleaned file
nav_history.to_csv(
    "data/processed/02_nav_history_cleaned.csv",
    index=False
)

print("nav_history cleaned successfully.")