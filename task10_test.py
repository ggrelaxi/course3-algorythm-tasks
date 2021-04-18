import unittest
from task10 import PrintingCosts

class PrintingCostsTest(unittest.TestCase):
    def testSuccess(self):
        string = "123"
        self.assertEqual(PrintingCosts(string), 64)

if __name__ == "__main__":
    unittest.main()