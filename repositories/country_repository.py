# import run_sql function
from db.run_sql import run_sql
# import Country class
from models.country import Country

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
    sql = 'SELECT * FROM countries WHERE id = %s'
    value = str(input_country_id)
    selected_country = run_sql(sql, value)[0]
    country_instance = Country(selected_country[1], int(selected_country[0]))
    #returns selected country as list
    return country_instance