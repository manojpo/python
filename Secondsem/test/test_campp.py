import unittest
from Secondsem.model.campp import *


class Test_campp(unittest.TestCase):
    def test_get_Camp_ID(self):
        e = campp("2", "Pokhara", 10, "Sniper", 1234,5,'New Road')
        self.assertEqual("2", e.get_Camp_ID())

    def test_get_Camp_Name(self):
        e = campp("2", "Pokhara", 10, "Sniper", 1234,5,"New Road")
        self.assertEqual("Pokhara", e.get_Camp_Name())




if __name__ == "__main__":
    unittest.main()






#







