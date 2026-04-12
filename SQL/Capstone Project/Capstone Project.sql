CREATE TABLE Salesman(
    Salesman_ID INTEGER,
    Name TEXT,
    City TEXT,
    Comission REAL
);

INSERT INTO Salesman(Salesman_ID,Name,City,Comission) VALUES
(5001,'James Hoong','New York',0.15),
(5002,'Nail Knite','Paris',0.13),
(5005,'Pit Alex','London',0.11),
(5006,'Mc Lyon','Paris',0.14),
(5007,'Paul Adam','Rome',0.13),
(5003,'Lauson Hen','San Jose',0.12);

CREATE TABLE Customers(
    Customer_ID TEXT,
    Customer_Name TEXT PRIMARY KEY,
    City TEXT,
    Grade TEXT,
    Salesman_ID TEXT
);

INSERT INTO Customers(Customer_ID,Customer_Name,City,Grade,Salesman_ID) VALUES
('3002','Nick Rimando','New York','100','5001'),
('3007','Brad Davis','New York','200','5001'),
('3005','Graham Zusi','California','200','5002'),
('3008','Julian Green','London','300','5002'),
('3004','Fabian Johnson','Paris','300','5006'),
('3009','Geoff Cameron','Berlin','100','5003'),
('3003','Jozy Altidor','Moscow','200','5007'),
('3001','Brad Guzan','London','','5005');

CREATE TABLE ORDERS(
    ORDER_NO TEXT,
    PURCHASE_AMOUNT TEXT,
    ORDER_DATE TEXT,
    CUSTOMER_ID TEXT,
    SALESMAN_ID TEXT
);

INSERT INTO ORDERS(ORDER_NO,PURCHASE_AMOUNT,ORDER_DATE,CUSTOMER_ID,SALESMAN_ID) VALUES
('70001','150.5','2012-10-05','3005','5002'),
('70009','270.65','2012-09-10','3001','5002'),
('70002','65.26','2012-10-05','3002','5003'),
('70004','110.5','2012-08-17','3009','5007'),
('70007','948.5','2012-09-10','3005','5005'),
('70005','2400.6','2012-07-27','3007','5006');

SELECT Customers.Customer_Name,Salesman.Name,Salesman.City FROM Customer JOIN Salesman ON Customer.City = Salesman.City;

SELECT Customer.Customer_Name,Salesman_Name FROM Customers JOIN Salesman ON Customers.Salesman_ID = Salesman.Salesman_ID;

SELECT ORDERS.ORDER_NO,Customers.Customer_Name,ORDERS.CUSTOMER_ID,ORDERS.SALESMAN_ID FROM ORDERS JOIN Customers ON ORDERS.CUSTOMER_ID = Customers.Customer_ID JOIN Salesman ON ORDERS.SALESMAN_ID = Salesman.Salesman_ID WHERE Customers.City <> Salesman.City;

SELECT ORDERS.ORDER_NO,Customers.Customer_Name FROM ORDERS JOIN Customers ON ORDERS.CUSTOMER_ID = Customers.Customer_ID;

SELECT Customers.Customer_Name AS 'Customer',Customer.Grade AS 'Grade' FROM ORDERS JOIN Salesman ON ORDERS.SALESMAN_ID = Salesman.Salesman_ID JOIN Customers ON ORDERS.CUSTOMER_ID = Customer.Customer_ID WHERE Customer.Grade IS NOT NULL;

SELECT Customer.Customer_Name AS 'Customer',Customer.City AS 'City',Salesman.Name AS 'Salesman', Salesman.Comission FROM Customers JOIN Salesman ON Customer.Salesman_ID =  Salesman.Salesman_ID WHERE Salesman .Comission BETWEEN 