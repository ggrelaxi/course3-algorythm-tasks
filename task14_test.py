import unittest
from task14 import Unmanned

class UnmannedTest(unittest.TestCase):
    def testSuccess(self):
        self.assertEqual(Unmanned(10, 2, [[3,5,5], [5,2,2]]), 12)
        self.assertEqual(Unmanned(10, 1, [[3,5,5]]), 12)
        self.assertEqual(Unmanned(10, 2, [[11,5,5],[15,2,2]]), 10)

if __name__ == "__main__":
    unittest.main()