--SQL (Structured query language) for Carto mapping
--Select all data from the table
SELECT * FROM ne_50m_admin_1_states
--CartoDB code to create dataset
SELECT *
FROM ne_50m_admin_1_states
WHERE postal = 'OR'
--Sample query
SELECT seismic_risk.acc_val, ST_Intersection(seismic_risk.the_geom, oregon.the_geom) AS the_geom
FROM seismic_risk, oregon
WHERE ST_Intersects(seismic_risk.the_geom, oregon.the_geom)
