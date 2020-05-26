SELECT t1.name, ROUND(t1.highest, 2) AS highest, t1.hour, t2.ts
FROM (SELECT name, SUBSTR(ts, 12, 2) AS hour, MAX(high) as highest
      FROM "19"
      GROUP BY 1, 2) t1
      JOIN (SELECT name, ts, SUBSTR(ts, 12, 2) AS hour, high
            FROM "19") t2
            ON t1.name = t2.name
            AND t1.hour = t2.hour
            AND t1.highest = t2.high
            ORDER BY 1, 3;