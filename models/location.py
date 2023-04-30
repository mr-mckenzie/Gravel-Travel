#               Not sure if this import is neccesary...
from models.country import Country

class Location:
    def __init__(self, input_name, input_country:Country, input_id = None):
        self.name = input_name
        self.country = input_country
        self.id = input_id