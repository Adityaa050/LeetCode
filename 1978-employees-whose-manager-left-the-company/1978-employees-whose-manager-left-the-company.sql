SELECT a.employee_id
FROM employees a
LEFT JOIN employees b
ON a.manager_id = b.employee_id
WHERE a.salary < 30000
AND a.manager_id IS NOT NULL
AND b.employee_id IS NULL
ORDER BY a.employee_id;