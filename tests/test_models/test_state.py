#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.state import State


class TestModels(unittest.TestCase):
    def test_state_attributes(self):
        state = State()
        self.assertTrue(hasattr(state, 'name'))
        self.assertEqual(state.name, '')


if __name__ == '__main__':
    unittest.main()
