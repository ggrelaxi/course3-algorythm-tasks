import unittest
from task27 import Football

class FootballTest(unittest.TestCase):
    def testSuccess(self):
        self.assertEqual(Football([1,3,2], 3), True)
        self.assertEqual(Football([3,2,1], 3), True)
        self.assertEqual(Football([9,5,3,7,1], 5), False)

if __name__ == "__main__":
    unittest.main()