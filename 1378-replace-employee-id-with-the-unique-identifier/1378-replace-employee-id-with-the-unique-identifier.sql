# Write your MySQL query statement below
select y.unique_id, x.name
from employees as x
left join employeeUNI as y
on x.id = y.id