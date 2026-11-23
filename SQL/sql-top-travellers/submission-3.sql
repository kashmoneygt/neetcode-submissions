-- Write your query below

SELECT DISTINCT u.name,
CASE WHEN r.distance IS NOT NULL
 THEN SUM(distance) OVER(PARTITION BY r.user_id ORDER BY r.user_id)
 ELSE 0
 END AS travelled_distance
FROM users u
LEFT JOIN rides r
ON u.id = r.user_id
ORDER BY travelled_distance DESC, u.name

-- 1 Maria 1 1 150
-- 1 Maria 4 1 130
