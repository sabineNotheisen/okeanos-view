import MySQLdb
from database.database_config import *


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
                            id INTEGER PRIMARY KEY NOT NULL,
                            name TEXT,
                            forename TEXT
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
