#!/usr/bin/python3
"""
Module for BaseModel unittest
"""
import os
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_init(self):
        model = BaseModel()
        self.assertIsNotNone(model.id)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str(self):
        model = BaseModel()
        expected_str = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(str(model), expected_str)

    def test_save(self):
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_to_dict(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('__class__', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], model.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()
