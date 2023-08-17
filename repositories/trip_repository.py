#import run_sql function
from db.run_sql import run_sql

#import Location class
from models.location import Location
import repositories.location_repository as location_repo

from models.trip import Trip

#save new trip record to database
def save (input_location: Location, input_date, input_length = None, input_wishlist = False):
    sql = 'INSERT INTO trips (location_id, date_visited, length_of_visit, wishlist) VALUES (%s, %s, %s, %s)'
    values = [input_location.id, input_date, input_length, input_wishlist]
    run_sql(sql, values)
    #return print('SAVE SUCCESSFUL')

#select all trips
def select_all_trips():
    sql = 'SELECT * FROM trips where wishlist = FALSE order by date_visited DESC'
    results = run_sql(sql)
    trips = [ ]
    for row in results:
        location = location_repo.select_one(row['location_id'])
        date = row['date_visited']
        length = row['length_of_visit']
        trip_id = row['id']
        new_trip = Trip(location, date, length, trip_id)
        trips.append(new_trip)
        
    return trips

#select all trips by location id
def select_by_location(input_location_id):
    sql = 'SELECT * FROM trips WHERE location_id = %s'
    value = [str(input_location_id)]
    results = run_sql(sql, value)
    trips = [ ]
    for row in results:
        location = location_repo.select_one(row['location_id'])
        date = row['date_visited']
        length = row['length_of_visit']
        trip_id = row['id']
        new_trip = Trip(location, date, length, trip_id)
        trips.append(new_trip)

    #returns a list of trip objects 
    return trips

#return a boolean representing if a location has been visited
def has_visited(input_location_id):
    sql = 'SELECT * FROM trips WHERE location_id = (%s) AND wishlist = FALSE'
    result = run_sql(sql, [str(input_location_id)])
    if result:
        return True
    else:
        return False
    
#count how many times a location has been visited
def number_of_visits(input_location_id):
    sql = 'SELECT * FROM trips WHERE location_id = (%s) AND wishlist = FALSE'
    result = run_sql(sql, [str(input_location_id)])

    return len(result)

#count how many days total travelled
def days_travelled():
    sql = 'SELECT * FROM trips where wishlist = FALSE'
    results = run_sql(sql)
    counter = 0
    for row in results:
        counter += row['length_of_visit']

    return counter

#count how many days total travelled in a single country
def days_travelled_in_location(input_location_id):
    sql = 'SELECT * FROM trips where location_id = (%s) AND wishlist = FALSE'
    results = run_sql(sql, [str(input_location_id)])
    counter = 0
    for row in results:
        counter += row['length_of_visit']

    return counter

#delete a single trip by id
def delete_by_id(input_id):
    sql = 'DELETE FROM trips WHERE id = %s'
    value = [str(input_id)]
    run_sql(sql, value)

#return a boolean representing if a location is on the wishlist
def on_wishlist(input_location_id):
    sql = 'SELECT * FROM trips WHERE location_id = (%s) AND wishlist = TRUE'
    result = run_sql(sql, [str(input_location_id)])
    if result:
        return True
    else:
        return False

#select all wishlist records
def select_all_wishlist():
    sql = 'SELECT * FROM trips where wishlist = TRUE'
    results = run_sql(sql)
    wishlist = [ ]
    for row in results:
        #print(f'ROW IS: {row}')
        location = location_repo.select_one(row['location_id'])
        wishlist.append(location)

    return wishlist

#save a location to the wishlist db
def add_to_wishlist(input_location_id, input_date = None, input_length = None, input_wishlist = True):
    sql = 'INSERT INTO trips (location_id, date_visited, length_of_visit, wishlist) VALUES (%s, %s, %s, %s)'
    values = [input_location_id, input_date, input_length, input_wishlist]
    run_sql(sql, values)


# #delete a wishlist record by the location_id
def delete_wishlist_by_location_id(input_location_id):
    sql = 'DELETE FROM trips WHERE location_id = %s AND wishlist = TRUE'
    value = [str(input_location_id)]
    run_sql(sql, value)