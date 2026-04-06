# Write your MySQL query statement below
select y.product_name, x.year, x.price
from sales as x
left join product as y
on x.product_id = y.product_id