-- Set up tables, firstly by dropping any old tables that exist.
-- trips, locations & countries are join tables so must be dropped in the right order
-- since they depend on the other tables.
DROP TABLE IF EXISTS trips;
DROP TABLE IF EXISTS locations;
DROP TABLE IF EXISTS countries;
DROP TABLE IF EXISTS continents;

-- a table to hold continents
CREATE TABLE continents (
    id              SERIAL NOT NULL PRIMARY KEY,
    name            VARCHAR(255)
);

-- a join table to hold country information
CREATE TABLE countries (
    id              SERIAL NOT NULL PRIMARY KEY,
    name            VARCHAR(255),
    continent_id    INT REFERENCES continents(id) NOT NULL
);

-- a join table to hold locations
CREATE TABLE locations (
    id              SERIAL NOT NULL PRIMARY KEY,
    name            VARCHAR(255),
    country_id      INT REFERENCES countries(id) ON DELETE CASCADE NOT NULL
);

-- a join table to record trips
-- note that location_id must be NOT NULL because this stops instances of Location classes without ids from being saved
CREATE TABLE trips (
    id              SERIAL PRIMARY KEY NOT NULL,
    location_id     INT REFERENCES locations(id) ON DELETE CASCADE NOT NULL,
    date_visited    DATE,
    length_of_visit INT,
    visited          BOOLEAN
);

-- add table rows containing continent records
INSERT INTO continents (name)
VALUES ('Asia');

INSERT INTO continents (name)
VALUES ('Africa');

INSERT INTO continents (name)
VALUES ('Europe');

INSERT INTO continents (name)
VALUES ('North America');

INSERT INTO continents (name)
VALUES ('South America');

INSERT INTO continents (name)
VALUES ('Oceania');

-- add table rows containing country records
INSERT INTO countries (name, continent_id)
VALUES ('Mongolia', 1);

INSERT INTO countries (name, continent_id)
VALUES ('Belgium', 3);

INSERT INTO countries (name, continent_id)
VALUES ('Netherlands', 3);

INSERT INTO countries (name, continent_id)
VALUES ('Sweden', 3);

INSERT INTO countries (name, continent_id)
VALUES ('Canada', 4);

INSERT INTO countries (name, continent_id)
VALUES ('Argentina', 5);

INSERT INTO countries (name, continent_id)
VALUES ('Uruguay', 5);

-- add table entries containing locations 
INSERT INTO locations (name, country_id)
VALUES ('Ulaanbaatar', 1);

INSERT INTO locations (name, country_id)
VALUES ('Ghent', 2);

INSERT INTO locations (name, country_id)
VALUES ('Amsterdam', 3);

INSERT INTO locations (name, country_id)
VALUES ('Maastricht', 3);

INSERT INTO locations (name, country_id)
VALUES ('Stockholm', 4);

INSERT INTO locations (name, country_id)
VALUES ('Vancouver', 5);

INSERT INTO locations (name, country_id)
VALUES ('Buenos Aires', 6);

INSERT INTO locations (name, country_id)
VALUES ('Montevideo', 7);

-- add table rows recording trips
INSERT INTO trips (location_id, date_visited, length_of_visit, visited)
VALUES (6, '2022-12-28', 8, True);

INSERT INTO trips (location_id, date_visited, length_of_visit, visited)
VALUES (2, '2022-08-05', 4, True);

INSERT INTO trips (location_id, date_visited, length_of_visit, visited)
VALUES (3, '2022-08-04', 1, True);

INSERT INTO trips (location_id, date_visited, length_of_visit, visited)
VALUES (3, '2017-03-25', 7, True);

-- add table rows to wishlist
INSERT INTO trips (location_id, visited)
VALUES (1, True);

INSERT INTO trips (location_id, visited)
VALUES (4, False);

INSERT INTO trips (location_id, visited)
VALUES (5, True);

INSERT INTO trips (location_id, visited)
VALUES (7, False);

INSERT INTO trips (location_id, visited)
VALUES (8, False);