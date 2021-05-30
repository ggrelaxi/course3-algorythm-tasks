import unittest
from task28 import Keymaker

class KeymakerTest(unittest.TestCase):
    def testSucces(self):
        self.assertEqual(Keymaker(10), "1001000010")
if __name__ == "__main__":
    unittest.main()