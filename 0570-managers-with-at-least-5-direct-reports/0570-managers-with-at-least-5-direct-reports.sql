# Write your MySQL query statement below
select b.name
from employee a
join employee b
on a.managerid = b.id
group by b.id
having count(*) >= 5