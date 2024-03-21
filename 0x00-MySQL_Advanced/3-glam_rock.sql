-- Task 3: Old school band.
-- IFNULL(split, 2020) - IFNULL(formed, 0)
SELECT band_name as band_name, IF(split IS NULL, 2022, split) - formed AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
