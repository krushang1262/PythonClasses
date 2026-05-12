-- Write the SQL SELECT query that displays the names of the employees that
-- have contacted Toll Brothers (one statement). Run the SQL SELECT query in
-- MySQL Workbench. Copy the results below as well. 

SELECT 
    CONCAT(e.Firstname, ' ', e.Lasttname) AS EmployeeName,
    CONCAT(c.Firstname, ' ', c.Lasttname) AS ContactName
FROM Employee AS e
JOIN ContactEmployee AS ce 
    ON e.EmployeeId = ce.EmployeeId
JOIN Contact AS c 
    ON c.ContactId = ce.ContactId;

