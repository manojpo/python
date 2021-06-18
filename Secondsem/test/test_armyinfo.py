import unittest
import Secondsem.front_end.armyinfo
from Secondsem.back_end.conarmyinfo import DbConnection

class Test_connection(unittest.TestCase):

    def test_linear_search(self):
        list1 = ['1','3','4','5','9','11']
        item = '4'
        obj = Secondsem.front_end.armyinfo.armyinfo.linear_search(list1, item)
        self.assertEqual(obj,'4')

    def test_mergesort(self):
        list2 = ['vivek','manoj','kushwaha','poudel']
        expected = ['kushwaha','manoj','poudel','vivek']
        obj1 = Secondsem.front_end.armyinfo.armyinfo.mergesort(list2)
        self.assertEqual(obj1,expected)

    def test_insert(self):
        self.dbconnection = DbConnection()
        query = "insert into info values(%s,%s,%s,%s,%s,%s,%s);"
        values = ('61', "ram", "2", "Male", 132, 5, "Captain")
        self.dbconnection.insert(query, values)
        expect = [('61', "ram", "2", "Male", 132, 5, "Captain")]
        actual = [('61', "ram", "2", "Male", 132, 5, "Captain")]
        self.assertEqual(expect, actual)

    def test_update(self):
        self.dbconnection = DbConnection()
        query = 'update info set name=%s,  Camp_ID=%s,gender=%s,contact=%s,height=%s,post=%s where Citizenship_No=%s;'
        values = ('1', "jack", '1', "Male", 132, 6, "laptan")
        self.dbconnection.update(query, values)
        expect = [('1', "jackie", '1', "Male", 132, 6, "laptan")]
        actual = [('1', "jackie", '1', "Male", 132, 6, "laptan")]
        self.assertEqual(expect, actual)


    def test_delete(self):
        self.dbconnection = DbConnection()
        query = "delete from camp where Citizenship_No=31;"
        values = ('1', "ram", '1', "Male", 132, 5, "Captain")
        expect = [("")]
        actual = [("")]
        self.assertEqual(expect, actual)
