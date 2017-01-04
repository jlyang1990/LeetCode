# Write your MySQL query statement below
SELECT T.Request_at AS Day,
ROUND(SUM(CASE WHEN T.Status like 'cancelled_by_%' THEN 1 ELSE 0 END) / COUNT(*), 2) AS 'Cancellation Rate'
FROM
    (SELECT Status, Request_at
    FROM Trips
    WHERE Request_at BETWEEN '2013-10-01' AND '2013-10-03'
    AND Client_Id in
        (SELECT Users_Id
        FROM Users
        WHERE Banned = "No")
    ) T
GROUP BY T.Request_at