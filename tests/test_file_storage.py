import unittest
import os
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_new_and_save(self):
        self.assertEqual(len(self.storage.all()), 0)
        self.storage.new({"id": "123", "name": "Test"})
        self.storage.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))
        with open(self.storage._FileStorage__file_path, 'r') as f:
            data = f.read()
            self.assertIn("123", data)
            self.assertIn("Test", data)

    def test_reload(self):
        self.storage.new({"id": "456", "name": "Reload Test"})
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        self.assertEqual(len(new_storage.all()), 1)
        self.assertIn("456", new_storage.all())

if __name__ == '__main__':
    unittest.main()
