CREATE TABLE employee1(
    ENO INTEGER,
    NAME TEXT,
    CITY TEXT,
    SALARY INTEGER,
    POST TEXT,
    COUNTRY TEXT
);

INSERT INTO employee1(ENO,NAME,CITY,SALARY,POST,COUNTRY) VALUES
(1,'Arjun','Bangalore',2500,'Worker','India'),
(2,'Eurtheseus','Sparta',5400,'Manager','Greece'),
(3,'James','York',25000,'Regional Officer','UK'),
(4,'Menshikov','St. Petersburg',3800,'CBO','Russia'),
(5,'Ronald','New York',100000,'CEO','USA');

SELECT * FROM employee1;