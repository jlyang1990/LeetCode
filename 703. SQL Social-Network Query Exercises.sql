# Q1: Find the names of all students who are friends with someone named Gabriel. 
SELECT name
FROM Highschooler, Friend
WHERE ID = ID1 AND ID2 IN
	(SELECT ID
	FROM Highschooler
	WHERE name = "Gabriel")


# Q2: For every student who likes someone 2 or more grades younger than themselves, return that student's name and grade, 
# and the name and grade of the student they like. 
SELECT H1.name, H1.grade, H2.name, H2.grade
FROM Highschooler H1, Highschooler H2, Likes
WHERE H1.ID = ID1 AND H2.ID = ID2 AND H1.grade - H2.grade >= 2


# Q3: For every pair of students who both like each other, return the name and grade of both students. 
# Include each pair only once, with the two names in alphabetical order.
SELECT H1.name, H1.grade, H2.name, H2.grade
FROM Highschooler H1, Highschooler H2, Likes L1, Likes L2
WHERE H1.ID = L1.ID1 AND H2.ID = L1.ID2 
AND H2.ID = L2.ID1 AND H1.ID = L2.ID2 AND H1.name < H2.name


# Q4: Find all students who do not appear in the Likes table (as a student who likes or is liked) and return their names and grades. 
# Sort by grade, then by name within each grade. 
SELECT name, grade
FROM Highschooler
WHERE ID NOT IN
    (SELECT ID1
    FROM Likes
    UNION
    SELECT ID2
    FROM Likes)
ORDER BY grade, name


# Q5: For every situation where student A likes student B, but we have no information about whom B likes 
# (that is, B does not appear as an ID1 in the Likes table), return A and B's names and grades. 
SELECT H1.name, H1.grade, H2.name, H2.grade
FROM Highschooler H1, Highschooler H2, Likes
WHERE H1.ID = ID1 AND H2.ID = ID2 AND ID2 NOT IN
    (SELECT ID1
    FROM Likes)


# Q6: Find names and grades of students who only have friends in the same grade. Return the result sorted by grade, then by name within each grade. 
SELECT name, grade
FROM Highschooler
WHERE ID IN
	(SELECT H1.ID
	FROM Highschooler H1, Highschooler H2, Friend
	WHERE H1.ID = ID1 AND H2.ID = ID2 AND H1.grade = H2.grade)
AND ID NOT IN
	(SELECT H1.ID
	FROM Highschooler H1, Highschooler H2, Friend
	WHERE H1.ID = ID1 AND H2.ID = ID2 AND H1.grade != H2.grade)
ORDER BY grade, name


# Q7: For each student A who likes a student B where the two are not friends, find if they have a friend C in common (who can introduce them!). 
# For all such trios, return the name and grade of A, B, and C. 
SELECT H1.name, H1.grade, H2.name, H2.grade, H3.name, H3.grade
FROM Highschooler H1, Highschooler H2, Highschooler H3, Friend F1, Friend F2
WHERE H1.ID = F1.ID1 AND H3.ID = F1.ID2 AND H3.ID = F2.ID1 AND H2.ID = F2.ID2
AND H2.ID IN
(SELECT ID2
FROM Likes
WHERE ID1 = H1.ID)


# Q8: Find the difference between the number of students in the school and the number of different first names.
SELECT num_student - num_name
FROM
    (SELECT COUNT(*) AS num_student, COUNT(DISTINCT name) AS num_name
    FROM Highschooler)


# Q9: Find the name and grade of all students who are liked by more than one other student. 
# method 1
SELECT name, grade
FROM Highschooler
WHERE
	(SELECT COUNT(*)
	FROM Likes
	WHERE ID2 = ID) > 1

# method 2
SELECT name, grade
FROM Highschooler
WHERE ID IN
	(SELECT ID2
	FROM Likes
	GROUP BY ID2
	HAVING COUNT(*) > 1)