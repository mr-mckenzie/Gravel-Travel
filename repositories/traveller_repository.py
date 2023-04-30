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