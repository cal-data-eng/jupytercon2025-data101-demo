SELECT DISTINCT
    title,
    artist
FROM hot_100
WHERE
    week_ending >= '2023-11-01' AND
    week_ending <= '2024-11-30' AND
    rank <= 5
ORDER BY artist;
