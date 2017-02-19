import MySQLdb
from database.database_config import *


# noinspection SqlNoDataSourceInspection,SqlDialectInspection
class DataBase:
    def __init__(self):
        self.sql = MySQLdb.connect(host=db_host, user=db_user, passwd=db_password, db=db_name)
        self.create_tables()

    def __del__(self):
        self.sql.close()

    def create_tables(self):
        c = self.sql.cursor()
        self.create_user_table(c)
        c.close()
        self.sql.commit()

    @staticmethod
    def create_user_table(c):
        c.execute('''CREATE TABLE IF NOT EXISTS user
                         (
                            id INTEGER PRIMARY KEY NOT NULL,
                            name TEXT,
                            forename TEXT
                         );''')
