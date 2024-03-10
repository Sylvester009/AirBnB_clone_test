#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestModels(unittest.TestCase):
    def test_amenity_attributes(self):
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(amenity.name, '')


if __name__ == '__main__':
    unittest.main()
