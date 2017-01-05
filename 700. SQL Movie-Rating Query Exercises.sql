# Q1: Find the titles of all movies directed by Steven Spielberg.
SELECT title
FROM Movie
WHERE director = "Steven Spielberg"


# Q2: Find all years that have a movie that received a rating of 4 or 5, and sort them in increasing order. 
SELECT year
FROM Movie
WHERE mID in
    (SELECT mID
    FROM Rating
    WHERE stars BETWEEN 4 AND 5)
ORDER BY year


# Q3: Find the titles of all movies that have no ratings. 
SELECT title
FROM Movie
WHERE mID NOT IN
    (SELECT mID
    FROM Rating)


# Q4: Some reviewers didn't provide a date with their rating. Find the names of all reviewers who have ratings with a NULL value for the date.
SELECT name
FROM Reviewer
WHERE rID IN
    (SELECT rID
    FROM Rating
    WHERE ratingDate IS NULL)


# Q5: Write a query to return the ratings data in a more readable format: reviewer name, movie title, stars, and ratingDate. 
# Also, sort the data, first by reviewer name, then by movie title, and lastly by number of stars.
SELECT name, title, stars, ratingDate
FROM Movie, Reviewer, Rating
WHERE Movie.mID = Rating.mID and Reviewer.rID = Rating.rID
ORDER BY name, title, stars


# Q6: For all cases where the same reviewer rated the same movie twice and gave it a higher rating the second time, return the reviewer's name 
# and the title of the movie. 
SELECT name, title
FROM Movie, Reviewer,
    (SELECT R1.rID, R1.mID
    FROM Rating R1, Rating R2
    WHERE R1.rID = R2.rID AND R1.mID = R2.mID 
    AND R1.stars < R2.stars AND R1.ratingDate < R2.ratingDate) R
WHERE Movie.mID = R.mID AND Reviewer.rID = R.rID


# Q7: For each movie that has at least one rating, find the highest number of stars that movie received. Return the movie title and number of stars. 
# Sort by movie title.
SELECT title, stars
FROM Movie,
    (SELECT mID, MAX(stars) AS stars
    FROM Rating
    GROUP BY mID) M
WHERE Movie.mID = M.mID
ORDER BY title


# Q8: For each movie, return the title and the 'rating spread', that is, the difference between highest and lowest ratings given to that movie. 
# Sort by rating spread from highest to lowest, then by movie title. 
SELECT title, max_stars-min_stars AS spread
FROM Movie,
    (SELECT mID, MAX(stars) AS max_stars, MIN(stars) AS min_stars
    FROM Rating
    GROUP BY mID) M
WHERE Movie.mID = M.mID
ORDER BY spread DESC, title


# Q9: Find the difference between the average rating of movies released before 1980 and the average rating of movies released after 1980.
SELECT avg_stars_before - avg_stars_after
FROM
	(SELECT AVG(avg_stars) AS avg_stars_before
	FROM
		(SELECT mID, AVG(stars) AS avg_stars
		FROM Rating
		WHERE mID in
			(SELECT mID
			FROM Movie
			WHERE year < "1980")
		GROUP BY mID)
	) M1,
	SELECT AVG(avg_stars) AS avg_stars_after
	FROM
		(SELECT mID, AVG(stars) AS avg_stars
		FROM Rating
		WHERE mID in
			(SELECT mID
			FROM Movie
			WHERE year > "1980")
		GROUP BY mID)
	) M2