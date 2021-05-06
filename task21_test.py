import unittest
from task21 import BiggerGreater

class BiggerGreaterTest(unittest.TestCase):
    def testSuccess(self):
        self.assertEqual(BiggerGreater("ая"), "яа")
        self.assertEqual(BiggerGreater("fff"), "")
        self.assertEqual(BiggerGreater("нклм"), "нкмл")
        self.assertEqual(BiggerGreater("вибк"), "викб")
        self.assertEqual(BiggerGreater("вкиб"), "ибвк")

if __name__ == "__main__":
    unittest.main()