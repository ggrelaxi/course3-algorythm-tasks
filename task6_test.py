import unittest
from task6 import PatternUnlock

class PatternUnlockTest(unittest.TestCase):
    def successTest(self):
        self.assertEqual(PatternUnlock(3, [1,2,9]), "241421")
        self.assertEqual(PatternUnlock(9, [1,2,3,4,5,6,2,7,8,9]), "982843")

if __name__ == "__main__":
    unittest.main()