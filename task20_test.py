from logging import basicConfig
import unittest
from task20 import BastShoe

class BashShoeGetSymbolTest(unittest.TestCase):
    def testGetSymbol(self):
        BastShoe("1 a")
        BastShoe("1 b")
        BastShoe("1 c")
        BastShoe("1 d")
        self.assertEqual(BastShoe("1 e"), "abcde")
        self.assertEqual(BastShoe("3 0"), "a")
        self.assertEqual(BastShoe("3 4"), "e")

if __name__ == "__main__":
    unittest.main()