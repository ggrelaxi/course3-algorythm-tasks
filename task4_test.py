import unittest
import random
from task4 import MadMax


class MadMaxTest(unittest.TestCase):
    def testSuccess(self):
        self.assertEqual(MadMax(7, [1, 2, 3, 4, 5, 6, 7]), [1, 2, 3, 7, 6, 5, 4])
        self.assertEqual(MadMax(7, [1,3,2,4,6,5,7]), [1,2,3,7,6,5,4])

    def testSuccessRandom(self):
        randomLen = random.randrange(1 // 2, 10 // 2) * 2 + 1
        randomArray = []
        for i in range(randomLen):
            randomArray.append(random.randint(1, 255));
        correctResul = MadMax(randomLen, randomArray)
        self.assertEqual(MadMax(randomLen, randomArray), correctResul)

if __name__ == "__main__":
    unittest.main()