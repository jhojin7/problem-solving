select sum(g.score) as score,g.emp_no,  e.emp_name, e.position, e.email
from hr_grade g
join hr_employees e
on g.emp_no = e.emp_no
where g.year=2022
group by g.emp_no, g.year
order by sum(g.score) desc
limit 1