CREATE DATABASE college_db;
USE college_db;

CREATE TABLE students(
id INT PRIMARY KEY,
name VARCHAR(100) NOT NULL,
email VARCHAR(100) UNIQUE,
age INT CHECK (AGE>=18),
course VARCHAR(40) DEFAULT 'B.Tech');

SELECT*FROM students;

INSERT INTO students VALUES
(1,'vaibhav','vaibhav@gmail.com', 22, 'B.Tech'),
(2,'shubham' ,'shubham@gmail.com', 22, 'B.Tech'),
(3,'aditya','aditya@gmail.com', 22, 'B.Tech');

SELECT*FROM students;

SELECT name, email FROM students;
SELECT * FROM students WHERE name='vaibhav';
SELECT * FROM students WHERE age=22 AND name ='shubham';
SELECT * FROM students WHERE age BETWEEN 20 AND 25;
SELECT * FROM students WHERE name IN ('shubham','aditya');

-- starts with v
SELECT * FROM students WHERE name LIKE 'v%'; 

-- end with a
SELECT * FROM students WHERE name LIKE 'a%';

-- contain sh
SELECT * FROM students WHERE name LIKE '%sh%';
SELECT * FROM students WHERE age BETWEEN 20 AND 25 ORDER BY id desc LIMIT 2;
 
 -- UPDATE
 
 UPDATE students SET age=18  WHERE id=2;
 
 SELECT*FROM students;