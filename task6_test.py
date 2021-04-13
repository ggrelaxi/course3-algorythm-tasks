import unittest
from task6 import PatternUnlock

class PatternUnlockTest(unittest.TestCase):
    def successTest(self):
        self.assertEqual(PatternUnlock(9, [1,2,3,4,5,6,7,8,9]), "45")

if __name__ == "__main__":
    unittest.main()