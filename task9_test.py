import unittest
from task9 import TheRabbitsFoot

class TheRabbitsFootTest(unittest.TestCase):
    def successTest(self):
        str = "отдай мою кроличью лапку"
        self.assertEqual(TheRabbitsFoot("отдай мою кроличью лапку", True), "омоюу толл дюиа акчп йрьк")
        self.assertEqual(TheRabbitsFoot(str, False), )

if __name__ == "__main__":
    unittest.main()