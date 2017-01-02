# Write your MySQL query statement below
SELECT D.Name AS Department, E3.Name AS Employee, E3.Salary AS Salary
FROM Department D
JOIN
    (SELECT E1.Name, E1.Salary, E1.DepartmentId
    FROM Employee E1
    WHERE
        (SELECT count(*)
        FROM
            (SELECT DISTINCT Salary, DepartmentId
            FROM Employee) E2
        WHERE E2.Salary >= E1.Salary
        AND E2.DepartmentId = E1.DepartmentId
        ) <= 3
    ) E3
ON D.Id = E3.DepartmentId