-- CREATE DATABASE practice;
-- USE practice;

-- CREATE TABLE info(
-- id INT PRIMARY KEY,
-- name VARCHAR(100) NOT NULL,
-- email VARCHAR(100) UNIQUE,
-- dob DATE,
-- info_time DATETIME DEFAULT CURRENT_TIMESTAMP
-- );

-- SELECT*FROM INFO

-- INSERT INTO info VALUES
-- (1,'VAIBHAV','vaibhav@gmail.com','2003-11-29', DEFAULT),
-- (2,'ADITYA','ADITYA@gmail.com','2003-11-24', DEFAULT),
-- (3,'SABLE','SABLE@gmail.com','2003-11-19', DEFAULT),
-- (4,'BHABAD','BHABAD@gmail.com','2007-11-01', DEFAULT);

-- For  printing specific coloum data
SELECT name, email FROM info;
SELECT dob, info_time FROM info;alter

-- Renaming a table

RENAME TABLE info TO user;
SHOW TABLES;
rename table info to users;
show tables;

RENAME TABLE USERS TO info;

-- ALTER TABLE

-- ADD COLUMN
ALTER TABLE info ADD COLUMN is_active BOOLEAN DEFAULT TRUE;
SELECT*FROM info;

-- DROP COLUMN
ALTER TABLE info DROP COLUMN is_active;
SELECT*FROM info;

-- MODIFY A COLUM TYPE 
ALTER TABLE info MODIFY COLUMN name VARCHAR(140);

-- MOVE COLUMN 
ALTER TABLE info MODIFY COLUMN email VARCHAR(100) AFTER dob;
SELECT*FROM info;


SELECT*FROM INFO;






