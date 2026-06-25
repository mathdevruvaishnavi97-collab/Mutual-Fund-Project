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


# Day 2 – Data Cleaning & SQLite Database Design

## Technologies Used

* Python
* Pandas
* NumPy
* SQLAlchemy
* SQLite
* Requests
* Jupyter Notebook
* Git & GitHub

## Tasks Completed

### Data Cleaning

* Cleaned NAV history dataset.
* Converted date columns to datetime format.
* Sorted records by AMFI code and date.
* Removed duplicate records.
* Validated NAV values greater than zero.

### Investor Transactions Cleaning

* Standardized transaction type values.
* Validated transaction amounts.
* Fixed date formats.
* Verified KYC status values.
* Removed duplicate records.

### Scheme Performance Cleaning

* Validated return metrics as numeric values.
* Checked expense ratio ranges.
* Identified and reviewed anomalies.
* Removed duplicate records.

### Database Design

* Designed SQLite star schema.
* Created dimension and fact tables.
* Defined primary and foreign key relationships.

### Database Loading

* Created SQLite database using SQLAlchemy.
* Loaded cleaned datasets into SQLite.
* Verified row counts after loading.

### SQL Analytics

* Created 10 analytical SQL queries for business insights.
* Analyzed fund performance, NAV trends, transaction patterns, and expense ratios.

### Documentation

* Created data dictionary.
* Created data quality summary report.
* Documented database schema and analytical queries.

## Deliverables

* 10 cleaned CSV files in `data/processed/`
* `bluestock_mf.db`
* `schema.sql`
* `queries.sql`
* `data_dictionary.md`
* `data_quality_summary.txt`

## Day 2 Status

* Data cleaning completed successfully.
* SQLite database created and validated.
* Analytical SQL queries prepared.
* Documentation completed.
* Project updated and committed to GitHub.


## Author

**Vaishnavi Mathdevru**  
Data Analyst Intern  
Bluestock Fintech
