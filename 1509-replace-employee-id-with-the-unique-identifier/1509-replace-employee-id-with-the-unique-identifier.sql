# Write your MySQL query statement below
select r.unique_id, l.name
from EmployeeUNI as r
right join Employees as l
    on l.id = r.id