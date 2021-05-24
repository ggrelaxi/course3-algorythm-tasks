import unittest
from task25 import TransformTransform

class TranformTransformTest(unittest.TestCase):
    def testSuccess(self):
        self.assertEqual(TransformTransform([1,2,3,4,5,6,7], 7), True)

if __name__ == "__main__":
    unittest.main()