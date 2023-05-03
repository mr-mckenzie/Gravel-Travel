from db.run_sql import run_sql

from models.location import Location
import repositories.country_repository as country_repo

#save a new location to the database
def save (location : Location):
    sql = 'INSERT INTO locations (name, country_id) VALUES (%s, %s) RETURNING id'
    values = [location.name, location.country.id]
    result = run_sql(sql, values)
    location.id = result[0]['id']
    return location

#select all locations
def select_all():
    sql = 'SELECT * FROM locations'
    results = run_sql(sql)
    location_list = [ ]
    for row in results:
        location_country = country_repo.select_one(row[2])
        new_location = Location(row[1], location_country, int(row[0]))
        location_list.append(new_location)
    #    print(row['name'])
    return location_list

#select a single location by id
def select_one(location_id):
    sql = 'SELECT * FROM locations WHERE id = %s'
    value = [str(location_id)]
    #print("PRINTING THIS")
    #print(value)
    return_from_sql = run_sql(sql, value)
    #print(f'THIS IS THE RESULT FROM SELECT ONE LOCATION {return_from_sql}')
    result = return_from_sql[0]
    selected_country = country_repo.select_one(result[2])
    selected_location = Location(result[1], selected_country, int(result[0]))
    return selected_location

#delete a location by id
def delete_by_id(input_id):
    sql = 'DELETE FROM locations WHERE id = (%s)'
    value = [str(input_id)]
    run_sql(sql, value)
