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
    list_of_travellers = []
    for row in all_travellers:
        list_of_travellers.append(Traveller(row[1], row[2], row[0]))
    #    print(row)
    return list_of_travellers

def select_one(input_traveller_id):
    sql = 'SELECT * FROM travellers WHERE id = %s'
    value = str(input_traveller_id)
    single_traveller = run_sql(sql, value)[0]
    #print(single_traveller)
    traveller_instance = Traveller(single_traveller[1], single_traveller[2], single_traveller[0])
    return traveller_instance