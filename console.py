import repositories.traveller_repository as traveller_repo
from models.traveller import Traveller

traveller_marco = Traveller("Marco", "Polo")
traveller_neil = Traveller("Neil", "Armstrong")

traveller_repo.save(traveller_marco)
traveller_repo.save(traveller_neil)

