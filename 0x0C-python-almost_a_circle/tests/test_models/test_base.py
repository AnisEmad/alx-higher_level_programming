import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_unique_ids(self):
        b1 = Base()
        b2 = Base()
        self.assertNotEqual(b1.id, b2.id)

    def test_increment_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_assign_id(self):
        b1 = Base(89)
        b2 = Base(0)
        self.assertEqual(b1.id, 89)
        self.assertEqual(b2.id, 0)

if __name__ == "__main__":
    unittest.main()
