-- Set up tables, firstly by dropping any old tables that exist.
-- holidays & wishlist are join tables so must be dropped first 
-- as they depend on the other tables.
DROP TABLE IF EXISTS trips;
DROP TABLE IF EXISTS holidays;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS locations;
DROP TABLE IF EXISTS countries;
DROP TABLE IF EXISTS continents;

-- a table to hold continents
CREATE TABLE continents (
    id              SERIAL NOT NULL PRIMARY KEY,
    name            VARCHAR(255)
);

-- a table to hold country information
CREATE TABLE countries (
    id              SERIAL NOT NULL PRIMARY KEY,
    name            VARCHAR(255),
    continent_id    INT REFERENCES continents(id) NOT NULL
);

-- table to hold locations
CREATE TABLE locations (
    id              SERIAL NOT NULL PRIMARY KEY,
    name            VARCHAR(255),
    country_id      INT REFERENCES countries(id) NOT NULL
);

-- a join table to record countries visited
-- note that location_id must be NOT NULL because this stops instances of Location classes without ids from being saved
--CREATE TABLE holidays (
--    id              SERIAL PRIMARY KEY NOT NULL,
--    location_id     INT REFERENCES locations(id) ON DELETE CASCADE NOT NULL,
--    date_visited    DATE,
--    length_of_visit INT,
--    wishlist        BOOLEAN
--);

CREATE TABLE trips (
    id              SERIAL PRIMARY KEY NOT NULL,
    location_id     INT REFERENCES locations(id) ON DELETE CASCADE NOT NULL,
    date_visited    DATE,
    length_of_visit INT,
    wishlist        BOOLEAN
);

-- a join table to record countries the user wants to visit
--CREATE TABLE wishlist (
--    id              SERIAL PRIMARY KEY NOT NULL,
--    location_id     INT REFERENCES locations(id) ON DELETE CASCADE NOT NULL
--);

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
VALUES ('China', 1);

INSERT INTO countries (name, continent_id)
VALUES ('Canada', 4);

INSERT INTO countries (name, continent_id)
VALUES ('Germany', 3);

INSERT INTO countries (name, continent_id)
VALUES ('Costa Rica', 4);

INSERT INTO countries (name, continent_id)
VALUES ('New Zealand', 6);

INSERT INTO countries (name, continent_id)
VALUES ('Denmark', 3);

INSERT INTO countries (name, continent_id)
VALUES ('France', 3);

INSERT INTO countries (name, continent_id)
VALUES ('Belgium', 3);

INSERT INTO countries (name, continent_id)
VALUES ('Iceland', 3);

INSERT INTO countries (name, continent_id)
VALUES ('Spain', 3);

INSERT INTO countries (name, continent_id)
VALUES ('Netherlands', 3);

-- add table entries containing locations 
INSERT INTO locations (name, country_id)
VALUES ('Beijing', 1);

INSERT INTO locations (name, country_id)
VALUES ('Vancouver', 2);

INSERT INTO locations (name, country_id)
VALUES ('Toronto', 2);

INSERT INTO locations (name, country_id)
VALUES ('Sudbury', 2);

INSERT INTO locations (name, country_id)
VALUES ('Berlin', 3);

INSERT INTO locations (name, country_id)
VALUES ('San Jose', 4);

INSERT INTO locations (name, country_id)
VALUES('Auckland', 5);

INSERT INTO locations (name, country_id)
VALUES('Wellington', 5);

INSERT INTO locations (name, country_id)
VALUES ('Copenhagen', 6);

INSERT INTO locations (name, country_id)
VALUES ('Paris', 7);

INSERT INTO locations (name, country_id)
VALUES ('Bordeaux', 7);

INSERT INTO locations (name, country_id)
VALUES ('Mallorca', 10);

-- add table rows recording holiday trips
INSERT INTO trips (location_id, date_visited, length_of_visit, wishlist)
VALUES (1, '2020-01-10', 8, False);

INSERT INTO trips (location_id, date_visited, length_of_visit, wishlist)
VALUES (7, '2020-02-10', 365, False);

INSERT INTO trips (location_id, date_visited, length_of_visit, wishlist)
VALUES (2, '2020-02-07', 2, False);

INSERT INTO trips (location_id, date_visited, length_of_visit, wishlist)
VALUES (3, '2020-02-01', 1, False);

INSERT INTO trips (location_id, date_visited, length_of_visit, wishlist)
VALUES (11, '2022-07-14', 5, False);

INSERT INTO trips (location_id, date_visited, length_of_visit, wishlist)
VALUES (9, '2022-11-01', 3, False);

-- add table rows to wishlist
INSERT INTO trips (location_id, wishlist)
VALUES (5, True);

INSERT INTO trips (location_id, wishlist)
VALUES (9, True);
