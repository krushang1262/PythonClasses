-- Section C: Mini Project
use sqlassessments;

-- 1.Title: Retail Profitability & Market Segment Analysis

select Segment, 
round(sum(Profit)) as totalProfit,
round(sum(Sales)) as totalSales
 from superstore
 group by Segment
 order by totalSales desc;
 
--  2. Problem Statement: Identify underperforming product categories and regions
-- by analyzing the relationship between discount rates and net profit margins.
select 
	Category,
	Region,
	avg(Discount) as avgDiscountRate,
	sum(Profit) as totalProfits 
from superstore
group by Category,Region
order by totalProfits;

-- 4. Required Deliverables: SQL script for database schema creation,
-- multi-condition filtering queries, aggregated performance report by region,
-- and a summary of loss-making transactions.

select ProductName, Region, sum(Profit) as totalProfit  from superstore where Profit >5000 or Profit <10000
group by ProductName,Region
order by totalProfit desc
limit 10;