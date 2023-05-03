#import run_sql function
from db.run_sql import run_sql

import repositories.location_repository as location_repo

#save a location to the wishlist db
def save (input_location_id):
    sql = 'INSERT INTO wishlist (location_id) VALUES (%s)'
    value = [input_location_id]
    run_sql(sql, value)
    #return print('SAVE SUCCESSFUL')

#select all wishlist records
def select_all():
    sql = 'SELECT * FROM wishlist'
    all_wishlist = run_sql(sql)
    wishlist = [ ]
    for row in all_wishlist:
        row_location = location_repo.select_one(row[1])
        wishlist.append(row_location)
        #returns a list of wishlist location objects
    print(f'THIS IS THE WISHLIST: {wishlist}')
    return wishlist

#returns a boolean to show if a location is on the wishlist
def on_wishlist(input_location_id):
    sql = 'SELECT * FROM wishlist where location_id = (%s)'
    result = run_sql(sql, [str(input_location_id)])
    #print(result)
    if result:
        return True
    else:
        return False

#delete a wishlist record by the location_id
def delete_by_location_id(input_location_id):
    sql = 'DELETE FROM wishlist WHERE location_id = %s'
    value = [str(input_location_id)]
    run_sql(sql, value)