# Write your MySQL query statement below
# method 1
SELECT D.Name AS Department, E3.Name AS Employee, E3.Salary AS Salary
FROM Department D
JOIN
	(SELECT E1.Name, E1.Salary, E1.DepartmentID
	FROM Employee E1
	JOIN
		(SELECT MAX(Salary) AS MaxSalary, DepartmentId
		FROM Employee
		GROUP BY DepartmentId
		) E2
	ON E1.DepartmentID = E2.DepartmentID
	AND E1.Salary = E2.MaxSalary
	) E3
ON D.Id = E3.DepartmentId


# method 2
SELECT D.Name AS Department, E.Name AS Employee, E.Salary AS Salary
FROM Department D, Employee E
WHERE D.Id = E.DepartmentId
AND (SELECT COUNT(*)
    FROM
        (SELECT DISTINCT DepartmentId, Salary
        FROM Employee) E1
    WHERE E1.Salary >= E.Salary AND E1.DepartmentId = E.DepartmentId
    ) = 1