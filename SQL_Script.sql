CREATE TABLE cat_reg AS
Select category AS Category,
       CAST(SUM(totalprice) FILTER (WHERE region = 'East') AS integer) AS East,
       CAST(SUM(totalprice) FILTER (WHERE region = 'West') AS integer) AS West,
       CAST(SUM(totalprice) As integer) as Grand_Total
FROM food_sales
GROUP BY category
Order By category;