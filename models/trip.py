from models.location import Location

class Trip:
    def __init__(self, input_location:Location, input_date = None, input_length = None, input_id = None):
        self.location = input_location
        self.date = input_date
        self.length = input_length
        self.id = input_id