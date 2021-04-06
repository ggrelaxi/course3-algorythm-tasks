import unittest
from task1 import squirrel

class SquirrelTest(unittest.TestCase):
    def testSuccess(self):
        self.assertEqual(squirrel(4), 2)
        self.assertEqual(squirrel(5), 1)
        self.assertEqual(squirrel(15), 1)

if __name__ == "__main__":
    unittest.main()