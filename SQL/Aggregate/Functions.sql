CREATE TABLE IF NOT EXISTS PRODUCTS(
    PID INTEGER,
    PName TEXT,
    SID INTEGER,
    CID INTEGER,
    Unit TEXT,
    PReal INTEGER
);

INSERT INTO PRODUCTS(PID,PName,SID,CID,Unit,PReal) VALUES
(1,'Chais',1,1,'10 Boxes*20 Bags',18),
(2,'Chang',1,1,'24-14 Oz Bottles',19),
(3,'Aniseed Syrup',1,2,'12-550 ML Bottles',10),
(4,'Chef Anton Seasoning',2,2,'48-6 Oz Jars',22),
(5,'Chef Anton Mix',2,2,'36 Boxes',21.35);

SELECT COUNT(PID) AS Product_Count FROM PRODUCTS;

SELECT AVG(PReal) AS Avg_Price FROM PRODUCTS;

SELECT SUM(PReal) AS Total_Price FROM PRODUCTS;