CREATE TABLE Customers(
    C_No INTEGER,
    C_Name TEXT,
    C_City TEXT,
    C_Grade INTEGER
);

INSERT INTO Customers(C_No,C_Name,C_City,C_Grade) VALUES
(1,'John','San Francisco',98),
(2,'Joanna','Ohio',103),
(3,'Jonas','New York',100),
(4,'Jonathan','New York',124),
(5,'Jones','Washington D.C.',76);

SELECT * FROM Customers;

--New York or Grade>100,
SELECT * FROM Customers WHERE C_City='New York' OR C_Grade>=100;

--New York AND Grade>100,
SELECT * FROM Customers WHERE C_City='New York' AND C_Grade>=100;