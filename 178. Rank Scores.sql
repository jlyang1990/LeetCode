# Write your MySQL query statement below
# method 1
SELECT Score, DENSE_RANK() OVER
(ORDER BY Score DESC)
FROM Scores


# method 2
SELECT Score,
	(SELECT count(*)
	FROM
		(SELECT DISTINCT Score
		FROM Scores) S2
	WHERE S2.Score >= S1.Score
	) Rank
FROM Scores S1
ORDER BY Score DESC