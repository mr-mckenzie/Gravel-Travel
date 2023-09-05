from db.run_sql import run_sql
from models.continent import Continent
from models.country import Country
import repositories.country_repository as country_repo

#select all continent records
def select_all():
    sql = 'SELECT * FROM continents'
    all_continents = run_sql(sql)
    all_results = []
    for row in all_continents:
        all_results.append( Continent(row['name'], int(row['id'])) )
    #returns a list of continent class instances
    return all_results

#select a single continent record by id
def select_one(input_continent_id):
    sql = 'SELECT * FROM continents WHERE id = (%s)'
    value = [str(input_continent_id)]
    selected_continent = (run_sql(sql, value))[0]
    continent_instance = Continent(selected_continent['name'], int(selected_continent['id']))
    #returns an instance of a continent class
    return continent_instance

#get all countries in a single continent
def get_countries(input_continent_id):
    sql = 'SELECT * FROM countries WHERE continent_id = %s ORDER BY LOWER(name)'
    countries = run_sql(sql, [str(input_continent_id)])
    list_of_countries_in_continent = [ ]

    for row in countries:

        country = Country(row['name'], select_one(input_continent_id), int(row['id']))

        country_with_locations = {'name': country.name,
                                  'continent': country.continent,
                                  'id': country.id,
                                  'locations': country_repo.get_locations(row['id'])}

        list_of_countries_in_continent.append(country_with_locations)

    return list_of_countries_in_continent

#get all countries ordered by continent
def all_by_continent():
    countries_by_continent = []
    
    for num in range(1,7):
        if get_countries(num) != []:
            continent_name = select_one(num).name
            dict_continent_countries = {
                'continent_name' : continent_name,
                'countries' : get_countries(num)
            }
            countries_by_continent.append( dict_continent_countries )

    return countries_by_continent