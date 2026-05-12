-- 6) In ContactEmployee table, the statement that removes Dianne Connor’s contact
-- event with Jack Lee (one statement).
-- HINT: Use the primary key of the ContactEmployee table to specify the correct record to remove.

select * from contactemployee;
delete ce from ContactEmployee as ce join Employee as e on ce.ContactEmployeeId = e.EmployeeId;