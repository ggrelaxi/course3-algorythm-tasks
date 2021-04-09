import unittest
from task3 import ConquestCampaign

class ConquestCampaignTest(unittest.TestCase):
    def testSuccess(self):
        self.assertEqual(ConquestCampaign(3, 4, 2, [2,2, 3,4]), 3)
        self.assertEqual(ConquestCampaign(3, 4, 2, [2,2, 2,2]), 4)
        self.assertEqual(ConquestCampaign(4, 5, 3, [2,2, 3,4, 2,5]), 4)
        self.assertEqual(ConquestCampaign(2,3,6,[1,1,1,2,1,3,2,1,2,2,2,3]), 1)

if __name__ == "__main__":
    unittest.main()