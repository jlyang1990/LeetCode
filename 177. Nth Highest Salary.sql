CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      SELECT E1.Salary
      FROM
        (SELECT DISTINCT Salary
        FROM Employee) E1
      WHERE
        (SELECT count(*)
        FROM
          (SELECT DISTINCT Salary
          FROM Employee) E2
        WHERE E2.Salary >= E1.Salary
        ) = N
  );
END