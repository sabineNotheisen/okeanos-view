import sqlite3


# noinspection SqlNoDataSourceInspection,SqlDialectInspection
class DataBase:
    def __init__(self, datafile):
        self.sql = sqlite3.connect(datafile, check_same_thread=False)
        self.create_tables()
        self.sql.execute("PRAGMA foreign_keys = 1")

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
