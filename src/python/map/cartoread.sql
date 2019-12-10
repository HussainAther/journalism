--SQL (Structured query language) for Carto mapping
--Select all data from the table
SELECT * FROM ne_50m_admin_1_states
--CartoDB code to create dataset
SELECT *
FROM ne_50m_admin_1_states
WHERE postal = 'OR'
