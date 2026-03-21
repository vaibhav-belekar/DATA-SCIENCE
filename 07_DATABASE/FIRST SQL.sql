CREATE DATABASE startersql;
USE startersql;

CREATE TABLE user(
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100) NOT NULL,
email VARCHAR(100) UNIQUE NOT NULL,
gender ENUM('male','Female','Other'),
date_of_birth DATE,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

SELECT*FROM user;




