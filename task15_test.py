import unittest
from unittest.case import TestCase
from task15 import TankRush

class TankRushTest(unittest.TestCase):
    def testSuccess(self):
        self.assertEqual(TankRush(3, 4, "1234 2345 0987", 1, 1, "1"), True)
        self.assertEqual(TankRush(3, 4, "1234 2345 0987", 2, 2, "34 98"), True)
        self.assertEqual(TankRush(3, 4, "1234 2345 0987", 2, 2, "34 97"), False)
        self.assertEqual(TankRush(3, 4, "1234 2345 0987", 3, 3, "123 234 098"), True)

if __name__ == "__main__":
    unittest.main()