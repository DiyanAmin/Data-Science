CREATE TABLE supplier1(
    SNO TEXT,
    SNAME TEXT,
    STATUS INTEGER,
    CITY TEXT
);

INSERT INTO supplier1(SNO,SNAME,STATUS,CITY) VALUES
('S1','Smith',20,'London'),
('S2','Jones',10,'Paris'),
('S3','Blake',30,'Paris'),
('S4','Clarke',20,'London'),
('S5','Adams',30,'Athens');

SELECT * FROM supplier1;