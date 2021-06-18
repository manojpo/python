import unittest
import Secondsem.front_end.camp
from Secondsem.back_end.conarmyinfo import DbConnection

class Test_connection(unittest.TestCase):

    def test_linear_search(self):
        list1 = ['2','3','4','5']
        item = '4'
        obj = Secondsem.front_end.camp.camp.linear_search(list1, item)
        self.assertEqual(obj,'4')

    def test_mergesort(self):
        list2 = ['Sniper','LMG','SMG','AR']
        expected = ['AR','LMG','SMG','Sniper']
        obj1 = Secondsem.front_end.camp.camp.mergesort(list2)
        self.assertEqual(obj1,expected)

    def test_insert(self):
        self.dbconnection = DbConnection()
        query = "insert into wep values(%s,%s,%s,%s);"
        values = ('AR', "m416", 73, 100)
        self.dbconnection.insert(query, values)
        expect = [('AR', "m416", 73, 100)]
        actual = [('AR', "m416", 73, 100)]
        self.assertEqual(expect, actual)

    def test_update(self):
        self.dbconnection = DbConnection()

        query = 'update wep set  Weapon_type=%s,  Weapon_Name=%s,Bullet_qty=%s where Weapon_No=%s;'
        values = ('AR', 'Mk', 24, 100)
        self.dbconnection.update(query, values)
        expect = [('SMG', 'Mk', 24, 100)]
        actual = [('SMG', 'Mk', 24, 100)]
        self.assertEqual(expect, actual)

    def test_delete(self):
        self.dbconnection = DbConnection()
        query = "delete from wep where Weapon_No=38;"
        values = ('AR', "m416", 38, 100)
        expect = [("")]
        actual = [("")]
        self.assertEqual(expect, actual)