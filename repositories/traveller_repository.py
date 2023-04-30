# import run_sql function
from db.run_sql import run_sql
# import Traveller class
from models.traveller import Traveller

def save (traveller: Traveller):
    sql = 'INSERT INTO travellers (first_name, last_name) VALUES (%s, %s) RETURNING id'
    values = [traveller.first_name, traveller.last_name]
    results = run_sql(sql, values)
    #print(f"THIS IS THE RESULTS VARIABLE: {results}")
    traveller.id = results[0]['id']
    return traveller

def select_all():
    sql = 'SELECT * FROM travellers'
    all_travellers = run_sql(sql)
    #for row in all_travellers:
    #    print(row)
    return all_travellers

def select_one(input_traveller_id):
    sql = 'SELECT * FROM travellers WHERE id = %s'
    value = str(input_traveller_id)
    single_traveller = run_sql(sql, value)
    return single_traveller[0]