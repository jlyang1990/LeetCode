# Write your MySQL query statement below
SELECT T2.Request_at AS Day,
ROUND(SUM(CASE WHEN T2.Status like 'cancelled_by_%' THEN 1 ELSE 0 END) / COUNT(*), 2) AS 'Cancellation Rate'
FROM
    (SELECT T1.Status, T1.Request_at, U.Banned
    FROM Trips T1
    JOIN Users U
    ON T1.Client_Id = U.Users_Id
    AND T1.Request_at BETWEEN '2013-10-01' AND '2013-10-03'
    AND U.Banned = "No"
    ) T2
GROUP BY T2.Request_at