# Write your MySQL query statement below
# method 1
SELECT C.Name AS Customers
FROM Customers C
LEFT JOIN Orders O
ON C.Id = O.CustomerId
WHERE O.CustomerId IS NULL

# method 2
SELECT Name AS Customers
FROM Customers
WHERE Id NOT IN
(SELECT CustomerId FROM Orders)