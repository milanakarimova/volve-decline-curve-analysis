SELECT
    wellbore,
    ROUND(SUM(oil_sm3), 2) AS total_oil_sm3,
    ROUND(SUM(gas_sm3), 2) AS total_gas_sm3,
    ROUND(SUM(water_sm3), 2) AS total_water_sm3,
    COUNT(*) AS monthly_records
FROM volve_production
GROUP BY wellbore
ORDER BY total_oil_sm3 DESC;
