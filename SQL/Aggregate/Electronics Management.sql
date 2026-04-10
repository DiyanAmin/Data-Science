CREATE TABLE Electronics(
    Product_ID TEXT,
    Product_Name TEXT,
    Brand TEXT,
    Category TEXT,
    Stock INTEGER,
    Price REAL
);

INSERT INTO Electronics(Product_ID,Product_Name,Brand,Category,Stock,Price) VALUES
('E1','Smartphone','Samsung','Mobile',50,25000),
('E2','Laptop','Dell','Computer',30,55000),
('E3','Headphones','Sony','Accessories',100,2000),
('E4','Smartwatch','Apple','Wearble',20,30000),
('E5','Tablet','Lenovo','Computer',25,18000);


SELECT COUNT(Product_ID) AS Total_Products FROM Electronics;

SELECT AVG(Price) AS Avg_Price FROM  Electronics;

SELECT SUM(Price) AS Total_Price FROM Electronics;

SELECT Product_Name,MAX(Price) AS Highest_Price FROM Electronics;

SELECT Product_Name,Stock FROM Electronics WHERE Stock < 30;

SELECT Category, COUNT(*) AS Product_Count FROM Electronics GROUP BY Category;