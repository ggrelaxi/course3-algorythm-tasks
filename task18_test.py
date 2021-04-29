import unittest
from task18 import MisterRobot

class MisterRobotTest(unittest.TestCase):
    def testSuccess(self):
        self.assertEqual(MisterRobot(7, [1,3,4,5,6,2,7]), True)

if __name__ == "__main__":
    unittest.main()