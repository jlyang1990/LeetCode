# Write your MySQL query statement below
SELECT DISTINCT L1.Num AS ConsecutiveNums
FROM Logs L1
JOIN Logs L2
ON L1.Id = L2.Id - 1
AND L1.Num = L2.Num
JOIN Logs L3
ON L1.Id = L3.Id - 2
AND L1.Num = L3.Num