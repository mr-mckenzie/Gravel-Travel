import repositories.traveller_repository as traveller_repo
import repositories.country_repository as country_repo
import repositories.travellers_countries_repository as t_c_repo
from models.traveller import Traveller
from models.country import Country

traveller_marco = Traveller("Marco", "Polo")
traveller_neil = Traveller("Neil", "Armstrong")

#traveller_repo.save(traveller_marco)
#traveller_repo.save(traveller_neil)

#print(traveller_marco.__dict__)

country_iceland = Country("Iceland")
country_cuba = Country("Cuba")

#country_repo.save(country_iceland)
#country_repo.save(country_cuba)

#print(country_cuba.__dict__)

#t_c_repo.save(traveller_marco, country_iceland, '2002-02-02')
#t_c_repo.save(traveller_neil, country_cuba, '2005-05-05') 