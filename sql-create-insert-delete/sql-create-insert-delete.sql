USE dsstudent;

CREATE TABLE person_Aj
	(person_id SMALLINT,
	first_name varchar(20), 
	last_name VARCHAR(20),
	city varchar(20),
	CONSTRAINT pk_t1 PRIMARY KEY(person_id)
	);

desc t1

show tables

INSERT INTO person_Aj (person_id, first_name , last_name , city)
VALUES (1, 'Aj', 'Villegas', 'LB');

INSERT INTO person_Aj (person_id, first_name , last_name , city)
VALUES (2, 'Katye', 'Villegas', 'Irvine'),
	   (3, 'Ethan', 'Villegas', 'Rancho');
	  
ALTER TABLE person_Aj 
ADD gender char(6);

UPDATE person_Aj 
SET gender = 'male'
WHERE person_id IN (1,3);

UPDATE person_Aj 
SET gender = 'female'
WHERE person_id = 2;

ALTER TABLE person_Aj 
DROP gender;

DELETE FROM person_Aj
WHERE person_id=2;

DROP TABLE person_Aj;