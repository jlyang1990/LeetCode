# Q1: Find the names of all reviewers who rated Gone with the Wind. 
SELECT name
FROM Reviewer
WHERE rID in
	(SELECT rID
	FROM Rating
	WHERE mID =
		(SELECT mID
		FROM Movie
		WHERE title = "Gone with the Wind")
	)


# Q2: For any rating where the reviewer is the same as the director of the movie, return the reviewer name, movie title, and number of stars. 
SELECT name, title, stars
FROM Movie, Reviewer, Rating
WHERE Movie.mID = Rating.mID and Reviewer.rID = Rating.rID and Movie.director = Reviewer.name


# Q3: Return all reviewer names and movie names together in a single list, alphabetized.
SELECT name
FROM Reviewer
UNION
SELECT title
FROM Movie


# Q4: Find the titles of all movies not reviewed by Chris Jackson. 
SELECT title
FROM Movie
WHERE mID NOT IN
    (SELECT mID
    FROM Rating
    WHERE rID IN
        (SELECT rID
        FROM Reviewer
        WHERE name = "Chris Jackson")
    )


# Q5: For all pairs of reviewers such that both reviewers gave a rating to the same movie, return the names of both reviewers. 
# Eliminate duplicates, don't pair reviewers with themselves, and include each pair only once. 
# For each pair, return the names in the pair in alphabetical order. 
SELECT DISTINCT Re1.name, Re2.name
FROM
Reviewer Re1, Reviewer Re2,
	(SELECT R1.rID AS rID1, R2.rID AS rID2
	FROM Rating R1, Rating R2
	WHERE R1.mID = R2.mID) R
WHERE Re1.rID = R.rID1 AND Re2.rID = R.rID2 AND Re1.name < Re2.name


# Q6: For each rating that is the lowest (fewest stars) currently in the database, return the reviewer name, movie title, and number of stars. 
SELECT name, title, stars
FROM Movie, Reviewer, Rating
WHERE Movie.mID = Rating.mID AND Reviewer.rID = Rating.rID AND stars =
    (SELECT min(stars)
    FROM Rating)


# Q7: List movie titles and average ratings, from highest-rated to lowest-rated. If two or more movies have the same average rating,
# list them in alphabetical order. 
SELECT title, avg_stars
FROM Movie,
    (SELECT mID, AVG(stars) AS avg_stars
    FROM Rating
    GROUP BY mID) R
WHERE Movie.mID = R.mID
ORDER BY avg_stars DESC, title


# Q8: Find the names of all reviewers who have contributed three or more ratings.
SELECT name
FROM Reviewer
WHERE rID in
    (SELECT rID
    FROM Rating
    GROUP BY rID
    HAVING COUNT(*) >= 3)


# Q9: Some directors directed more than one movie. For all such directors, return the titles of all movies directed by them, 
# along with the director name. Sort by director name, then movie title.
SELECT title, director
FROM Movie
WHERE director IN
    (SELECT director
    FROM Movie
    GROUP BY director
    HAVING COUNT(*) > 1)
ORDER BY director, title


# Q10: Find the movie(s) with the highest average rating. Return the movie title(s) and average rating.
SELECT title, avg_stars
FROM Movie, 
    (SELECT mID, AVG(stars) AS avg_stars
    FROM Rating
    GROUP BY mID) R
WHERE Movie.mID = R.mID AND R.avg_stars =
    (SELECT MAX(avg_stars)
    FROM
        (SELECT AVG(stars) AS avg_stars
        FROM Rating
        GROUP BY mID)
    )


# Q11: Find the movie(s) with the lowest average rating. Return the movie title(s) and average rating.
SELECT title, avg_stars
FROM Movie,
    (SELECT mID, AVG(stars) AS avg_stars
    FROM Rating
    GROUP BY mID) R
WHERE Movie.mID = R.mID AND R.avg_stars =
    (SELECT MIN(avg_stars)
    FROM
        (SELECT AVG(stars) AS avg_stars
        FROM Rating
        GROUP BY mID)
    )


# Q12: For each director, return the director's name together with the title(s) of the movie(s) they directed 
# that received the highest rating among all of their movies, and the value of that rating. Ignore movies whose director is NULL.
SELECT director, title, max_stars
FROM
	(SELECT director, title, max_stars
	FROM Movie,
		(SELECT mID, MAX(stars) AS max_stars
		FROM Rating
		GROUP BY mID) R
	WHERE Movie.mID = R.mID AND director IS NOT NULL) J
WHERE 0 =
	(SELECT COUNT(*)
	FROM
		(SELECT director, title, max_stars
		FROM Movie,
			(SELECT mID, MAX(stars) AS max_stars
			FROM Rating
			GROUP BY mID) R
		WHERE Movie.mID = R.mID AND director IS NOT NULL) J2
	WHERE J2.director = J.director AND J2.max_stars > J.max_stars)