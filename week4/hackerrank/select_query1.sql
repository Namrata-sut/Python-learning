-- Revising the Select Query I
--Query all columns for all American cities in the CITY table with populations larger than 100000. The CountryCode for America is USA.
SELECT * FROM city WHERE population > 100000 AND countrycode = "USA";

--Weather Observation Station 1
--Query a list of CITY and STATE from the STATION table.
SELECT city, state FROM station;

--Weather Observation Station 3
--Query a list of CITY names from STATION for cities that have an even ID number. Print the results in any order, but exclude duplicates from the answer.
SELECT DISTINCT city FROM station WHERE id = (id%2=0);

--Weather Observation Station 4
--Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.
SELECT count(city)-count(DISTINCT city) FROM station;

--Weather Observation Station 6
--Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.
SELECT DISTINCT city
FROM station
WHERE LOWER(city) LIKE 'a%'
   OR LOWER(city) LIKE 'e%'
   OR LOWER(city) LIKE 'i%'
   OR LOWER(city) LIKE 'o%'
   OR LOWER(city) LIKE 'u%';

--Weather Observation Station 7
--Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.
SELECT DISTINCT city
FROM station
WHERE LOWER(city) LIKE '%a'
   OR LOWER(city) LIKE '%e'
   OR LOWER(city) LIKE '%i'
   OR LOWER(city) LIKE '%o'
   OR LOWER(city) LIKE '%u';

--Weather Observation Station 8
--Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. Your result cannot contain duplicates.
SELECT DISTINCT city FROM station
WHERE (LOWER(city) LIKE 'a%' OR LOWER(city) LIKE 'e%' OR LOWER(city) LIKE 'i%' OR LOWER(city) LIKE 'o%' OR LOWER(city) LIKE 'u%')
  AND (LOWER(city) LIKE '%a' OR LOWER(city) LIKE '%e' OR LOWER(city) LIKE '%i' OR LOWER(city) LIKE '%o' OR LOWER(city) LIKE '%u');

--Weather Observation Station 9
--Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.
SELECT DISTINCT city FROM station
WHERE city NOT IN(SELECT city FROM station
WHERE LOWER(city) LIKE 'a%'
OR LOWER(city) LIKE 'e%'
OR LOWER(city) LIKE 'i%'
OR LOWER(city) LIKE 'o%'
OR LOWER(city) LIKE 'u%');

--Weather Observation Station 10
--Query the list of CITY names from STATION that do not end with vowels. Your result cannot contain duplicates.
SELECT DISTINCT city FROM station
WHERE city NOT IN
(SELECT city FROM station
WHERE city LIKE '%a'
OR city LIKE '%e'
OR city LIKE '%i'
OR city LIKE '%o'
OR city LIKE '%u' );

--Weather Observation Station 11
--Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.
SELECT DISTINCT city
FROM station
WHERE
    LOWER(city) NOT LIKE 'a%' AND
    LOWER(city) NOT LIKE 'e%' AND
    LOWER(city) NOT LIKE 'i%' AND
    LOWER(city) NOT LIKE 'o%' AND
    LOWER(city) NOT LIKE 'u%'
    OR
    LOWER(city) NOT LIKE '%a' AND
    LOWER(city) NOT LIKE '%e' AND
    LOWER(city) NOT LIKE '%i' AND
    LOWER(city) NOT LIKE '%o' AND
    LOWER(city) NOT LIKE '%u';

--Weather Observation Station 12
--Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain duplicates.
SELECT DISTINCT city
FROM station
WHERE
    LOWER(city) NOT LIKE 'a%' AND
    LOWER(city) NOT LIKE 'e%' AND
    LOWER(city) NOT LIKE 'i%' AND
    LOWER(city) NOT LIKE 'o%' AND
    LOWER(city) NOT LIKE 'u%'
    AND
    LOWER(city) NOT LIKE '%a' AND
    LOWER(city) NOT LIKE '%e' AND
    LOWER(city) NOT LIKE '%i' AND
    LOWER(city) NOT LIKE '%o' AND
    LOWER(city) NOT LIKE '%u';

--Employee Names
--Write a query that prints a list of employee names (i.e.: the name attribute) from the Employee table in alphabetical order.
SELECT name FROM employee ORDER BY name ASC;

--Employee Salaries
--Write a query that prints a list of employee names (i.e.: the name attribute) for employees in Employee having a salary greater than  per month who have been employees for less than  months. Sort your result by ascending employee_id.
SELECT name FROM employee WHERE salary > 2000 AND months < 10 ORDER BY employee_id ASC;






















