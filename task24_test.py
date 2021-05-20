import unittest
from task24 import MatrixTurn

class MatrixTurnTest(unittest.TestCase):
    def testSuccess(self):
        matrix = ["123456", "234567", "345678", "456789"]
        turn = ["212345", "343456", "456767", "567898"]
        self.assertEqual(MatrixTurn(matrix, 4, 6, 1), turn)

if __name__ == "__main__":
    unittest.main()