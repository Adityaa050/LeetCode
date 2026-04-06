# Write your MySQL query statement below
select x.customer_id, count(*) as count_no_trans
from visits as x
left join transactions as y
on x.visit_id = y.visit_id
where y.visit_id is null
group by x.customer_id