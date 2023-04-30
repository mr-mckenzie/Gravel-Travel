-- Set up tables, firstly by dropping any old tables that exist.
-- travellers_countries is a join table so it must be dropped first as it depends on the other tables.
DROP TABLE IF EXISTS travellers_countries;
DROP TABLE IF EXISTS travellers;
DROP TABLE IF EXISTS countries;

-- a table to hold the details of the traveller
CREATE TABLE travellers (
    id              SERIAL NOT NULL PRIMARY KEY,
    first_name      VARCHAR(255),
    last_name       VARCHAR(255)
);

-- a table to hold country information
CREATE TABLE countries (
    id              SERIAL NOT NULL PRIMARY KEY,
    name            VARCHAR(255)
);

-- a join table to link travellers with countries visited
CREATE TABLE travellers_countries (
    id              SERIAL PRIMARY KEY NOT NULL,
    traveller_id    INT REFERENCES travellers(id),
    country_id      INT REFERENCES countries(id),
    date_visited    DATE
);

-- add table rows containing traveller records
INSERT INTO travellers (first_name, last_name)
VALUES ('Gertrude', 'Smith');

INSERT INTO travellers (first_name, last_name)
VALUES ('Timothy', 'White');

-- add table rows containing country records
INSERT INTO countries (name)
VALUES ('South Korea');

INSERT INTO countries (name)
VALUES ('Canada');

INSERT INTO countries (name)
VALUES ('Estonia');

INSERT INTO countries (name)
VALUES ('Mongolia');

INSERT INTO countries (name)
VALUES ('Samoa');

INSERT INTO countries (name)
VALUES ('Ecuador');

-- add table rows linking travellers to countries
INSERT INTO travellers_countries (traveller_id, country_id, date_visited)
VALUES (1, 2, '2015-09-07');

INSERT INTO travellers_countries (traveller_id, country_id, date_visited)
VALUES (1, 4, '2023-03-27');

INSERT INTO travellers_countries (traveller_id, country_id, date_visited)
VALUES (2, 3, '2004-12-08');

INSERT INTO travellers_countries (traveller_id, country_id, date_visited)
VALUES (2, 2, '2004-07-14');