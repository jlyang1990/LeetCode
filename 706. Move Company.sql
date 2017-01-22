#table: company
#Member_id, Company, Year_Start
#1, Microsoft, 2000
#1, Google, 2006
#1, Facebook, 2012
#2, Microsoft, 2001. more info on 1point3acres.com
#2, Oracle, 2004
#2, Google, 2007
#...


-- how many members ever moved from Microsoft to Google? (both member #1 and member #2 count)

SELECT COUNT(DISTINCT c1.Member_id)
FROM company c1 AND company c2
WHERE c1.Member_id = c2.Member_id 
AND c1.Company = 'Microsoft' 
AND c2.Company = 'Google'
AND c1.Year_Start < c2.Year_Start


# deal with the cases when years are equal
SELECT COUNT(DISTINCT c1.Member_id)
FROM
(SELECT *, ROW_NUMBER()
OVER (PARTITION BY Company) AS Row_Number
FROM company) c1
AND
(SELECT *, ROW_NUMBER()
OVER (PARTITION BY Company) AS Row_Number
FROM company) c2
WHERE c1.Member_id = c2.Member_id 
AND c1.Company = 'Microsoft' 
AND c2.Company = 'Google'
AND c1.Row_Number < c2.Row_Number


-- how many members moved directly from Microsoft to Google? (Member 2 does not count since Microsoft -> Oracle -> Google)


SELECT COUNT(DISTINCT c1.Member_id)
FROM company c1 AND company c2
WHERE c1.Member_id = c2.Member_id
AND c1.Company = 'Microsoft' 
AND c2.Company = 'Google'
AND c1.Year_Start < c2.Year_Start
AND NOT EXIST(
SELECT c3.Member_id
FROM company c3
WHERE c3.Member_id = c1.Member_id
AND c3.Year_Start > c1.Year_Start AND c3.Year_Start < c2.Year_Start
)
