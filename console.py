#import repositories.traveller_repository as traveller_repo
import repositories.country_repository as country_repo
import repositories.holiday_repository as holiday_repo
import repositories.location_repository as location_repo
import repositories.wishlist_repository as wishlist_repo
#from models.traveller import Traveller
from models.country import Country
from models.location import Location

country_iceland = Country("Iceland")
country_cuba = Country("Cuba")

country_repo.save(country_iceland)
country_repo.save(country_cuba)

#print(country_cuba.__dict__)

location_reykavik = Location("Reykjavik", country_iceland)
location_havana = Location("Havana", country_cuba)

location_repo.save(location_reykavik)
location_repo.save(location_havana)

#print(location_havana.__dict__)

holiday_repo.save(location_reykavik, '2002-02-02')
holiday_repo.save(location_havana, '2005-05-05') 

#wishlist_repo.save(location_havana)
#wishlist_repo.save(location_reykavik)

all_countries = country_repo.select_all()
#print(f'ALL COUNTRIES = {all_countries}')

one_country = country_repo.select_one(3)
#print(f'SINGLE COUNTRY = {one_country.__dict__}')

#all_travellers = traveller_repo.select_all()
#print(f'ALL TRAVELLERS = {all_travellers}')

#one_traveller = traveller_repo.select_one(2)
#print(f'SINGLE TRAVELLER = {one_traveller}')

#all_holidays = holiday_repo.select_all()
#print(f'ALL HOLIDAYS = {all_holidays}')

#one_holiday = holiday_repo.select_one(4)
#print(f'SINGLE HOLIDAY = {one_holiday}')

all_locations = location_repo.select_all()
#print(f'ALL LOCATIONS: {all_locations}')
#for locale in all_locations:
#    print(locale.__dict__)

one_location = location_repo.select_one(5)
#print(f'SINGLE LOCATION: {one_location.__dict__}')

locations_in_country = country_repo.get_locations(2)
#print("LOCATIONS IN COUNTRY: ")
#for location in locations_in_country:
#    print(location.__dict__)

all_holidays = holiday_repo.select_all()
print(all_holidays)

print(holiday_repo.has_visited(1))
print(holiday_repo.has_visited(2))

#wishlist_repo.delete_by_location_id(7)