from logging import basicConfig
import unittest
from task20 import BastShoe

class BastShoeTest(unittest.TestCase):
    def testSuccess(self):
        BastShoe("1 Привет")
        BastShoe("1 , Мир")
        BastShoe("2 5")
        self.assertEqual(BastShoe("3 1"), "р")




if __name__ == "__main__":
    unittest.main()