import pandas as pd

files = {
    "01_fund_master.csv":"01_fund_master_cleaned.csv",
    "03_aum_by_fund_house.csv":"03_aum_by_fund_house_cleaned.csv",
    "04_monthly_sip_inflows.csv":"04_monthly_sip_inflows_cleaned.csv",
    "05_category_inflows.csv":"05_category_inflows_cleaned.csv",
    "06_industry_folio_count.csv":"06_industry_folio_count_cleaned.csv",
    "09_portfolio_holdings.csv":"09_portfolio_holdings_cleaned.csv",
    "10_benchmark_indices.csv":"10_benchmark_indices_cleaned.csv"
}

for source, target in files.items():
    df = pd.read_csv(f"data/raw/{source}")
    df = df.drop_duplicates()
    df.to_csv(f"data/processed/{target}", index=False)
    print(f"{target} created")