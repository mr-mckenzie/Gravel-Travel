#import run_sql function
from db.run_sql import run_sql

#import Location and Traveller classes
from models.location import Location
import repositories.location_repository as location_repo

#save holiday new record to database
def save (input_location: Location, input_date):
    sql = 'INSERT INTO holidays (location_id, date_visited) VALUES (%s, %s)'
    values = [input_location.id, input_date]
    run_sql(sql, values)
    #return print('SAVE SUCCESSFUL')

#select all holidays
def select_all():
    sql = 'SELECT * FROM holidays'
    all_holidays = run_sql(sql)
    holidays = [ ]
    for row in all_holidays:
        #print(f'ROW IS: {row}')
        row_location = location_repo.select_one(row[1])
        date = row[2]
        holiday_id = row[0]
        #print(row_location.__dict__)
        #print(date)
        holidays.append([row_location, date, holiday_id])

        #returns a list of holidays in the format [location_object, date] 
    return holidays

#select all holidays by location id
def select_by_location(input_location_id):
    sql = 'SELECT * FROM holidays WHERE location_id = %s'
    value = [str(input_location_id)]
    all_holidays = run_sql(sql, value)
    holidays = [ ]
    for row in all_holidays:
        row_location = location_repo.select_one(row[1])
        date = row[2]
        holiday_id = row[0]
        holidays.append([row_location, date, holiday_id])

    #returns a list of holidays in the format [location_object, date] 
    return holidays

#return a boolean representing if a location has been visited
def has_visited(input_location_id):
    sql = 'SELECT * FROM holidays where location_id = (%s)'
    result = run_sql(sql, [str(input_location_id)])
    #print(result)
    if result:
        return True
    else:
        return False
    
#delete a single holiday by id
def delete_by_id(input_id):
    sql = 'DELETE FROM holidays WHERE id = %s'
    value = [str(input_id)]
    run_sql(sql, value)