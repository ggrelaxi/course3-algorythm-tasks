import unittest
from task8 import SumOfThe

class SumOfTheTest(unittest.TestCase):
    def testSuccess(self):
        self.assertEqual(SumOfThe(7, [100, -50, 10, -25, 90, -35, 90]), 90)

if __name__ == "__main__":
    unittest.main()