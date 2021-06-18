import mysql.connector

class DbConnection:
    def __init__(self):
        self.con=mysql.connector.connect(host='localhost',user='root',password='',database='militarya')
        self.cursor=self.con.cursor()


    def insert(self,query,values):
        self.cursor.execute(query,values)
        self.con.commit()

    def update(self,query,values):
        self.cursor.execute(query,values)
        self.con.commit()

    def update2(self,query,values):
        self.cursor.execute(query, values)
        self.con.commit()



    def delete(self,query,values):
        self.cursor.execute(query,values)
        self.con.commit()

    def select1(self,query):
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        self.con.commit()
        return records

    def select2(self,query,values):
        self.cursor.execute(query,values)
        records=self.cursor.fetchall()
        self.con.commit()
        return records

    def fetch(self,query):
        self.cursor.execute(query)
        self.rows=self.cursor.fetchall()
        self.con.commit()

    def search_data(self,query):
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.con.commit()



