#import run_sql function
from db.run_sql import run_sql

#import Location and Traveller classes
from models.location import Location

def save (input_location: Location):
    sql = 'INSERT INTO wishlist (location_id) VALUES (%s)'
    value = (input_location.id)
    run_sql(sql, value)
    return #print('SAVE SUCCESSFUL')