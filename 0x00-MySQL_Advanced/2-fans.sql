-- SQL script that ranks country origins of bands
-- ordered by the number of (non-unique) fans
SELECT origin, fans as nb_fans
FROM metal_bands
ORDER BY fans;
