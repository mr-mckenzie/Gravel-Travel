# import run_sql function
from db.run_sql import run_sql
# import Country class
from models.country import Country
from models.location import Location

# a function to save instances of country classes into the 'countries' db
def save(input_country: Country):
    sql = 'INSERT INTO countries (name) VALUES (%s) RETURNING (id)'
    values = [input_country.name]
    run_sql_return = run_sql(sql, values)
    #print(f"THIS IS THE 'run_sql_return' VARIABLE FROM SAVE COUNTRY: {run_sql_return}")
    id = run_sql_return[0]['id']
    input_country.id = id
    #               XXXXXX Unsure if I need to return the country in this function... make similar adjustment to traveller repo XXXXXX
    return input_country

def select_all():
    sql = 'SELECT * FROM countries'
    all_countries = run_sql(sql)
    #print('THIS IS THE RETURN OF RUN_SQL ON SELECT ALL:')
    all_results = []
    for row in all_countries:
        all_results.append(Country(row[1], int(row[0])))
    #returns instacnes of country classes in list format
    return all_results

def select_one(input_country_id):
    sql = 'SELECT * FROM countries WHERE id = (%s)'
    value = [str(input_country_id)]
    return_from_sql = run_sql(sql, value)
    #print(f'THIS IS THE RESULT FROM SELECT ONE COUNTRY {return_from_sql}')

    selected_country = return_from_sql[0]
    country_instance = Country(selected_country[1], int(selected_country[0]))
    #returns selected country as list
    return country_instance

def get_locations(input_country_id):
    sql = 'SELECT * FROM locations WHERE country_id = %s'
    locations = run_sql(sql, str(input_country_id))
    list_of_locations_in_country = [ ]
    #print("THIS IS THE GET LOCATIONS LIST:")
    for row in locations:

        list_of_locations_in_country.append(Location(row[1], select_one(input_country_id), int(row[0])))

        #print(row)
    #print(list_of_locations_in_country)
    return list_of_locations_in_country

def delete_by_id(input_id):
    sql = 'DELETE FROM countries WHERE id = (%s)'
    value = [str(input_id)]
    run_sql(sql, value)