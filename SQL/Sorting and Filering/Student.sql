CREATE TABLE Students(
    Student_ID INTEGER,
    Name TEXT,
    Department TEXT,
    Marks INTEGER,
    City TEXT
);

INSERT INTO Students(Student_ID,Name,Department,Marks,City) VALUES
(1,'Arun','Computer Science',85,'Chennai'),
(2,'Priya','Mathematics',78,'Erode'),
(3,'Rahul','Physics',92,'Coimbatore'),
(4,'Divya','Chemistry',88,'Madurai'),
(5,'Karthik','Biology',67,'Salem'),
(6,'Sneha','Computer Science',95,'Trichy'),
(7,'Vikram','Mathematics',73,'Erode'),
(8,'Anjali','Physics',81,'Chennai');

SELECT * FROM Students;

SELECT * FROM Students WHERE Marks > 80;

SELECT * FROM Students WHERE City = 'Erode';

SELECT * FROM Students WHERE Department NOT LIKE 'P%';

SELECT COUNT(*) AS 'Total Students' FROM Students;

SELECT AVG(Marks) AS 'Average Marks' FROM Students;

SELECT MAX(Marks) AS 'Highest Marks' FROM Students;

SELECT * FROM Students ORDER BY Marks DESC;