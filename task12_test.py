import unittest
from task12 import MassVote

class MassVoteTest(unittest.TestCase):
    def testSuccess(self):
        self.assertEqual(MassVote(5, [60,10,10,15,5]), "majority winner 1")
        self.assertEqual(MassVote(3, [10,15,10]), "minority winner 2")
        self.assertEqual(MassVote(3, [10,10,10]), "no winner")

if __name__ == "__main__":
    unittest.main()