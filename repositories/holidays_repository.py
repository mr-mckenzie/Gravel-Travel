#import run_sql function
from db.run_sql import run_sql

#import Country and Traveller classes
from models.country import Country
from models.traveller import Traveller

def save (input_traveller: Traveller, input_country: Country, input_date):
    sql = 'INSERT INTO holidays (traveller_id, country_id, date_visited) VALUES (%s, %s, %s)'
    values = (input_traveller.id, input_country.id, input_date)
    run_sql(sql, values)
    return #print('SAVE SUCCESSFUL')