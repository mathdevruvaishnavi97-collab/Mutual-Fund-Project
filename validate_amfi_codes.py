import pandas as pd

# Load datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

# Extract unique AMFI codes
fund_master_codes = set(fund_master["amfi_code"])
nav_history_codes = set(nav_history["amfi_code"])

# Find missing codes
missing_codes = fund_master_codes - nav_history_codes

# Display results
print("\nTotal schemes in fund master:", len(fund_master_codes))
print("Total schemes in NAV history:", len(nav_history_codes))

if len(missing_codes) == 0:
    print("\nAll AMFI codes are present in nav_history.")
else:
    print("\nMissing AMFI codes:")
    print(missing_codes)

print("\nAMFI code validation completed successfully.")