USE loandb;
CREATE TEMPORARY TABLE dsstudent.row_counts AS (
    SELECT TABLE_NAME, TABLE_ROWS as row_quantity
    FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_SCHEMA = 'loandb'
);

SELECT *
from dsstudent.row_counts;

SELECT AMT_INCOME_TOTAL as annual_income,
    AMT_INCOME_TOTAL / 12 as monthly_income
FROM loandb.train;
    
SELECT ROUND(DAYS_BIRTH / -365) AS age
FROM loandb.train;
    
SELECT OCCUPATION_TYPE, COUNT(*) AS quantity
FROM loandb.train
WHERE OCCUPATION_TYPE IS NOT NULL
GROUP BY OCCUPATION_TYPE
ORDER BY quantity DESC;

SELECT DAYS_EMPLOYED,
    CASE 
        WHEN DAYS_EMPLOYED = (SELECT MAX(DAYS_EMPLOYED) FROM loandb.train) THEN 'bad data'
        ELSE 'normal data'
    END AS Flag_for_bad_data
FROM loandb.train;
    
CREATE TEMPORARY TABLE dsstudent.splpro2(
SELECT ip.DAYS_INSTALMENT, ip.DAYS_ENTRY_PAYMENT, t.TARGET
FROM loandb.installments_payments ip 
INNER JOIN loandb.train t ON ip.SK_ID_CURR = t.SK_ID_CURR
INNER JOIN credit_card_balance ccb ON ip.SK_ID_CURR = ccb.SK_ID_CURR
INNER JOIN previous_application pa ON ip.SK_ID_CURR = pa.SK_ID_CURR;

SELECT 
    TARGET,
    MIN(DAYS_INSTALMENT) AS min_days_installment,
    MAX(DAYS_INSTALMENT) AS max_days_installment,
    MIN(DAYS_ENTRY_PAYMENT) AS min_days_entry_payment,
    MAX(DAYS_ENTRY_PAYMENT) AS max_days_entry_payment
FROM dsstudent.sqlpro2
GROUP BY TARGET;