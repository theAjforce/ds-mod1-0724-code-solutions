
USE telecom;

SELECT id, log_feature, volume,
CASE
	WHEN volume < 100 THEN "low"
	WHEN volume > 500 THEN "large"
	ELSE "medium"
END volume_1
FROM log_feature; 

SELECT volume_1, COUNT(volume) AS value_counts
FROM dsstudent.conditional_logic
GROUP BY volume_1
ORDER BY value_counts DESC;

USE hr;

SELECT EmployeeNumber, HourlyRate,
CASE
	WHEN HourlyRate > 80 THEN "high hourly rate"
	WHEN HourlyRate < 40 THEN "low hourly rate"
	ELSE "medium hourly rate"
END HourlyRate_1
FROM employee;

SELECT Gender,
CASE 
	WHEN Gender = "Female" THEN 0
	ELSE 1
END Gender_1
FROM employee;
