import pandas as pd
import os

# Folder containing CSV files
folder_path = "data/raw"

# List all CSV files
csv_files = [file for file in os.listdir(folder_path) if file.endswith(".csv")]

print(f"Found {len(csv_files)} CSV files\n")

for file in csv_files:
    file_path = os.path.join(folder_path, file)

    print("="*60)
    print("File Name:", file)

    df = pd.read_csv(file_path)

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\n")