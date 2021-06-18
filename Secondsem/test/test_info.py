import unittest
from Secondsem.model.info import *

class Test_info(unittest.TestCase):
    def test_get_Citizenship_No(self):
        e = info("2", "fg", "2", "Female", 86,76,'hg')
        self.assertEqual("2", e.get_Citizenship_No())

    def test_get_name(self):
        e = info("2", "fg", "2", "Female", 86,76,"hg")
        self.assertEqual("fg", e.get_name())




if __name__ == "__main__":
    unittest.main()
    


