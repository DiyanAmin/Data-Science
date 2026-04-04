CREATE TABLE student1(
    SID INTEGER PRIMARY KEY,
    NAME TEXT,
    AGE INTEGER,
    CITY TEXT
);

CREATE TABLE mark1(
    SID INTEGER,
    SUBJECT TEXT,
    SCORE INTEGER,
    FOREIGN KEY(SID) REFERENCES student1(sid)
);

INSERT INTO student1(SID,NAME,AGE,CITY) VALUES
(1,'Arun',20,'Chennai'),
(2,'Priya',21,'Coimbatore'),
(3,'Karthik',19,'Madurai'),
(4,'Divya',22,'Salem'),
(5,'Rahul',20,'Erode');

INSERT INTO mark1(SID,SUBJECT,SCORE) VALUES
(1,'Maths',85),
(1,'Science',78),
(1,'English',90),

(2,'Maths',88),
(2,'Science',92),
(2,'English',81),

(3,'Maths',70),
(3,'Science',65),
(3,'English',75),

(4,'Maths',95),
(4,'Science',89),
(4,'English',93),

(5,'Maths',60),
(5,'Science',72),
(5,'English',68);

SELECT * from student1;
SELECT * from mark1;