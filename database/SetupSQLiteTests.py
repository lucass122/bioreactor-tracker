import random
import sqlite3

# test class for creating SQLite3 database for Simon

# these 2 parameters set db name and row number of the tables in the sqlite database
from aifc import Error

DATABASE_NAME = 'birts_test_1.db'
ROW_NUMBER = 100000


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None

    try:
        # create table maira_data_db that contains all important data
        # setup db connection and cursor
        conn = sqlite3.connect(DATABASE_NAME)
        print(sqlite3.version)
        cursor = conn.cursor()
        return conn


    except Error as e:
        print(e)
    return conn


if __name__ == '__main__':
    conn = create_connection(DATABASE_NAME)
    cursor = conn.cursor()

    # creates test table birts_db
    # delete database if it already exists so recreating db is possible
    delete_command = """DROP TABLE IF EXISTS birts_db"""
    cursor.execute(delete_command)
    create_command = """CREATE TABLE IF NOT EXISTS birts_db(read_id INTEGER PRIMARY KEY,
    taxonomy TEXT,
    abundance INTEGER,
    sample_id INTEGER,
    project_id INTEGER,
    meta1 INTEGER,
    meta2 INTEGER,
    meta3 INTEGER,
    meta4 TEXT,
    meta5 TEXT,
    meta6 TEXT)"""

    # columns are as follows
    # read id (integer); read taxonomy ( text); abundance ( integer); sample id (integer); project id (integer); meta1 (integer); meta2 (integer); meta3 (integer); meta4 (text); meta5(text); meta6(text)
    # read taxonomy is the taxonomy parsed from maira
    # abundance is the bacterial abundance parsed from maira
    #  sample id is an integer that represents the ID of the sample the read originates from
    #  project id is integer that represents the ID of the project the read originates from
    #  meta1-meta6 are placeholders for metadata that may be included into the database in the future
    cursor.execute(create_command)

    # fills test table with 10.000 lines change upper limit to change database row number
    for i in range(1, ROW_NUMBER):
        cursor.execute(f"INSERT INTO birts_db VALUES ({i},'Clostridium Kluyveri', {random.randint(1, 100000)},"
                       f" {random.randint(1, 100000)}, {random.randint(1, 100000)}, {random.randint(1, 100000)},"
                       f" {random.randint(1, 100000)}, {random.randint(1, 100000)},'asdf','asdf','asdf')")

    cursor.execute("SELECT * FROM birts_db")

    results = cursor.fetchall()
    print(results)
    conn.commit()
    conn.close()
