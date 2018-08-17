#!/usr/bin/python
 
import sqlite3
from sqlite3 import Error
from collections import OrderedDict


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
        
    return None

 
def list_headers(conn):
    global names

    cur = conn.cursor()
    cur.execute("SELECT * FROM SpotData")
    #names = list(map(lambda x: x[0], cur.description))
    names = [description[0] for description in cur.description]
    print(names)
    

def display_all_from_table(conn):
    global rows
    
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM SpotData")

    rows = cur.fetchall()
 
    for row in rows:
        print(row)
        


    
#maybe convert to tuple first
def create_OrderedDict(): #https://docs.python.org/2/library/collections.html#collections.OrderedDict
    orderedDict = OrderedDict(zip(names, rows[0]))
    print orderedDict

    
def main():
    database = "SBFspot.db"
 
    # create a database connection
    conn = create_connection(database)
    with conn:
        print(". List headers of table: SpotData")
        list_headers(conn)
 
        print(". Query all data within table: SpotData")
        display_all_from_table(conn)

        print(". Create ordered key/value dictionary for passing to JSON encoder.")
        create_OrderedDict()
      

 
if __name__ == '__main__':
    main()
