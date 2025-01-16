--Write a query identifying the type of each record in the TRIANGLES table using its three side lengths.
--Output one of the following statements for each record in the table:
--
--Equilateral: It's a triangle with  sides of equal length.
--Isosceles: It's a triangle with  sides of equal length.
--Scalene: It's a triangle with  sides of differing lengths.
--Not A Triangle: The given values of A, B, and C don't form a triangle.

SELECT
    CASE
        WHEN (a+b) <= c OR (b+c) <= a OR (a+c) <= b THEN 'Not A Triangle'
        WHEN a = b AND b = c THEN 'Equilateral'
        WHEN a = b OR b = c or c = a THEN 'Isosceles'
        WHEN a != b AND b != c AND c != a THEN 'Scalene'
    END
FROM TRIANGLES;


--Generate the following two result sets:
--Query an alphabetically ordered list of all names in OCCUPATIONS, immediately followed by the first letter of each
--profession as a parenthetical (i.e.: enclosed in parentheses). For example: AnActorName(A), ADoctorName(D),
--AProfessorName(P), and ASingerName(S).
--Query the number of ocurrences of each occupation in OCCUPATIONS. Sort the occurrences in ascending order, and
--output them in the following format: There are a total of [occupation_count] [occupation]s.
SELECT name || '(' ||  SUBSTRING(occupation, 1, 1) ||  ')' AS occup FROM occupations
ORDER BY name ASC;
SELECT 'There are a total of ' || COUNT(occupation) || ' ' || LOWER(occupation) || 's.' FROM occupations
GROUP BY occupation
ORDER BY COUNT(occupation)ASC, occupation ASC;

--You are given a table, BST, containing two columns: N and P, where N represents the value of a node in Binary Tree,
--and P is the parent of N.
--Write a query to find the node type of Binary Tree ordered by the value of the node. Output one of the following
--for each node:
--Root: If node is root node.
--Leaf: If node is leaf node.
--Inner: If node is neither root nor leaf node.
SELECT N, CASE
WHEN P IS NULL THEN 'Root'
WHEN N IN (SELECT DISTINCT P FROM BST) THEN 'Inner'
ELSE 'Leaf'
END
FROM BST
ORDER BY N;
