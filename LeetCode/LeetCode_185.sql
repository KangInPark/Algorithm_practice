select Department, Employee, Salary 
from (select b.name as Department, a.name as Employee, a.salary as Salary, DENSE_RANK() over(partition by a.departmentId order by a.salary desc) as num from employee as a join department as b on a.departmentId = b.id) as t
where num <= 3