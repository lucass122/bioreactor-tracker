import sqlite3

import pandas as pd


class SQLiteToPandas():

    def __init__(self, path_to_sqlite_db, table_name):
        self.path_to_sqlite_db = path_to_sqlite_db
        self.table_name = table_name

    def sqlite_to_pandas(self):
        con = sqlite3.connect(self.path_to_sqlite_db)
        df = pd.read_sql_query(f"SELECT * from {self.table_name}", con)
        # print(df)
        con.close()
        return df
