import unittest
from task13 import UFO

class UFOTest(unittest.TestCase):
    def testSuccess(self):
        self.assertEqual(UFO(2, [1234,1777], False), [4660,6007]);
        self.assertEqual(UFO(2, [1234,1777], True), [668,1023]);

if __name__ == "__main__":
    unittest.main()