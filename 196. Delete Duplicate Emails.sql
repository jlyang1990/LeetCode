# Write your MySQL query statement below
DELETE FROM Person
WHERE Id NOT IN
(SELECT * FROM
(SELECT MIN(Id)
FROM Person
GROUP BY Email) P2)