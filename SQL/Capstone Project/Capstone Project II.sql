CREATE TABLE RESTAURANT(
    NAME TEXT,
    NEIGHBOURHOOD TEXT,
    CUISINE TEXT,
    REVIEW REAL,
    PRICE TEXT,
    HEALTH TEXT
);

INSERT INTO RESTAURANT(NAME,NEIGHBOURHOOD,CUISINE,REVIEW,PRICE,HEALTH) VALUES
('Peter','Brooklyn','Steak',4.4,'$$$$','A'),
('Jongro','Midtown','Korean',3.5,'$$','A'),
('Pocha','Midtown','Pizza',4.0,'$$','B'),
('Lighthouse','Queens','Chinese',3.9,'$','A'),
('Minca','Downtown','American',4.6,'$$$',''),
('Marea','Chinatown','Chinese',3.0,'$$',''),
('Dirty Candy','Uptown','Italian',4.9,'$$$$','B'),
('Di Fara Pizza','Brooklyn','Pizza',3.8,'$$','A'),
('Glden Unicorn','Uptown','Italian',3.8,'$$','A');

SELECT DISTINCT NEIGHBOURHOOD FROM RESTAURANT;

SELECT DISTINCT CUISINE FROM RESTAURANT;

SELECT * FROM RESTAURANT WHERE CUISINE = 'Chinese';

SELECT * FROM RESTAURANT WHERE REVIEW >= 4.0;

SELECT * FROM RESTAURANT WHERE CUISINE = 'Italian' AND PRICE IN ('$$','$$$');

SELECT * FROM RESTAURANT WHERE PRICE = '$$$';

SELECT * FROM RESTAURANT WHERE NAME LIKE '%Candy%';

SELECT * FROM RESTAURANT WHERE NEIGHBOURHOOD IN ('Midtown','Downtown','Chinatown');

SELECT * FROM RESTAURANT WHERE HEALTH = '' OR HEALTH IS NULL;

SELECT * FROM RESTAURANT ORDER BY REVIEW DESC LIMIT 4;