-- BEGIN STARTER
-- SELECT _____
--     _____,
--     _____
-- FROM _____
-- WHERE
--     _____ AND
--     _____ AND
--     _____
-- ORDER BY _____;
-- END STARTER

-- BEGIN SOLUTION NO PROMPT
SELECT DISTINCT
    title,
    artist
FROM
    hot_100
WHERE
    week_ending >= '2023-11-01' AND
    week_ending <= '2023-11-30' AND
    -- Alternatively, students can use:
    -- week_ending BETWEEN '2023-11-01' AND '2023-11-30' AND
    rank <= 5
ORDER BY
    artist;
-- END SOLUTION
