import unittest
from task5 import SynchronizingTables

class SynchronizingTables(unittest.TestCase):
    def successTest(self):
        self.assertEqual(SynchronizingTables(3, [50,1,1024], [20000, 100000, 90000]), [90000, 20000, 100000])

if __name__ == "__main__":
    unittest.main()