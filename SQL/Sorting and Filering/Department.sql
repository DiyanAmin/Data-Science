CREATE TABLE Department(
    Employee_ID INTEGER,
    Name TEXT,
    Department_ID INTEGER,
    Manager_ID INTGER,
    Salary INTEGER
);

INSERT INTO Department(Employee_ID,Name,Department_ID,Manager_ID,Salary) VALUES
(100,'Steven King',90,100,24000),
(101,'Neene Kochcar',90,100,17000),
(102,'Lex Dehaan',90,102,9000),
(103,'Bruce Lee',60,103,48000),
(104,'Diana Wills',60,103,25000),
(105,'Valli Pator',50,100,42000),
(1973,'Luv Hami',60,102,5000),
(106,'David Austin',90,100,6000);

SELECT Department_ID AS 'Department Code', COUNT(*) AS 'No. of Employees' FROM Department GROUP BY Department_ID;

SELECT Department_ID AS 'Department Code', SUM(Salary) AS 'Total Salary' FROM Department WHERE Manager_ID = 103 GROUP BY Department_ID;

SELECT Department_ID, COUNT(*) AS 'No. of Employees' FROM Department GROUP BY Department_ID HAVING COUNT(*) > 2;