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
VALUES ('South Korea', 1);

INSERT INTO countries (name, continent_id)
VALUES ('Vietnam', 1);

INSERT INTO countries (name, continent_id)
VALUES ('Austria', 3);

INSERT INTO countries (name, continent_id)
VALUES ('Belarus', 3);

INSERT INTO countries (name, continent_id)
VALUES ('Netherlands', 3);

INSERT INTO countries (name, continent_id)
VALUES ('Spain', 3);

INSERT INTO countries (name, continent_id)
VALUES ('Sweden', 3);

INSERT INTO countries (name, continent_id)
VALUES ('Argentina', 5);

INSERT INTO countries (name, continent_id)
VALUES ('Uruguay', 5);

-- add table entries containing locations 
INSERT INTO locations (name, country_id)
VALUES ('Busan', 1);

INSERT INTO locations (name, country_id)
VALUES ('Hanoi', 2);

INSERT INTO locations (name, country_id)
VALUES ('Vienna', 3);

INSERT INTO locations (name, country_id)
VALUES ('Graz', 3);

INSERT INTO locations (name, country_id)
VALUES ('Salihorsk', 4);

INSERT INTO locations (name, country_id)
VALUES ('Maastricht', 5);

INSERT INTO locations (name, country_id)
VALUES ('Amsterdam', 5);

INSERT INTO locations (name, country_id)
VALUES('Madrid', 6);

INSERT INTO locations (name, country_id)
VALUES('Bilbao', 6);

INSERT INTO locations (name, country_id)
VALUES ('Örnsköldsvik', 7);

INSERT INTO locations (name, country_id)
VALUES ('Buenos Aires', 8);

INSERT INTO locations (name, country_id)
VALUES ('Montevideo', 9);

-- add table rows recording trips
INSERT INTO trips (location_id, date_visited, length_of_visit, visited)
VALUES (1, '2018-10-10', 8, True);

INSERT INTO trips (location_id, date_visited, length_of_visit, visited)
VALUES (2, '2021-06-07', 2, True);

INSERT INTO trips (location_id, date_visited, length_of_visit, visited)
VALUES (3, '2022-04-01', 1, True);

INSERT INTO trips (location_id, date_visited, length_of_visit, visited)
VALUES (7, '2017-09-25', 19, True);

INSERT INTO trips (location_id, date_visited, length_of_visit, visited)
VALUES (9, '2019-12-30', 3, True);

INSERT INTO trips (location_id, date_visited, length_of_visit, visited)
VALUES (11, '2019-03-14', 5, True);

-- add table rows to wishlist
INSERT INTO trips (location_id, visited)
VALUES (4, False);

INSERT INTO trips (location_id, visited)
VALUES (5, True);

INSERT INTO trips (location_id, visited)
VALUES (6, False);

INSERT INTO trips (location_id, visited)
VALUES (8, True);

INSERT INTO trips (location_id, visited)
VALUES (10, False);

INSERT INTO trips (location_id, visited)
VALUES (12, False);