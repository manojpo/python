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
        list2 = ['ktm','parbat','er','qr','pokhara']
        expected = ['er','ktm','parbat','pokhara','qr']
        obj1 = Secondsem.front_end.camp.camp.mergesort(list2)
        self.assertEqual(obj1,expected)

    def test_insert(self):
        self.dbconnection = DbConnection()
        query = "insert into camp values(%s,%s,%s,%s,%s,%s,%s);"
        values = ('18', "ktm", 1, "Defense",132,1,"balaju")
        self.dbconnection.insert(query, values)
        expect = [('19', "ktm", 1, "Defense",132,1,"balaju")]
        actual = [('19', "ktm", 1, "Defense",132,1,"balaju")]
        self.assertEqual(expect, actual)

    def test_update(self):
        self.dbconnection = DbConnection()
        query = 'update camp set  Camp_Name=%s,  Camp_No=%s,Title=%s,contact=%s,Tent_No=%s,address=%s where Camp_ID=%s;'
        values = ('41', "ktm", 1, "Defense",132,1,"balaju")
        self.dbconnection.update(query, values)
        expect = [('41', "kt", 1, "Defense",132,1,"balaju")]
        actual = [('41', "kt", 1, "Defense",132,1,"balaju")]
        self.assertEqual(expect, actual)

    def test_delete(self):
        self.dbconnection = DbConnection()
        query = "delete from camp where Camp_ID=38;"
        values = ('1', "ktm", 4, "Defense",132,1,"balaju")
        expect = [("")]
        actual = [("")]
        self.assertEqual(expect, actual)

    #