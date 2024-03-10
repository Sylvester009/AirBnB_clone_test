#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestModels(unittest.TestCase):
    def test_review_attributes(self):
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertEqual(review.place_id, '')
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertEqual(review.user_id, '')
        self.assertTrue(hasattr(review, 'text'))
        self.assertEqual(review.text, '')


if __name__ == '__main__':
    unittest.main()
