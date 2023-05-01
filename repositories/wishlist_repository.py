#import run_sql function
from db.run_sql import run_sql

#import Location and Traveller classes
from models.location import Location
from models.traveller import Traveller

def save (input_traveller: Traveller, input_location: Location):
    sql = 'INSERT INTO wishlist (traveller_id, location_id) VALUES (%s, %s)'
    values = (input_traveller.id, input_location.id)
    run_sql(sql, values)
    return #print('SAVE SUCCESSFUL')