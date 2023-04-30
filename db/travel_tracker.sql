-- Set up tables, firstly by dropping any old tables that exist.
-- holidays is a join table so it must be dropped first as it depends on the other tables.
DROP TABLE IF EXISTS holidays;
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
-- note that traveller_id and country_id must be NOT NULL because this stops instances of Traveller and Country classes without ids from being saved
CREATE TABLE holidays (
    id              SERIAL PRIMARY KEY NOT NULL,
    traveller_id    INT REFERENCES travellers(id) NOT NULL,
    country_id      INT REFERENCES countries(id) NOT NULL,
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
INSERT INTO holidays (traveller_id, country_id, date_visited)
VALUES (1, 2, '2015-09-07');

INSERT INTO holidays (traveller_id, country_id, date_visited)
VALUES (1, 4, '2023-03-27');

INSERT INTO holidays (traveller_id, country_id, date_visited)
VALUES (2, 3, '2004-12-08');

INSERT INTO holidays (traveller_id, country_id, date_visited)
VALUES (2, 2, '2004-07-14');