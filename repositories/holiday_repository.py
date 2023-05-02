#import run_sql function
from db.run_sql import run_sql

#import Location and Traveller classes
from models.location import Location
import repositories.location_repository as location_repo

def save (input_location: Location, input_date):
    sql = 'INSERT INTO holidays (location_id, date_visited) VALUES (%s, %s)'
    values = (input_location.id, input_date)
    run_sql(sql, values)
    return #print('SAVE SUCCESSFUL')

# XXXXXXXX   STILL TO UPDATE   XXXXXXX
# XXXXXXXX        BELOW        XXXXXXX
def select_all():
    sql = 'SELECT * FROM holidays'
    all_holidays = run_sql(sql)
    holidays = [ ]
    for row in all_holidays:
        #print(row)
        row_location = location_repo.select_one(row[1])
        date = row[2]
        #print(row_location.__dict__)
        #print(date)
        holidays.append([row_location, date])

        #returns a list of holidays in the format [location_object, date] 
    return holidays

#def select_one(input_holiday_id):
#    sql = 'SELECT * FROM holidays WHERE id = %s'
#    value = str(input_holiday_id)
#    return run_sql(sql, value)[0]

#NEED FUNCTIONS TO DISPLAY VISITED FOR ONE TRAVELLER ID

def has_visited(input_location_id):
    sql = 'SELECT * FROM holidays where location_id = (%s)'
    result = run_sql(sql, str(input_location_id))
    print(result)
    if result:
        return True
    else:
        return False
    
# def list_of_visited():
#     sql = 'SELECT * FROM holidays'
#     all_records = run_sql(sql)
#     location_ids_visited = []
#     for row in all_records:
#         if