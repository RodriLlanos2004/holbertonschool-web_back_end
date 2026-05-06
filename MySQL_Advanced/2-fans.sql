-- Clasifica los orígenes de las bandas de metal por número total de fans.
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
