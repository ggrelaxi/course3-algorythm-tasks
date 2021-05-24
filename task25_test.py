import unittest
from task25 import TransformTransform

class TranformTransformTest(unittest.TestCase):
    def testSuccess(self):
        self.assertEqual(TransformTransform([3,2,1], 3), True)

if __name__ == "__main__":
    unittest.main()