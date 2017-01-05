# Q1: For every situation where student A likes student B, but student B likes a different student C, return the names and grades of A, B, and C. 
SELECT H1.name, H1.grade, H2.name, H2.grade, H3.name, H3.grade
FROM Highschooler H1, Highschooler H2, Highschooler H3, Likes L1, Likes L2
WHERE H1.ID = L1.ID1 AND H2.ID = L1.ID2 AND H2.ID = L2.ID1 AND H3.ID = L2.ID2
AND H1.ID != H3.ID


# Q2: Find those students for whom all of their friends are in different grades from themselves. Return the students' names and grades. 
SELECT name, grade
FROM Highschooler
WHERE ID IN
	(SELECT H1.ID
	FROM Highschooler H1, Highschooler H2, Friend
	WHERE H1.ID = ID1 AND H2.ID = ID2 AND H1.grade != H2.grade)
AND ID NOT IN
	(SELECT H1.ID
	FROM Highschooler H1, Highschooler H2, Friend
	WHERE H1.ID = ID1 AND H2.ID = ID2 AND H1.grade = H2.grade)


# Q3: What is the average number of friends per student?
SELECT 1.0*total_friend/total_student
FROM
    (SELECT COUNT(*) AS total_friend
    FROM Friend),
    (SELECT COUNT(*) AS total_student
    FROM Highschooler)


# Q4: Find the number of students who are either friends with Cassandra or are friends of friends of Cassandra. 
# Do not count Cassandra, even though technically she is a friend of a friend. 
SELECT COUNT(*)-1
FROM
    (SELECT ID2
    FROM Friend
    WHERE ID1 IN
        (SELECT ID
        FROM Highschooler
        WHERE name = "Cassandra")
    UNION
    SELECT ID2
    FROM Friend
    WHERE ID1 IN
        (SELECT ID2
        FROM Friend
        WHERE ID1 IN
            (SELECT ID
            FROM Highschooler
            WHERE name = "Cassandra")
        )
    )


# Q5: Find the name and grade of the student(s) with the greatest number of friends. 
SELECT name, grade
FROM Highschooler,
	(SELECT ID1, COUNT(*) AS num_friend
	FROM Friend
	GROUP BY ID1)
WHERE ID = ID1
AND num_friend = 
	(SELECT MAX(num_friend)
	FROM
		(SELECT COUNT(*) AS num_friend
		FROM Friend
		GROUP BY ID1)
	)