SELECT NAME, 
 
 cast(ROUND((population / (SELECT population FROM world WHERE name = 'Germany') * 100), 0) as nvarchar(10)) + '%'

AS PERCENTAGE FROM world
WHERE continent = 'Europe'
SELECT NAME, 
 
 CONCAT(CAST(ROUND(
(population / (SELECT population FROM world WHERE name = 'Germany') 
* 100),0)
as INT),'%')

AS PERCENTAGE FROM world
WHERE continent = 'Europe'