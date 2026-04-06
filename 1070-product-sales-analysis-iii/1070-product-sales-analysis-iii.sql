# Write your MySQL query statement below
select a.product_id, a.year as first_year, a.quantity, a.price
from sales a
join (
    select product_id, min(year) as first_year
    from sales
    group by product_id
) b
where a.product_id = b.product_id and a.year = b.first_year