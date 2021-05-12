import unittest
from task23 import TreeOfLife

class TreeOfLifeTest(unittest.TestCase):
    def testSuccess(self):
        self.assertEqual(TreeOfLife(3,4,4,[".+..", "..+.", ".+.."]), [".+..", "..+.", ".+.."])

if __name__ == "__main__":
    unittest.main()