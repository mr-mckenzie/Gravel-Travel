import unittest
from models.location import Location
from models.country import Country

class TestLocationClass(unittest.TestCase):
    def setUp(self):
        self.italy = Country("Italy", 5)
        self.venice = Location("Venice", self.italy, 2)

    def test_location_has_name(self):
        self.assertEqual("Venice", self.venice.name)

    def test_location_has_country(self):
        self.assertEqual(self.italy, self.venice.country)

    def test_location_has_id(self):
        self.assertEqual(2, self.venice.id)