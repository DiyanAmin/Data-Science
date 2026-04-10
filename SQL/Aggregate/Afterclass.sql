CREATE TABLE Employees(
    ID INTEGER,
    Name TEXT,
    Salary INTGER
);

INSERT INTO Employees(ID,Name,Salary) VALUES
(1,'Vickram',1000000),
(2,'Vickram',1500000),
(3,'Vickram',890000),
(4,'Vickram',6400000),
(5,'Vickram',2500000),
(6,'Vickram',6800000),
(7,'Vickram',3000000),
(8,'Vickram',4000000),
(9,'Vickram',4440000),
(10,'Vickram',3330000);

SELECT * FROM Employees;

SELECT SUM(Salary) AS Total_Salary FROM Employees;

SELECT AVG(Salary) AS Avg_Salary FROM Employees;

SELECT MAX(Salary) AS Highest_Salary FROM Employees;
SELECT MIN(Salary) AS Lowest_Salary FROM Employees;
