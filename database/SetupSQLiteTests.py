import random
import sqlite3

# test class for creating SQLite3 database for Simon

# these 2 parameters set db name and row number of the tables in the sqlite database
from aifc import Error


def inc_sample_id(index, variable_to_inc):
    if (index % 14) == 0:
        variable_to_inc = variable_to_inc + 1
        return (variable_to_inc)
    return (variable_to_inc)


DATABASE_NAME = '/Users/timolucas/PycharmProjects/phd-project/database/dash_test.db'
ROW_NUMBER = 1000
sample_id = 0
test_names = ['Pseudomonas aeruginosa', 'Acinetobacter baumannii', 'Neisseria meningitidis', 'Erwinia',
              'Escherichia coli', 'Klebsiella pneumoniae', 'Staphylococcus aureus', 'Streptococcus oralis',
              'Streptococcus agalactiae', 'Streptococcus pneumoniae', 'Streptococcus pyogenes', 'Enterococcus faecalis',
              'Streptococcus mitis', 'Streptococcus pseudopneumoniae']
test_abundances = [200, 250, 235, 442, 335, 1200, 2100, 3210, 460, 570, 490, 679, 479, 4500]
print(len(test_abundances))


# increment sample id every 13th row


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
    # OTU id (integer); OTU taxonomy ( text); OTU abundance ( integer); sample id (integer); project id (integer); meta1 (integer); meta2 (integer); meta3 (integer); meta4 (text); meta5(text); meta6(text)
    # read taxonomy is the taxonomy parsed from maira
    # abundance is the bacterial abundance parsed from maira
    #  sample id is an integer that represents the ID of the sample the read originates from
    #  project id is integer that represents the ID of the project the read originates from
    #  meta1-meta6 are placeholders for metadata that may be included into the database in the future
    cursor.execute(create_command)

    # fills test table with $ROW_NUMBER lines change variable to adjust DB size
    for i in range(0, ROW_NUMBER):
        sample_id = inc_sample_id(i, sample_id)
        name = test_names[i % 14]
        # print(name)
        abundance = test_abundances[i % 14] + (random.randint(0, 1000))
        # print(abundance)
        cursor.execute(f"INSERT INTO birts_db VALUES ({i},'{name}', {abundance},"
                       f" {sample_id}, 1, {random.randint(1, 100000)},"
                       f" {random.randint(1, 100000)}, {random.randint(1, 100000)},'asdf','asdf','asdf')")

    cursor.execute("SELECT * FROM birts_db")

    results = cursor.fetchall()
    print(results)
    conn.commit()
    conn.close()
