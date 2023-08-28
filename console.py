import repositories.continent_repository as cont_repo
import repositories.country_repository as country_repo
import repositories.location_repository as location_repo
import repositories.wishlist_repository as wishlist_repo
import repositories.trip_repository as trip_repo
from models.country import Country
from models.location import Location

country_iceland = Country("Iceland", cont_repo.select_one(3))
country_cuba = Country("Cuba", cont_repo.select_one(4))

country_repo.save(country_cuba)

location_reykavik = Location("Reykjavik", country_iceland)
location_havana = Location("Havana", country_cuba)

location_repo.save(location_havana)
trip_repo.save(location_havana, '2000-01-01', '7')