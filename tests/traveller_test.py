import unittest
from models.traveller import Traveller

class TestTravellerClass(unittest.TestCase):
    def setUp(self):
        self.new_user = Traveller("Xavier", "Brown", 48)

    def test_traveller_has_first_name(self):
        self.assertEqual("Xavier", self.new_user.first_name)

    def test_traveller_has_last_name(self):
        self.assertEqual("Brown", self.new_user.last_name)

    def test_traveller_has_id(self):
        self.assertEqual(48, self.new_user.id)