from db.run_sql import run_sql
from models.country import Country
from models.location import Location
import repositories.continent_repository as continent_repo

#save a new country record
def save(input_country: Country):
    sql = 'INSERT INTO countries (name, continent_id) VALUES (%s, %s) RETURNING (id)'
    values = [input_country.name, input_country.continent.id]
    run_sql_return = run_sql(sql, values)
    id = run_sql_return[0]['id']
    input_country.id = id
    return input_country

#select all country records
def select_all():
    sql = 'SELECT * FROM countries ORDER BY LOWER(name)'
    all_countries = run_sql(sql)
    all_results = []
    for row in all_countries:
        continent = continent_repo.select_one(row['continent_id'])
        all_results.append(Country(row['name'], continent,  int(row['id'])))
    #returns a list of country instances
    return all_results

#select a single country record by id
def select_one(input_country_id):
    sql = 'SELECT * FROM countries WHERE id = (%s)'
    value = [str(input_country_id)]
    result = run_sql(sql, value)[0]
    continent = continent_repo.select_one(result['continent_id'])
    country_instance = Country(result['name'], continent, int(result['id']))
    #returns an instance of a country
    return country_instance

#get all locations in a single country
def get_locations(input_country_id):
    sql = 'SELECT * FROM locations WHERE country_id = %s ORDER BY LOWER(name)'
    locations = run_sql(sql, [str(input_country_id)])
    list_of_locations_in_country = [ ]

    for row in locations:

        list_of_locations_in_country.append(Location(row['name'], select_one(input_country_id), int(row['id'])))

    return list_of_locations_in_country

#delete country by id
def delete_by_id(input_id):
    sql = 'DELETE FROM countries WHERE id = (%s)'
    value = [str(input_id)]
    run_sql(sql, value)

#update country name
def update_name(input_id, input_name):
    sql = 'UPDATE countries SET name = (%s) WHERE id = (%s)'
    value = [input_name, input_id]
    run_sql(sql, value)

#update country continent
def update_continent(input_id, input_continent_id):
    sql = 'UPDATE countries SET continent_id = (%s) WHERE id = (%s)'
    value = [input_continent_id, input_id]
    run_sql(sql, value)