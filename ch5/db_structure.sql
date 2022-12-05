# pp 77 - 78

CREATE TABLE emps (
 empno INT NOT NULL,
 empname VARCHAR(50),
 job VARCHAR(30),
 PRIMARY KEY (empno)
);
CREATE TABLE salary (
 empno INT NOT NULL,
 salary INT,
 PRIMARY KEY (empno)
);
ALTER TABLE salary ADD FOREIGN KEY (empno) REFERENCES emps (empno);
CREATE TABLE orders (
 pono INT NOT NULL,
 empno INT NOT NULL,
 total INT,
 PRIMARY KEY (pono),
 FOREIGN KEY (empno) REFERENCES emps (empno)
);
CREATE TABLE stocks(
 ticker VARCHAR(10),
 date VARCHAR(10),
 price DECIMAL(15,2)
);
