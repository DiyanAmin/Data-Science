CREATE TABLE Winners(
    Year INTEGER,
    Subject TEXT,
    Name TEXT,
    Country TEXT,
    Category TEXT
);

INSERT INTO Winners(Year,Subject,Name,Country,Category) VALUES
(1970,'Physics','Hannes Alfven','Sweden','Scientist'),
(1970,'Physics','Louis Neel','France','Scientist'),
(1971,'Physics','Paul','France','Scientist'),
(1971,'Chemistry','Hamilton','Sweden','Linguist'),
(1972,'Literature','Bernard Kelson','Germany','Economist'),
(1972,'Economics','Joseph','Russia','Economist'),
(1973,'Biology','Philips','USA','Prime Minister'),
(1980,'Biology','Martin','USA','President'),
(1981,'Physiology','Hannah','Hungary','Scientist'),
(1975,'Physics','Peter','Chile','Scientist');

SELECT * FROM Winners WHERE SUBJECT NOT LIKE 'P%';