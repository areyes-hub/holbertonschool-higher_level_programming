-- lists all records of the table second_table
-- doesn't list records without a name
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
