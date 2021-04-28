import unittest
from task17 import LineAnalysis

class LineAnalysisTest(unittest.TestCase):
    def testSuccess(self):
        self.assertEqual(LineAnalysis("*"), True)
        self.assertEqual(LineAnalysis("***"), True)
        self.assertEqual(LineAnalysis("*.......*.......*"), True)
        self.assertEqual(LineAnalysis("**"), True)
        self.assertEqual(LineAnalysis("*.*"), True)
        self.assertEqual(LineAnalysis("*..*...*..*..*..*..*"), False)
        self.assertEqual(LineAnalysis("*..*..*..*..*..**..*"), False)
        self.assertEqual(LineAnalysis('*......*.......*'), False)

if __name__ == "__main__":
    unittest.main()
