use SqlAssessments;

-- 1. Execute a query to retrieve the first 20 records from the orders table to verify data ingestion
select 
	orderDate,
	orderID 
from superstore 
limit 20;

-- 2. Select Order ID, Order Date, Sales, and Profit, applying a column alias to display Sales as Total_Sales.
select
	orderID,
	orderDate,
	Sales as Total_Sales,
	Profit 
from superstore;

-- 3. Filter the dataset to isolate all high-value transactions where the Sales figure exceeds 5000.
select * from superstore where Sales > 5000;

-- 4.  Generate a report of the top 10 most profitable orders by sorting the records by Profit in descending order
select * from superstore order by Profit desc limit 10;


