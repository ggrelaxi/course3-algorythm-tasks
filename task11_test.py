import unittest
from task11 import BigMinus

class BigMinusTest(unittest.TestCase):
    def testSuccess(self):
        self.assertEqual(BigMinus("1234567891", "1"), "1234567890")
        self.assertEqual(BigMinus("1", "321"), "320")
        self.assertEqual(BigMinus("-1234567891", "1"), "1234567892")
if __name__ == "__main__":
    unittest.main()