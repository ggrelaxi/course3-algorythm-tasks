import unittest
from task7 import WordSearch

class WordSearchTest(unittest.TestCase):
    def testSuccess(self):
        string = "1) строка разбивается на набор строк через выравнивание по заданной ширине."
        subStr = "строк"
        self.assertEqual(WordSearch(12, string, subStr), [0,0,0,1,0,0,0])
    
    def testSuccessBigWord(self):
        string = "1) строка разбивается на набор строк через выравниванием по заданной ширине."
        subStr = "строк"
        self.assertEqual(WordSearch(12, string, subStr), [0,0,0,1,0,0,0,0])

    def testSuccessSingleWord(self):
        string = "12345"
        subStr = "123"
        self.assertEqual(WordSearch(3, '12345', '123'), [1,0])

    def testSuccessSingleWordOneMore(self):
        string = "12345"
        subStr = "123"
        self.assertEqual(WordSearch(3, '12345', '45'), [0,1])
    
if __name__ == "__main__":
    unittest.main()