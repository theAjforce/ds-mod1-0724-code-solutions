USE telecom;

SELECT id, log_feature AS `log`, volume AS vol FROM log_feature;

SELECT id, resource_type FROM resource_type ORDER BY id LIMIT 5;

SELECT id, resource_type FROM resource_type ORDER BY id DESC LIMIT 5;

SELECT id, resource_type FROM resource_type ORDER BY 1, 2 DESC LIMIT 5;

SELECT COUNT(*) AS numbers_row, COUNT(DISTINCT(id)) AS id_nunique, COUNT(DISTINCT(severity_type)) AS severity_type_nunique FROM severity_type;

SELECT id, log_feature, volume FROM log_feature WHERE log_feature = 'feature 201' AND volume > 100 AND volume < 300 ORDER BY volume;