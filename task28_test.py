import unittest
from task28 import Keymaker

class KeymakerTest(unittest.TestCase):
    def testSucces(self):
        self.assertEqual(Keymaker(4), "1000")
if __name__ == "__main__":
    unittest.main()