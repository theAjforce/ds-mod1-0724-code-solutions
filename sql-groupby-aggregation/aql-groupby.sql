
SELECT location, COUNT(DISTINCT(event_type)) AS num_unique_event_type
FROM dsstudent.telecom_db
GROUP BY location
ORDER BY location;

SELECT location, SUM(volume) AS total_volume
FROM dsstudent.telecom_db
GROUP BY location
ORDER BY total_volume DESC
LIMIT 3;


SELECT fault_severity, COUNT(DISTINCT(location)) AS num_of_unique_locations
FROM dsstudent.telecom_db
GROUP BY fault_severity
HAVING fault_severity > 1;

USE hr;

SELECT attrition, MIN(age) AS min_age, MAX(age) AS max_age, AVG(age) AS avg_age
FROM employee
GROUP BY attrition;

SELECT Attrition, Department, COUNT(*) AS num_quanitity
FROM employee
WHERE Attrition IS NOT NULL
GROUP BY Attrition, Department
ORDER BY Attrition, Department ASC;


SELECT Attrition, Department, COUNT(*) AS num_quantity
FROM employee
WHERE Attrition IS NOT NULL
GROUP BY Attrition, Department
HAVING num_quantity > 100
ORDER BY Attrition, Department ASC;
