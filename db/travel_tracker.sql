-- Set up tables, firstly by dropping any old tables that exist.
-- user_country is a join table so it must be dropped first as it depends on the other tables.
DROP TABLE IF EXISTS traveller_country;
DROP TABLE IF EXISTS traveller;
DROP TABLE IF EXISTS country;

-- a table to hold the details of the traveller
CREATE TABLE traveller (
    id              SERIAL NOT NULL PRIMARY KEY,
    first_name      VARCHAR(255),
    last_name       VARCHAR(255)
);

-- a table to hold country information
CREATE TABLE country (
    id              SERIAL NOT NULL PRIMARY KEY,
    name            VARCHAR(255)
);

-- a join table to link travellers with countries visited
CREATE TABLE traveller_country (
    id              SERIAL PRIMARY KEY NOT NULL,
    traveller_id    INT REFERENCES traveller(id),
    country_id      INT REFERENCES country(id),
    date_visited    DATE
);

-- add table rows containing traveller records
INSERT INTO traveller (first_name, last_name)
VALUES ('Gertrude', 'Smith');

INSERT INTO traveller (first_name, last_name)
VALUES ('Timothy', 'White');

-- add table rows containing country records
INSERT INTO country (name)
VALUES ('South Korea');

INSERT INTO country (name)
VALUES ('Canada');

INSERT INTO country (name)
VALUES ('Estonia');

INSERT INTO country (name)
VALUES ('Mongolia');

INSERT INTO country (name)
VALUES ('Samoa');

INSERT INTO country (name)
VALUES ('Ecuador');

-- add table rows linking travellers to countries
INSERT INTO traveller_country (traveller_id, country_id, date_visited)
VALUES (1, 2, '2015-09-07');

INSERT INTO traveller_country (traveller_id, country_id, date_visited)
VALUES (1, 4, '2023-03-27');

INSERT INTO traveller_country (traveller_id, country_id, date_visited)
VALUES (2, 3, '2004-12-08');

INSERT INTO traveller_country (traveller_id, country_id, date_visited)
VALUES (2, 2, '2004-07-14');