import unittest
from task16 import MaximumDiscount

class MaximumDiscountTest(unittest.TestCase):
    def testSuccess(self):
        self.assertEqual(MaximumDiscount(3, [400,300,250]), 250)
        self.assertEqual(MaximumDiscount(7, [400,350,300,250,200,150,100]), 450)

if __name__ == "__main__":
    unittest.main()