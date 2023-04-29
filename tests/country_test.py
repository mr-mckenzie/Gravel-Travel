import unittest
from models.country import Country

class TestCountryClass(unittest.TestCase):
    def test_country_has_name(self):
        Ireland = Country("Ireland")
        self.assertEqual("Ireland", Ireland.name)