# Data Dictionary

## 01_fund_master.csv

| Column Name | Data Type | Description |
|------------|-----------|-------------|
| amfi_code | Integer | Unique AMFI scheme code |
| fund_house | Text | Mutual fund company name |
| scheme_name | Text | Name of mutual fund scheme |
| category | Text | Fund category |
| sub_category | Text | Fund sub-category |
| plan | Text | Direct or Regular plan |
| risk_category | Text | Risk level of the scheme |

---

## 02_nav_history.csv

| Column Name | Data Type | Description |
|------------|-----------|-------------|
| amfi_code | Integer | AMFI scheme code |
| date | Date | NAV date |
| nav | Float | Net Asset Value |

---

## 07_scheme_performance.csv

| Column Name | Data Type | Description |
|------------|-----------|-------------|
| return_1yr_pct | Float | One year return percentage |
| return_3yr_pct | Float | Three year return percentage |
| return_5yr_pct | Float | Five year return percentage |
| expense_ratio_pct | Float | Expense ratio percentage |
| aum_crore | Integer | Assets under management |

---

## 08_investor_transactions.csv

| Column Name | Data Type | Description |
|------------|-----------|-------------|
| investor_id | Text | Unique investor ID |
| transaction_date | Date | Date of transaction |
| transaction_type | Text | SIP, Lumpsum or Redemption |
| amount_inr | Integer | Transaction amount |
| state | Text | Investor state |
| city | Text | Investor city |
| kyc_status | Text | KYC verification status |

Source: Bluestock Mutual Fund Project Datasets