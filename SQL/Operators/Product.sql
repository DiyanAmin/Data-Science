CREATE TABLE IF NOT EXISTS Products(
    Product_ID INTEGER PRIMARY KEY,
    Product_Name TEXT,
    Product_Price INTEGER,
    Product_Commission INTEGER
);

INSERT INTO Products(Product_ID,Product_Name,Product_Price,Product_Commission) VALUES
(101,'Mother Board',3200,15),
(102,'Keyboard',450,16),
(103,'Zip Drive',250,14),
(104,'Speaker',550,16),
(105,'Monitor',5000,11),
(106,'DVD Drive',900,12),
(106,'CD Drive',800,12),
(108,'Printer',2600,13),
(109,'Refill Cartridge',350,13),
(110,'Mouse',250,12);

SELECT Product_Name,Product_Price FROM Products WHERE Product_Price=(SELECT MIN(Product_Price) FROM Products);
SELECT Product_Name,Product_Price FROM Products WHERE Product_Price=(SELECT MAX(Product_Price) FROM Products); 