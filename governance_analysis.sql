-- SQLite CLI: run from repository root after python risk_assessment.py
.mode csv
.import reports/risk_register.csv risk_register
SELECT tier, COUNT(*) AS suppliers, SUM(CAST(annual_spend AS INTEGER)) AS spend FROM risk_register GROUP BY tier;
SELECT supplier_id, score, actions FROM risk_register WHERE tier = 'High' ORDER BY CAST(score AS INTEGER) DESC;
SELECT category, COUNT(*) AS suppliers, SUM(CASE WHEN CAST(exceptions AS INTEGER)>0 THEN 1 ELSE 0 END) AS exceptions FROM risk_register GROUP BY category;
