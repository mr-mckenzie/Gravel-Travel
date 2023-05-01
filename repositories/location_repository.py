from db.run_sql import run_sql

from models.location import Location

def save (location : Location):
    sql = 'INSERT INTO locations (name, country_id) VALUES (%s, %s) RETURNING id'
    values = (location.name, location.country.id)
    result = run_sql(sql, values)
    location.id = result[0]['id']
    return location

def select_all():
    sql = 'SELECT * FROM locations'
    results = run_sql(sql)
    #for row in results:
    #    print(row['name'])
    return results

def select_one(location_id):
    sql = 'SELECT * FROM locations WHERE id = (%s)'
    value = str(location_id)
    return run_sql(sql, value)[0]
