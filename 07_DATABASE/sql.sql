USE college_db;
CREATE TABLE employees_data (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100),
    department VARCHAR(50),
    salary INT,
    age INT,
    city VARCHAR(50),
    join_date DATE
);

INSERT INTO employees_data VALUES
(1,'Amit','amit@gmail.com','IT',50000,25,'Mumbai','2022-01-10'),
(2,'Rahul','rahul@gmail.com','HR',40000,28,'Pune','2021-03-15'),
(3,'Sneha','sneha@gmail.com','Finance',60000,30,'Delhi','2020-07-20'),
(4,'Priya','priya@gmail.com','IT',55000,26,'Mumbai','2023-02-12'),
(5,'Karan','karan@gmail.com','Sales',45000,27,'Nashik','2022-06-18'),
(6,'Neha','neha@gmail.com','HR',42000,24,'Pune','2021-09-25'),
(7,'Vikas','vikas@gmail.com','IT',70000,32,'Bangalore','2019-11-05'),
(8,'Anjali','anjali@gmail.com','Finance',65000,29,'Delhi','2020-12-30'),
(9,'Rohit','rohit@gmail.com','Sales',48000,31,'Mumbai','2022-08-14'),
(10,'Pooja','pooja@gmail.com','IT',52000,23,'Pune','2023-05-22'),
(11,'Sagar','sagar@gmail.com','HR',39000,26,'Nashik','2021-01-17'),
(12,'Meena','meena@gmail.com','Finance',61000,28,'Delhi','2020-04-10'),
(13,'Arjun','arjun@gmail.com','IT',75000,35,'Bangalore','2018-09-09'),
(14,'Komal','komal@gmail.com','Sales',47000,27,'Mumbai','2022-10-01'),
(15,'Deepak','deepak@gmail.com','HR',41000,29,'Pune','2021-06-11'),
(16,'Riya','riya@gmail.com','IT',53000,24,'Delhi','2023-03-01'),
(17,'Manoj','manoj@gmail.com','Finance',62000,31,'Mumbai','2019-05-21'),
(18,'Kavita','kavita@gmail.com','HR',43000,27,'Pune','2022-11-30'),
(19,'Tarun','tarun@gmail.com','Sales',46000,28,'Nashik','2021-08-19'),
(20,'Simran','simran@gmail.com','IT',58000,26,'Bangalore','2020-02-14'),
(21,'Nikhil','nikhil@gmail.com','Finance',64000,30,'Delhi','2019-12-25'),
(22,'Aarti','aarti@gmail.com','HR',40000,25,'Mumbai','2023-01-05'),
(23,'Yash','yash@gmail.com','Sales',49000,29,'Pune','2022-04-17'),
(24,'Divya','divya@gmail.com','IT',56000,27,'Delhi','2021-07-23'),
(25,'Ramesh','ramesh@gmail.com','Finance',67000,34,'Bangalore','2018-06-10'),
(26,'Sonal','sonal@gmail.com','HR',42000,26,'Mumbai','2020-09-09'),
(27,'Ajay','ajay@gmail.com','Sales',48000,28,'Nashik','2021-02-28'),
(28,'Bhavna','bhavna@gmail.com','IT',59000,29,'Pune','2022-12-12'),
(29,'Chetan','chetan@gmail.com','Finance',63000,32,'Delhi','2019-03-18'),
(30,'Esha','esha@gmail.com','HR',41000,24,'Mumbai','2023-06-20'),
(31,'Farhan','farhan@gmail.com','IT',72000,33,'Bangalore','2018-11-11'),
(32,'Gauri','gauri@gmail.com','Sales',47000,27,'Pune','2022-05-05'),
(33,'Harsh','harsh@gmail.com','Finance',66000,31,'Delhi','2020-08-08'),
(34,'Isha','isha@gmail.com','HR',39000,25,'Nashik','2021-10-10'),
(35,'Jay','jay@gmail.com','IT',54000,26,'Mumbai','2023-04-04');

SELECT*FROM employees_data;

-- for count function
SELECT COUNT(*) FROM employees_data WHERE salary >=50000;
-- min max
SELECT MIN(salary) AS min_salary, MAX(salary) AS max_salary FROM employees_data;
SELECT SUM(salary) AS total_sal FROM employees_data;
SELECT AVG(salary) AS total_sal FROM employees_data;
select*from employees_data;

SELECT department,AVG(salary) AS avg_salary FROM employees_data GROUP BY department;

SELECT id,department,LOWER(name) AS LOWER, CONCAT(LOWER(name),"0611") AS username,LENGTH(name) AS name_len, NOW() AS time FROM employees_data; 