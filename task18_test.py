import unittest
from task18 import MisterRobot
import time

class MisterRobotTest(unittest.TestCase):
    def testSuccess(self):
        self.assertEqual(MisterRobot(7, [1,3,4,5,6,2,7]), True)
        self.assertEqual(MisterRobot(7, [1,4,3,5,7,6,2]), True)
    def testTime(self):
        startTime = time.time()
        MisterRobot(7, [1,4,3,5,7,6,2])
        endTime = time.time()
        self.assertLess((endTime - startTime), 1)
if __name__ == "__main__":
    unittest.main()