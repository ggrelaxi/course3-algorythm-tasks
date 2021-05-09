import unittest
from task22 import SherlockValidString

class SherlockValidStringTest(unittest.TestCase):
    def testSuccess(self):
        self.assertEqual(SherlockValidString("xyz"), True)
        self.assertEqual(SherlockValidString("xxyyz"), True)
        self.assertEqual(SherlockValidString("xxyyz"), True)
        self.assertEqual(SherlockValidString("xyzzz"), None)
        self.assertEqual(SherlockValidString("xxyyza"), None)
        self.assertEqual(SherlockValidString("xxyyzabc"), None)
    
if __name__ == "__main__":
    unittest.main()