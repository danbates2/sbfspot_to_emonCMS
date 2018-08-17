#!/usr/bin/python
 
import sqlite3
from sqlite3 import Error
 
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

    cur = conn.cursor()
    cur.execute("SELECT * FROM SpotData")
    names = list(map(lambda x: x[0], cur.description))
    names = [description[0] for description in cur.description]
    print(names)
    
def select_all_tasks(conn):
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
 
 
def select_task_by_priority(conn, priority):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM SpotData WHERE Pac1=?", (priority,))
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)
 
 
def main():
    database = "SBFspot.db"
 
    # create a database connection
    conn = create_connection(database)
    with conn:
        print(". List headers of table: SpotData")
        list_headers(conn)
 
        print(". Query all data within table: SpotData")
        select_all_tasks(conn)

 
if __name__ == '__main__':
    main()
