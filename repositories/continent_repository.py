# import run_sql function
from db.run_sql import run_sql
from models.continent import Continent
from models.country import Country

#select all continent records
def select_all():
    sql = 'SELECT * FROM continents'
    all_continents = run_sql(sql)
    #print('THIS IS THE RETURN OF RUN_SQL ON SELECT ALL:')
    all_results = []
    for row in all_continents:
        all_results.append( Continent(row['name'], int(row['id'])) )
    #returns instances of continent classes in a list format
    return all_results

#select a single continent record by id
def select_one(input_continent_id):
    sql = 'SELECT * FROM continents WHERE id = (%s)'
    value = [str(input_continent_id)]
    selected_continent = (run_sql(sql, value))[0]
    
    #return_from_sql = run_sql(sql, value)
    #selected_continent = return_from_sql[0]

    continent_instance = Continent(selected_continent['name'], int(selected_continent['id']))
    #returns an instance of a continent class
    return continent_instance

#get all countries in a single continent
def get_countries(input_continent_id):
    sql = 'SELECT * FROM countries WHERE continent_id = %s ORDER BY name'
    locations = run_sql(sql, [str(input_continent_id)])
    list_of_countries_in_continent = [ ]

    for row in locations:

        list_of_countries_in_continent.append(Country(row['name'], select_one(input_continent_id), int(row['id'])))

    #print(list_of_locations_in_country)
    return list_of_countries_in_continent

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
            print(countries_by_continent)
    #returns a list containing lists of countries
    return countries_by_continent