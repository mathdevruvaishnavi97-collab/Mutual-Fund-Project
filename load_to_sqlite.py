import pandas as pd
from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

# Load cleaned datasets

nav_history = pd.read_csv(
    "data/processed/02_nav_history_cleaned.csv"
)

transactions = pd.read_csv(
    "data/processed/08_investor_transactions_cleaned.csv"
)

performance = pd.read_csv(
    "data/processed/07_scheme_performance_cleaned.csv"
)

# Load tables into SQLite

nav_history.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

# Verify row counts

print("fact_nav rows:", len(nav_history))
print("fact_transactions rows:", len(transactions))
print("fact_performance rows:", len(performance))

print("\nSQLite database created successfully.")