#import run_sql function
from db.run_sql import run_sql

#import Country and Traveller classes
from models.location import Location
from models.traveller import Traveller

def save (input_traveller: Traveller, input_location: Location, input_date):
    sql = 'INSERT INTO holidays (traveller_id, location_id, date_visited) VALUES (%s, %s, %s)'
    values = (input_traveller.id, input_location.id, input_date)
    run_sql(sql, values)
    return #print('SAVE SUCCESSFUL')

def select_all():
    sql = 'SELECT * FROM holidays'
    all_holidays = run_sql(sql)
    #for row in all_holidays:
    #    print(row)
    return all_holidays

def select_one(input_holiday_id):
    sql = 'SELECT * FROM holidays WHERE id = %s'
    value = str(input_holiday_id)
    return run_sql(sql, value)[0]