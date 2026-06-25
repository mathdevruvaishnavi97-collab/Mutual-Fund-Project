-- 1. Top 5 funds by AUM

SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV

SELECT AVG(nav) AS average_nav
FROM fact_nav;

-- 3. Total transactions by type

SELECT transaction_type,
COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY transaction_type;

-- 4. Average transaction amount

SELECT AVG(amount_inr) AS avg_transaction
FROM fact_transactions;

-- 5. Funds with expense ratio less than 1%

SELECT scheme_name, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 6. Top 5 funds by 5-year return

SELECT scheme_name, return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;

-- 7. Fund count by category

SELECT category,
COUNT(*) AS fund_count
FROM fact_performance
GROUP BY category;

-- 8. Highest Sharpe Ratio funds

SELECT scheme_name, sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;

-- 9. Transactions by state

SELECT state,
COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 10. Risk grade distribution

SELECT risk_grade,
COUNT(*) AS total_funds
FROM fact_performance
GROUP BY risk_grade;