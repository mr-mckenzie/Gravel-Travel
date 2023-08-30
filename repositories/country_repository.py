# import run_sql function
from db.run_sql import run_sql
from models.country import Country
from models.location import Location
import repositories.continent_repository as continent_repo

# a function to save instances of country classes into the 'countries' db
def save(input_country: Country):
    sql = 'INSERT INTO countries (name, continent_id) VALUES (%s, %s) RETURNING (id)'
    values = [input_country.name, input_country.continent.id]
    run_sql_return = run_sql(sql, values)
    #print(f"THIS IS THE 'run_sql_return' VARIABLE FROM SAVE COUNTRY: {run_sql_return}")
    id = run_sql_return[0]['id']
    input_country.id = id
    return input_country

#select all country records
def select_all():
    sql = 'SELECT * FROM countries ORDER BY LOWER(name)'
    all_countries = run_sql(sql)
    #print('THIS IS THE RETURN OF RUN_SQL ON SELECT ALL:')
    all_results = []
    for row in all_countries:
        continent = continent_repo.select_one(row['continent_id'])
        all_results.append(Country(row['name'], continent,  int(row['id'])))
    #returns instances of country classes in list format
    return all_results

#select a single country record by id
def select_one(input_country_id):
    sql = 'SELECT * FROM countries WHERE id = (%s)'
    value = [str(input_country_id)]
    result = run_sql(sql, value)[0]
    #print(f'THIS IS THE RESULT FROM SELECT ONE COUNTRY {return_from_sql}')
    continent = continent_repo.select_one(result['continent_id'])
    country_instance = Country(result['name'], continent, int(result['id']))
    #returns an instance of a country
    return country_instance

#get all locations in a single country
def get_locations(input_country_id):
    sql = 'SELECT * FROM locations WHERE country_id = %s ORDER BY Lower(name)'
    locations = run_sql(sql, [str(input_country_id)])
    list_of_locations_in_country = [ ]
    #print("THIS IS THE GET LOCATIONS LIST:")
    for row in locations:

        list_of_locations_in_country.append(Location(row['name'], select_one(input_country_id), int(row['id'])))

        #print(row)
    #print(list_of_locations_in_country)
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