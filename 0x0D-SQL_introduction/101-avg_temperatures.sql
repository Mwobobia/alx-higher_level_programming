-- A script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

-- Import in hbtn_0c_0 database this table dump: download https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql

SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
