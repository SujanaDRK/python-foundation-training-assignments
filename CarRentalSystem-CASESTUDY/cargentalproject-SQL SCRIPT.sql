CREATE DATABASE IF NOT EXISTS CarRentalDB;
USE CarRentalDB;

CREATE TABLE Vehicle (
    vehicleID INT PRIMARY KEY AUTO_INCREMENT,
    make VARCHAR(50),
    model VARCHAR(50),
    year INT,
    dailyRate DECIMAL(10, 2),
    status VARCHAR(20),
    passengerCapacity INT,
    engineCapacity DECIMAL(5, 2)
);

CREATE TABLE Customer (
    customerID INT PRIMARY KEY AUTO_INCREMENT,
    firstName VARCHAR(50),
    lastName VARCHAR(50),
    email VARCHAR(100),
    phoneNumber VARCHAR(15)
);

CREATE TABLE Lease (
    leaseID INT PRIMARY KEY AUTO_INCREMENT,
    vehicleID INT,
    customerID INT,
    startDate DATE,
    endDate DATE,
    type VARCHAR(20),
    FOREIGN KEY (vehicleID) REFERENCES Vehicle(vehicleID),
    FOREIGN KEY (customerID) REFERENCES Customer(customerID)
);

CREATE TABLE Payment (
    paymentID INT PRIMARY KEY AUTO_INCREMENT,
    leaseID INT,
    paymentDate DATE,
    amount DECIMAL(10, 2),
    FOREIGN KEY (leaseID) REFERENCES Lease(leaseID)
);

INSERT INTO Vehicle (make, model, year, dailyRate, status, passengerCapacity, engineCapacity)
VALUES
('Toyota', 'Camry', 2020, 1500.00, 'available', 5, 2.5),
('Hyundai', 'i20', 2022, 1200.00, 'available', 5, 1.2),
('Honda', 'City', 2019, 1400.00, 'notAvailable', 5, 1.5),
('Mahindra', 'XUV500', 2021, 2000.00, 'available', 7, 2.2),
('Maruti', 'Swift', 2018, 1000.00, 'notAvailable', 5, 1.2),
('Tata', 'Harrier', 2023, 2200.00, 'available', 5, 2.0),
('Ford', 'EcoSport', 2017, 1300.00, 'available', 5, 1.5),
('Kia', 'Seltos', 2021, 2100.00, 'available', 5, 1.4),
('Renault', 'Kwid', 2016, 900.00, 'notAvailable', 4, 0.8),
('Volkswagen', 'Polo', 2020, 1350.00, 'available', 5, 1.2);

INSERT INTO Customer (firstName, lastName, email, phoneNumber)
VALUES
('Ravi', 'Kumar', 'ravi.kumar@example.com', '9876543210'),
('Anjali', 'Sharma', 'anjali.sharma@example.com', '9988776655'),
('Suresh', 'Naidu', 'suresh.naidu@example.com', '9123456780'),
('Meera', 'Raj', 'meera.raj@example.com', '9812345678'),
('Rahul', 'Verma', 'rahul.verma@example.com', '9977886655'),
('Kavya', 'Menon', 'kavya.menon@example.com', '9797979797'),
('Ajay', 'Reddy', 'ajay.reddy@example.com', '9123987456'),
('Divya', 'Singh', 'divya.singh@example.com', '9001234567'),
('Manoj', 'Patil', 'manoj.patil@example.com', '9612345890'),
('Sneha', 'Jain', 'sneha.jain@example.com', '9870001112');

INSERT INTO Lease (vehicleID, customerID, startDate, endDate, type)
VALUES
(1, 1, '2025-06-01', '2025-06-05', 'Daily'),
(2, 2, '2025-06-03', '2025-07-03', 'Monthly'),
(4, 3, '2025-05-20', '2025-06-20', 'Monthly'),
(5, 4, '2025-06-01', '2025-06-10', 'Daily'),
(6, 5, '2025-06-05', '2025-06-15', 'Daily'),
(7, 6, '2025-06-06', '2025-06-16', 'Daily'),
(8, 7, '2025-06-02', '2025-07-02', 'Monthly'),
(9, 8, '2025-05-30', '2025-06-04', 'Daily'),
(3, 9, '2025-06-08', '2025-06-28', 'Monthly'),
(10, 10, '2025-06-01', '2025-06-06', 'Daily');

