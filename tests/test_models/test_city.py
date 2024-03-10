#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.city import City


class TestModels(unittest.TestCase):
    def test_city_attributes(self):
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertEqual(city.state_id, '')
        self.assertTrue(hasattr(city, 'name'))
        self.assertEqual(city.name, '')


if __name__ == '__main__':
    unittest.main()
