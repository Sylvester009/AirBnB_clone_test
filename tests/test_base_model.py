#!/usr/bin/python3
import unittest
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}"
          .format(key, type(my_model_json[key]), my_model_json[key]))


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        model = BaseModel()
        self.assertIsNotNone(model.id)
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(model.updated_at)

    def test_save(self):
        model = BaseModel()
        initial_updated_at = model.updated_at
        curr_updated_at = model.save()
        self.assertNotEqual(initial_updated_at, curr_updated_at)

    def test_to_dict(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'],
                         model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'],
                         model.updated_at.isoformat())

    def test_str(self):
        """
        Test for string representation
        """
        model = BaseModel()
        self.assertTrue(str(model).startswith('[BaseModel]'))
        self.assertIn(model.id, str(model))
        self.assertIn(str(model.__dict__), str(model))


if __name__ == "__main__":
    unittest.main()
