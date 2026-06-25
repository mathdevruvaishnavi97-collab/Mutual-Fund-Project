import pandas as pd

# Load dataset
performance = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

print("Original Shape:", performance.shape)

# Return columns to validate
return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct"
]

# Convert return columns to numeric
for col in return_columns:
    performance[col] = pd.to_numeric(
        performance[col],
        errors="coerce"
    )

# Check missing values after conversion
print("\nMissing Values in Return Columns:")
print(performance[return_columns].isnull().sum())

# Expense ratio validation
invalid_expense = performance[
    (performance["expense_ratio_pct"] < 0.1)
    |
    (performance["expense_ratio_pct"] > 2.5)
]

print("\nFunds with Invalid Expense Ratio:")
print(invalid_expense[
    ["scheme_name", "expense_ratio_pct"]
])

# Remove duplicates
performance = performance.drop_duplicates()

print("\nCleaned Shape:", performance.shape)

# Save cleaned file
performance.to_csv(
    "data/processed/07_scheme_performance_cleaned.csv",
    index=False
)

print("\nScheme performance cleaned successfully.")