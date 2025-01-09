--Given the CITY and COUNTRY tables, query the sum of the populations of all cities where the CONTINENT is 'Asia'.
--Note: CITY.CountryCode and COUNTRY.Code are matching key columns.
SELECT SUM(city.population) FROM city
INNER JOIN country ON countrycode = code
GROUP BY continent
HAVING continent = "Asia"


--Given the CITY and COUNTRY tables, query the names of all cities where the CONTINENT is 'Africa'.
SELECT city.name FROM city
INNER JOIN country ON city.countrycode = country.code
WHERE country.continent = "Africa";


--Given the CITY and COUNTRY tables, query the names of all the continents (COUNTRY.Continent) and
--their respective average city populations (CITY.Population) rounded down to the nearest integer.
SELECT country.continent, FLOOR(avg(city.population)) FROM country
INNER JOIN city ON country.code = city.countrycode
GROUP BY country.continent;


