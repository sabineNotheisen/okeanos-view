import MySQLdb
from database.database_config import *
from database.tables import *


# noinspection SqlNoDataSourceInspection,SqlDialectInspection
class DataBase:
    def __init__(self):
        self.conn = MySQLdb.connect(host=db_host, user=db_user, passwd=db_password, db=db_name)
        self.create_tables()

    def create_tables(self):
        self.create_user_table()

    def execute_request(self, request):
        cursor = self.conn.cursor()
        cursor.execute(request)
        return cursor

    def insert_request(self, request):
        cursor = self.execute_request(request)
        self.conn.commit()
        cursor.close()

    def create_user_table(self):
        request = '''CREATE TABLE IF NOT EXISTS user
                         (
                            '''+get_user_table()+'''
                         );'''
        self.insert_request(request)

    def get_all_columns_of_table(self, table):
        request = '''select column_name, column_type from information_schema.columns
                     where table_schema = "''' + db_name + '''"
                     and table_name = "''' + table + '''''''"'''
        cursor = self.execute_request(request)
        columns = [column for column in self.execute_request(request)]
        cursor.close()
        return columns

    def register_user(self, data):
        columns = self.get_all_columns_of_table("user")
        query = "INSERT INTO `user` ("
        for column_name, column_type in columns:
            if column_name != "id":
                query += "`"+column_name+"`, "
        query = query[:-2] + ") VALUES ("
        for column_name, column_type in columns:
            if column_name != "id":
                query += "NULL" if (data[column_name] == '') else "'" + data[column_name] + "'"
                query += ", "
        query = query[:-2] + ")"
        self.insert_request(query)
