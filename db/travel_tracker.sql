-- Set up tables, firstly by dropping any old tables that exist.
-- holidays & wishlist are join tables so must be dropped first 
-- as they depend on the other tables.
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
CREATE TABLE holidays (
    id              SERIAL PRIMARY KEY NOT NULL,
    location_id     INT REFERENCES locations(id) ON DELETE CASCADE NOT NULL,
    date_visited    DATE,
    length_of_visit INT,
    wishlist        BOOLEAN
);

-- a join table to record countries the user wants to visit
CREATE TABLE wishlist (
    id              SERIAL PRIMARY KEY NOT NULL,
    location_id     INT REFERENCES locations(id) ON DELETE CASCADE NOT NULL
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
VALUES ('Canada', 4);

INSERT INTO countries (name, continent_id)
VALUES ('Estonia', 3);

INSERT INTO countries (name, continent_id)
VALUES ('Mongolia', 1);

INSERT INTO countries (name, continent_id)
VALUES ('Samoa', 6);

INSERT INTO countries (name, continent_id)
VALUES ('Ecuador', 5);

INSERT INTO countries (name, continent_id)
VALUES ('France', 3);

INSERT INTO countries (name, continent_id)
VALUES ('Kenya', 2);

-- add table entries containing locations 
INSERT INTO locations (name, country_id)
VALUES ('Seoul', 1);

INSERT INTO locations (name, country_id)
VALUES ('Vancouver', 2);

INSERT INTO locations (name, country_id)
VALUES ('Winnipeg', 2);

INSERT INTO locations (name, country_id)
VALUES ('Tallinn', 3);

INSERT INTO locations (name, country_id)
VALUES ('Ulaanbaatar', 4);

INSERT INTO locations (name, country_id)
VALUES('Apia', 5);

INSERT INTO locations (name, country_id)
VALUES ('Quito', 6);

INSERT INTO locations (name, country_id)
VALUES ('Paris', 7);

INSERT INTO locations (name, country_id)
VALUES ('Bordeaux', 7);

INSERT INTO locations (name, country_id)
VALUES ('Nice', 7);

INSERT INTO locations (name, country_id)
VALUES ('Orleans', 7);

-- add table rows recording holiday trips
INSERT INTO holidays (location_id, date_visited)
VALUES (2, '2015-09-07');

INSERT INTO holidays (location_id, date_visited)
VALUES (4, '2023-03-27');

INSERT INTO holidays (location_id, date_visited)
VALUES (3, '2013-04-03');

INSERT INTO holidays (location_id, date_visited)
VALUES (2, '2004-07-14');

-- add table rows to wishlist
INSERT INTO wishlist (location_id)
VALUES (6);

INSERT INTO wishlist (location_id)
VALUES (7);

INSERT INTO wishlist (location_id)
VALUES (5);

INSERT INTO wishlist (location_id)
VALUES (9);
