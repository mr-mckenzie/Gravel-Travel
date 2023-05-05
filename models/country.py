from models.continent import Continent

class Country:
    def __init__(self, input_name, input_continent: Continent, input_id = None):
        #Country has property of name (string)
        self.name = input_name
        self.continent = input_continent
        #id is an optional varaible (of data type int) and defaults to None
        self.id = input_id