-- In the Company table, the statement that changes the name of “Urban
-- Outfitters, Inc.” to “Urban Outfitters” 

select * from company;
update company set CompanyName = 'Urban Outfitters' where CompanyName = 'Skyline Pvt Ltd'