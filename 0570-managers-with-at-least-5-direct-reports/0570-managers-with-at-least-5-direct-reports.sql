# Write your MySQL query statement below
select b.name
from employee a
join employee b
on a.managerid = b.id
group by a.managerid
having count(*) >= 5