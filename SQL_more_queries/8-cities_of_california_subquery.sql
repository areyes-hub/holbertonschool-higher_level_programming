-- lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT id, name
FROM cities
WHERE cities.state_id = states.id
HAVING states.name = 'California'
ORDER BY cities.id ASC;
