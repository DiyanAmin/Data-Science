CREATE TABLE IF NOT EXISTS Student(
    Roll_No TEXT PRIMARY KEY,
    Name TEXT NOT NULL,
    City TEXT,
    Phone NUMBER,
    Age NUMBER
);

INSERT INTO Student(Roll_No,Name,City,Phone,Age) VALUES
(1,'Ram','Delhi',123456789,12),
(2,'Ramesh','Gurgaon',987654321,11),
(3,'Rohan','Rohtak',142515234,10),
(4,'Rahul','Delhi',745285528,10),
(5,'Raj','Delhi',658265926,12),
(6,'Rajesh','Delhi',648744744,11);

SELECT * FROM Student;
SELECT * FROM Student WHERE Age=12 AND City='Delhi';
SELECT * FROM Student WHERE Age=11 AND Name='Ramesh';
SELECT * FROM Student WHERE Name='Rahul' or Name='Raj';
SELECT * FROM Student WHERE Age=10 AND (Name='Rahul' OR Name='Rohan');