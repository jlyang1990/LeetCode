# Write your MySQL query statement below
SELECT D.Name AS Department, E.Name AS Employee, E.Salary AS Salary
FROM Department D, Employee E
WHERE D.Id = E.DepartmentId
AND (SELECT count(*)
    FROM
        (SELECT DISTINCT Salary, DepartmentId
        FROM Employee) E1
    WHERE E1.Salary >= E.Salary
    AND E1.DepartmentId = E.DepartmentId
    ) <= 3