INSERT INTO Payment (leaseID, paymentDate, amount)
VALUES
(1, '2025-06-01', 7500.00),
(2, '2025-06-03', 36000.00),
(3, '2025-05-20', 42000.00),
(4, '2025-06-01', 10000.00),
(5, '2025-06-05', 11000.00),
(6, '2025-06-06', 12000.00),
(7, '2025-06-02', 42000.00),
(8, '2025-05-30', 5000.00),
(9, '2025-06-08', 32000.00),
(10, '2025-06-01', 8000.00);

-- 1. customer management 

INSERT INTO Customer (firstName, lastName, email, phoneNumber)
VALUES ('Nikhil', 'Mehta', 'nikhil.mehta@example.com', '9876500011');

UPDATE Customer
SET email = 'newemail.nikhil@example.com'
WHERE customerID = 11;

SELECT * FROM Customer WHERE customerID = 11;

-- 2. vehicle management

INSERT INTO Vehicle (make, model, year, dailyRate, status, passengerCapacity, engineCapacity)
VALUES ('Skoda', 'Rapid', 2021, 1600.00, 'available', 5, 1.6);

UPDATE Vehicle
SET status = 'notAvailable'
WHERE vehicleID = 11;

SELECT * FROM Vehicle WHERE vehicleID = 11;

-- 3. lease management 

INSERT INTO Lease (vehicleID, customerID, startDate, endDate, type)
VALUES (11, 11, '2025-06-15', '2025-06-19', 'Daily');

SELECT 
    V.dailyRate * DATEDIFF(L.endDate, L.startDate) AS totalLeaseCost
FROM 
    Lease L
JOIN 
    Vehicle V ON L.vehicleID = V.vehicleID
WHERE 
    L.leaseID = 11;
    
-- 4. payment handling 

-- a) Record a new payment
INSERT INTO Payment (leaseID, paymentDate, amount)
VALUES (11, '2025-06-15', 6400.00);

-- b) Retrieve payment history for a specific customer (e.g., customerID = 1)
SELECT P.paymentID, P.paymentDate, P.amount, C.firstName, C.lastName
FROM Payment P
JOIN Lease L ON P.leaseID = L.leaseID
JOIN Customer C ON L.customerID = C.customerID
WHERE C.customerID = 1;

-- c) Calculate total revenue from all payments
SELECT SUM(amount) AS totalRevenue FROM Payment;

-- 5. LIST AVAILABLE CARS

SELECT * FROM Vehicle WHERE status = 'available';

-- 6. LIST RENTED CARS (currently under lease)

SELECT V.*
FROM Vehicle V
JOIN Lease L ON V.vehicleID = L.vehicleID
WHERE CURDATE() BETWEEN L.startDate AND L.endDate;

-- 7. FIND CAR BY ID

SELECT * FROM Vehicle WHERE vehicleID = 5;

-- 8. FIND CUSTOMER BY ID

SELECT * FROM Customer WHERE customerID = 4;

-- 9. LIST ALL CUSTOMERS

SELECT * FROM Customer;

-- 10. LIST ACTIVE LEASES

SELECT * FROM Lease
WHERE CURDATE() BETWEEN startDate AND endDate;

-- 11. LIST LEASE HISTORY (completed leases)

SELECT * FROM Lease
WHERE endDate < CURDATE();

-- 12. RETURN CAR (update vehicle status + end lease)

-- a) Set vehicle status to 'available' on return
UPDATE Vehicle
SET status = 'available'
WHERE vehicleID = (
    SELECT vehicleID FROM Lease WHERE leaseID = 3
);

-- b) Optional: Update lease end date to current date if returned early
UPDATE Lease
SET endDate = CURDATE()
WHERE leaseID = 3;

SELECT * FROM Customer;
SELECT * FROM Vehicle;
SELECT * FROM Lease;







