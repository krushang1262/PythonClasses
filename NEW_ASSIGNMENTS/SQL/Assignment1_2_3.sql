create table Company(
	CompanyId int primary key,
    CompanyName varchar(45),
    Street varchar(45),
    City varchar(45),
    State varchar(2),
    Zip varchar(10)
);

create table Contact(
	ContactId INT primary key, 
    CompanyId int not null, foreign key (CompanyId) references Company(CompanyId),
    Firstname varchar(45),
	Lasttname varchar(45),
    Street varchar(45),
    City varchar(45),
    State varchar(2),
    Zip varchar(10),
    IsMain boolean,
	Email varchar(45),
    Phone varchar(12)
);

create table Employee(
	EmployeeId INT primary key, 
	Firstname varchar(45),
	Lasttname varchar(45),
    Salary Decimal(10, 2),
    HireDate Date,
    JobTitle varchar(25),
    Email varchar(45),
    Phone varchar(12)
);

create table ContactEmployee(
	ContactEmployeeId INT primary key, 
    ContactId int not null, foreign key (ContactId) references Contact(ContactId),
    EmployeeId int not null, foreign key(EmployeeId) references Employee(EmployeeId),
    ContactDate Date,
	Description varchar(100)
);

INSERT INTO Company (CompanyId, CompanyName, Street, City, State, Zip) VALUES
(1, 'Tech Solutions', '12 Park Street', 'Ahmedabad', 'GJ', '380001'),
(2, 'Bright Future', '45 CG Road', 'Surat', 'GJ', '395003'),
(3, 'Skyline Pvt Ltd', '78 Ring Road', 'Vadodara', 'GJ', '390001');

INSERT INTO Contact (ContactId, CompanyId, Firstname, Lasttname, Street, City, State, Zip, IsMain, Email, Phone) VALUES
(1, 1, 'Rahul', 'Sharma', '12 Park Street', 'Ahmedabad', 'GJ', '380001', TRUE, 'rahul@gmail.com', '9876543210'),
(2, 1, 'Neha', 'Patel', '15 River Road', 'Ahmedabad', 'GJ', '380002', FALSE, 'neha@gmail.com', '9876543211'),
(3, 2, 'Amit', 'Verma', '45 CG Road', 'Surat', 'GJ', '395003', TRUE, 'amit@gmail.com', '9876543212'),
(4, 3, 'Priya', 'Mehta', '78 Ring Road', 'Vadodara', 'GJ', '390001', TRUE, 'priya@gmail.com', '9876543213');

INSERT INTO Employee(EmployeeId, Firstname, Lasttname, Salary, HireDate, JobTitle, Email, Phone)VALUES
(1, 'Karan', 'Joshi', 45000.00, '2022-01-15', 'Developer', 'karan@gmail.com', '9876500001'),
(2, 'Riya', 'Shah', 55000.00, '2021-06-20', 'Manager', 'riya@gmail.com', '9876500002'),
(3, 'Vikas', 'Patel', 40000.00, '2023-03-10', 'Tester', 'vikas@gmail.com', '9876500003'),
(4, 'Sneha', 'Desai', 60000.00, '2020-11-05', 'HR', 'sneha@gmail.com', '9876500004');

INSERT INTO ContactEmployee(ContactEmployeeId, ContactId, EmployeeId, ContactDate, Description) VALUES
(1, 1, 2, '2024-01-10', 'Project discussion'),
(2, 2, 1, '2024-02-15', 'Software support'),
(3, 3, 3, '2024-03-20', 'Testing requirements'),
(4, 4, 4, '2024-04-05', 'HR meeting');