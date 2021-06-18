import unittest
from Secondsem.model.weap import *


class Test_weap(unittest.TestCase):
    def test_get_Weapon_No(self):
        e = weap("AR", "m416", 1, 180)
        self.assertEqual(1, e.get_Weapon_No())

    def test_get_Weapon_Name(self):
        e = weap("AR", "m416", 1, 180)
        self.assertEqual("m416", e.get_Weapon_Name())


if __name__ == "__main__":
    unittest.main()






