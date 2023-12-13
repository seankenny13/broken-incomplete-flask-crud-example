-- Create user and grant privileges
CREATE USER 'A'@'%' IDENTIFIED BY 'B';
GRANT ALL PRIVILEGES ON *.* TO 'A'@'%';

-- Create and use the database
CREATE DATABASE IF NOT EXISTS student;
USE student;

-- Create students table
CREATE TABLE IF NOT EXISTS students (
    studentID INT AUTO_INCREMENT PRIMARY KEY,
    studentName VARCHAR(255),
    email VARCHAR(255)
);

-- Insert sample data
INSERT INTO students (studentName, email) VALUES 
    ("first student", "firststudent@mydomain.ie"),
    ("second student", "secondstudent@mydomain.ie");

-- Select data from students table
SELECT * FROM students;

