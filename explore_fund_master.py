import pandas as pd

# Load fund master dataset
fund_master = pd.read_csv("data/raw/01_fund_master.csv")

# Display basic information
print("\nTotal number of schemes:")
print(len(fund_master))

# Unique fund houses
print("\nUnique Fund Houses:")
print(fund_master["fund_house"].unique())

# Unique categories
print("\nUnique Categories:")
print(fund_master["category"].unique())

# Unique sub-categories
print("\nUnique Sub Categories:")
print(fund_master["sub_category"].unique())

# Unique risk grades
print("\nUnique Risk Categories:")
print(fund_master["risk_category"].unique())

# AMFI code information
print("\nSample AMFI Codes:")
print(fund_master["amfi_code"].head(10))