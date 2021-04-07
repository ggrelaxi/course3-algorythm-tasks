import unittest

from task2 import odometer

class OdometerTest(unittest.TestCase):
    def test_success(self):
        self.assertEqual(odometer([10,1,20,2]), 30)
        self.assertEqual(odometer([20,1,30,2,40,5]), 170)

if __name__ == "__main__":
    unittest.main()