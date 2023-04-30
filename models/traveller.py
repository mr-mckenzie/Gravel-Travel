class Traveller:
    def __init__(self, input_first_name:str, input_last_name:str, input_id = None):
        #User has properties of a first name (first_name) and a last name (last_name)
        #Both are of data type: string
        self.first_name = input_first_name
        self.last_name = input_last_name
        #id is an optional varaible (of data type int) and defaults to None
        self.id = input_id