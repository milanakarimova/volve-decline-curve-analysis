SELECT
    wellbore,
    year,
    ROUND(SUM(oil_sm3), 2) AS yearly_oil_sm3,
    ROUND(SUM(gas_sm3), 2) AS yearly_gas_sm3,
    ROUND(SUM(water_sm3), 2) AS yearly_water_sm3
FROM volve_production
GROUP BY wellbore, year
ORDER BY wellbore, year;
