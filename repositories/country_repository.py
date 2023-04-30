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