-- A script that displays the max temperature of each state (ordered by State name).

-- Import in hbtn_0c_0 database this table dump: download (same as Temperatures #0)

-- https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql

SELECT state, MAX(value) as max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
