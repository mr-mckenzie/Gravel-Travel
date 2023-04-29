-- Set up tables, firstly by dropping any old tables that exist.
-- user_country is a join table so it must be dropped first as it depends on the other tables.
DROP TABLE IF EXISTS user_country;
DROP TABLE IF EXISTS traveller;
DROP TABLE IF EXISTS country;

-- a table to hold the details of the traveller
CREATE TABLE traveller (
    id SERIAL,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);

-- a table to hold country information
CREATE TABLE country (
    id SERIAL,
    name VARCHAR(255)
);

-- a join table to link travellers with countries visited
CREATE TABLE traveller_country (
    id SERIAL,
    user_id INT,
    country_id INT,
    date_visited DATE
);