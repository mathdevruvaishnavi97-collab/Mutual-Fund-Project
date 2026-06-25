# Mutual Fund Project

This project is developed as part of the Bluestock Fintech Data Analyst Internship.

## Project Objective

The main objective of this project is to perform data ingestion and initial analysis on mutual fund datasets. It includes loading datasets, fetching live NAV data, validating AMFI codes, and preparing the data for further analysis and dashboard development.

## Folder Structure

```
MutualFund_Project
│
├── data
│   ├── raw
│   └── processed
├── notebooks
├── sql
├── dashboard
├── reports
├── data_ingestion.py
├── live_nav_fetch.py
├── fetch_multiple_nav.py
├── explore_fund_master.py
├── validate_amfi_codes.py
├── requirements.txt
└── README.md
```

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Requests
- SQLAlchemy
- Jupyter Notebook

## Tasks Completed (Day 1)

- Created project folder structure.
- Loaded and explored 10 datasets using Pandas.
- Checked shape, data types, and missing values.
- Fetched live NAV data from MFAPI.
- Retrieved NAV data for key mutual fund schemes.
- Explored fund houses, categories, and risk levels.
- Validated AMFI scheme codes.
- Prepared a data quality summary.
- Uploaded the project to GitHub.

Day 2 – Data Cleaning & SQLite Database Design
Tasks Completed
Data Cleaning
Cleaned NAV history dataset.
Converted dates to datetime format.
Sorted records by AMFI code and date.
Removed duplicates.
Validated NAV values.
Investor Transactions Cleaning
Standardized transaction types.
Validated transaction amounts.
Fixed date formats.
Verified KYC status values.
Scheme Performance Cleaning
Validated return metrics.
Checked expense ratio ranges.
Identified and reviewed anomalies.
Database Design
Designed SQLite star schema.
Created dimension and fact tables.
Defined primary and foreign key relationships.
Database Loading
Loaded cleaned datasets into SQLite using SQLAlchemy.
Verified row counts after loading.
SQL Analytics
Created 10 analytical SQL queries for business insights.
Documentation
Created data dictionary.
Created data quality summary report.
Deliverables
10 cleaned CSV files
bluestock_mf.db
schema.sql
queries.sql
data_dictionary.md
data_quality_summary.txt

## Author

**Vaishnavi Mathdevru**  
Data Analyst Intern  
Bluestock Fintech
