import unittest

from task26 import BalancedParentheses

class BalancedParenthesesTest(unittest.TestCase):
    def testSuccess(self):
        one = "()" 
        two = "(()) ()()"
        three = "((())) (()()) (())() ()(()) ()()()"

        self.assertEqual(BalancedParentheses(1), one)
        self.assertEqual(BalancedParentheses(2), two)
        self.assertEqual(BalancedParentheses(3), three)

if __name__ == "__main__":
    unittest.main()