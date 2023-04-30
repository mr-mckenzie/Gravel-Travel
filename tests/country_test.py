import unittest
from models.country import Country

class TestCountryClass(unittest.TestCase):
    def setUp(self):
        self.ireland = Country("Ireland", 155)

    def test_country_has_name(self):
        self.assertEqual("Ireland", self.ireland.name)

    def test_country_has_id(self):
        self.assertEqual(155, self.ireland.id)
