import unittest
from task7 import WordSearch

class WordSearchTest(unittest.TestCase):
    def testSuccess(self):
        string = "1) строка разбивается на набор строк через выравнивание по заданной ширине."
        subStr = "строк"
        self.assertEqual(WordSearch(12, string, subStr), [0,0,0,1,0,0,0])
    
if __name__ == "__main__":
    unittest.main()