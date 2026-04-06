# Write your MySQL query statement below
select a.name, b.bonus
from employee as a
left join bonus as b
on a.empid = b.empid
where bonus < 1000 or bonus is null