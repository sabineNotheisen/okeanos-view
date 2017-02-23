import MySQLdb
from database.database_config import *
from database.tables import *
from database.tables_init import *


# noinspection SqlNoDataSourceInspection,SqlDialectInspection
class DataBase:
    def __init__(self):
        self.conn = MySQLdb.connect(host=db_host, user=db_user, passwd=db_password, db=db_name)

    def create_tables(self):
        self.create_table('type_of_adherent', get_type_of_adherent_table())
        self.init_table('type_of_adherent', get_init_of_type_of_adherent_table())
        self.create_table('adherent', get_adherent_table())

    def execute_request(self, request):
        cursor = self.conn.cursor()
        cursor.execute(request)
        return cursor

    def insert_request(self, request):
        cursor = self.execute_request(request)
        self.conn.commit()
        cursor.close()

    def create_table(self, table, definition):
        request = '''CREATE TABLE IF NOT EXISTS ''' + table + ''' ('''+definition+''');'''
        self.insert_request(request)

    def init_table(self, table, insertions):
        for insertion in insertions:
            query = "INSERT INTO "+table+" VALUES ('', "
            for value in insertion:
                query += "'" + value + "', "
            query = query[:-2] + ")"
            self.insert_request(query)

    def get_all_columns_of_table(self, table):
        request = '''select column_name, column_type from information_schema.columns
                     where table_schema = "''' + db_name + '''"
                     and table_name = "''' + table + '''''''"'''
        cursor = self.execute_request(request)
        columns = [column for column in cursor]
        cursor.close()
        return columns

    def register_adherent(self, data):
        columns = self.get_all_columns_of_table("adherent")
        query = "INSERT INTO `adherent` ("
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

    def find_all(self, table):
        request = '''select * from '''+table
        cursor = self.execute_request(request)
        columns = self.get_all_columns_of_table(table)
        adherents = []
        for adherent in cursor:
            current_adherent = {}
            key = 0
            for column_name, column_type in columns:
                current_adherent[column_name] = adherent[key]
                key += 1
            adherents.append(current_adherent)
        cursor.close()
        return adherents
