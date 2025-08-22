USE online_retail;

CREATE TABLE customers (
    CustomerID INT PRIMARY KEY,
    Country VARCHAR(100)
);

CREATE TABLE products (
    StockCode VARCHAR(20) PRIMARY KEY,
    Description VARCHAR(255)
);

CREATE TABLE invoices (
    InvoiceNo VARCHAR(20) PRIMARY KEY,
    InvoiceDate DATETIME,
    CustomerID INT,
    FOREIGN KEY (CustomerID) REFERENCES customers(CustomerID)
);


drop table if exists orders;
SHOW VARIABLES LIKE 'local_infile';

CREATE TABLE orders (
    InvoiceNo VARCHAR(20),
    StockCode VARCHAR(20),
    Quantity INT,
    UnitPrice DECIMAL(10, 2),
    TotalPrice DECIMAL(10, 2)
);

SHOW VARIABLES LIKE 'secure_file_priv';
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 9.4/Uploads/orders.csv'
INTO TABLE orders
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

SELECT COUNT(*) FROM orders;
SELECT COUNT(*) FROM invoices;
SELECT COUNT(*) FROM products;
SELECT COUNT(*) FROM customers;

select * from orders limit 

ALTER TABLE orders
ADD CONSTRAINT fk_invoice FOREIGN KEY (InvoiceNo) REFERENCES invoices(InvoiceNo),
ADD CONSTRAINT fk_stock FOREIGN KEY (StockCode) REFERENCES products(StockCode);

SELECT 
    DATE_FORMAT(i.InvoiceDate, '%Y-%m') AS Month,
    p.Description AS Product,
    SUM(o.Quantity) AS TotalQuantity,
    SUM(o.TotalPrice) AS TotalRevenue
FROM orders o
JOIN products p ON o.StockCode = p.StockCode
JOIN invoices i ON o.InvoiceNo = i.InvoiceNo
GROUP BY Month, Product
ORDER BY Month, TotalRevenue DESC;

SELECT 
    CONCAT(YEAR(i.InvoiceDate), '-Q', QUARTER(i.InvoiceDate)) AS Quarter,
    p.Description AS Product,
    SUM(o.Quantity) AS TotalQuantity,
    SUM(o.TotalPrice) AS TotalRevenue
FROM orders o
JOIN products p ON o.StockCode = p.StockCode
JOIN invoices i ON o.InvoiceNo = i.InvoiceNo
GROUP BY Quarter, Product
ORDER BY Quarter, TotalRevenue DESC;

SELECT 
    p.Description AS Product,
    SUM(o.Quantity) AS TotalQuantity,
    SUM(o.TotalPrice) AS TotalRevenue
FROM orders o
JOIN products p ON o.StockCode = p.StockCode
GROUP BY Product
ORDER BY TotalRevenue DESC
LIMIT 10;

SELECT 
    c.Country,
    p.Description AS Product,
    SUM(o.TotalPrice) AS TotalRevenue,
    SUM(o.Quantity) AS TotalQuantity
FROM orders o
JOIN products p ON o.StockCode = p.StockCode
JOIN invoices i ON o.InvoiceNo = i.InvoiceNo
JOIN customers c ON i.CustomerID = c.CustomerID
GROUP BY c.Country, Product
ORDER BY c.Country, TotalRevenue DESC;
