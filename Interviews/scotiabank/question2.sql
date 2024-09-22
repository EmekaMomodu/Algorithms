SELECT
    d.dept_id,
    COUNT(e.emp_id) AS num_employees,
    SUM(e.salary) AS total_salary
FROM department d LEFT JOIN employee e ON d.dept_id = e.dept_id
GROUP BY d.dept_id
HAVING COUNT(e.emp_id) > 0
ORDER BY d.dept_id;