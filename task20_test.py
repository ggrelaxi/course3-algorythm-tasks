import unittest
from task20 import BastShoe

class BastShoeTest(unittest.TestCase):
    def testSuccess(self):
        self.assertEqual(BastShoe("1 Привет"), "Привет")

if __name__ == "__main__":
    unittest.main()