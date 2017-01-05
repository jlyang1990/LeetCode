# Q1: It's time for the seniors to graduate. Remove all 12th graders from Highschooler. 
DELETE FROM Highschooler
WHERE grade = 12


# Q3: For all cases where A is friends with B, and B is friends with C, add a new friendship for the pair A and C. 
# Do not add duplicate friendships, friendships that already exist, or friendships with oneself. 
INSERT INTO Friend
SELECT DISTINCT F1.ID1, F2.ID2
FROM Friend F1, Friend F2
WHERE F1.ID2 = F2.ID1
AND F2.ID2 NOT IN
	(SELECT ID2
	FROM Friend
	WHERE ID1 = F1.ID1)
AND F2.ID2 != F1.ID1