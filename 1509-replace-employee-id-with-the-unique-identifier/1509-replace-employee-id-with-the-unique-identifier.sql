# Write your MySQL query statement below
select e.unique_id, s.name
from Employees as s
left join EmployeeUNI as e
    on s.id = e.id