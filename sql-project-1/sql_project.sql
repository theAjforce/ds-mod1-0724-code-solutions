CREATE TABLE customer_Aj
(customer_id smallint,
name varchar(20),
location varchar(20),
total_expenditure varchar(20));

INSERT INTO customer_Aj (customer_id, name, location, total_expenditure)
VALUES (1701, "John", 'Newport Beach, CA', '2000'),
(1707, 'Tracy', 'Irvine, CA', '1500'),
(1711, 'Daniel', 'Newport Beach, CA', '2500'),
(1703, 'Ella', 'Santa Ana, CA', '1800'),
(1708, 'Mel', 'Orange, CA', '1700'),
(1716, 'Steve', 'Irvine, CA', '18000');

UPDATE customer_Aj
SET total_expenditure = '1800'
WHERE customer_id IN (1716);

ALTER TABLE customer_Aj 
ADD gender varchar(20);

UPDATE customer_Aj 
SET gender = 'M'
WHERE customer_id IN (1701, 1711, 1716);

UPDATE customer_Aj 
SET gender = 'F'
WHERE customer_id IN (1707, 1703, 1708);

DELETE FROM customer_Aj 
WHERE customer_id=1716;

ALTER TABLE customer_Aj 
ADD store varchar(20);

ALTER TABLE customer_Aj 
DROP COLUMN store;

SELECT * FROM customer_Aj;

SELECT name n, total_expenditure total_exp
FROM customer_Aj;

ALTER TABLE customer_Aj 
DROP COLUMN total_expenditure;

ALTER TABLE customer_Aj 
ADD total_expenditure smallint;

UPDATE customer_Aj 
SET total_expenditure = 2000
WHERE name='John';

UPDATE customer_Aj 
SET total_expenditure = 1500
WHERE name='Tracy';

UPDATE customer_Aj 
SET total_expenditure = 2500
WHERE name='Daniel';

UPDATE customer_Aj 
SET total_expenditure = 1800
WHERE name='Ella';

UPDATE customer_Aj 
SET total_expenditure = 1700
WHERE name='Mel';

SELECT total_expenditure
FROM customer_Aj
ORDER BY total_expenditure DESC;

SELECT name, total_expenditure
FROM customer_Aj
ORDER BY total_expenditure DESC 
LIMIT 3;

SELECT COUNT(DISTINCT(location)) nunique
FROM customer_Aj;

SELECT DISTINCT(location) unique_cities
FROM customer_Aj ca;

SELECT * FROM customer_Aj ca 
WHERE gender = 'M';

SELECT * FROM customer_Aj ca 
WHERE gender = 'F';

SELECT * FROM customer_Aj ca 
WHERE location = 'Irvine, CA';

SELECT name, location
FROM customer_Aj ca 
WHERE total_expenditure < 2000
ORDER BY name ASC;