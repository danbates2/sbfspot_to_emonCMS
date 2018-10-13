#!/usr/bin/python

import sqlite3
from sqlite3 import Error
from collections import OrderedDict
import json
import requests

# Notes:
# With emonCMS already installed on a rPi, SBFspot will run fine. Tested using the default SBFspot SQLite.
# The default SBFspot folder locations will need changing during install from /home/pi/smadata to /home/pi/data/smadata, for write permissions to not throw errors.
# Change the folder locations in both SBFspot conf, and SBFspotUploadDaemon conf.

#API KEY
apikey = "yourapikey"
database = "/home/pi/data/smadata/SBFspot.db"
emoncms_server = "http://emoncms.org"

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
    names = [description[0] for description in cur.description]

    #print(". List headers of table: SpotData")
    #print(names)


def display_last_from_table(conn):
    global rows

    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM SpotData ORDER BY TimeStamp DESC LIMIT 1")

    rows = cur.fetchone()

    #print(". Query all data within table: SpotData")
    #for row in rows:
        #print(row)


def OrderedDict_to_JSON(): #https://docs.python.org/2/library/collections.html#collections.OrderedDict
    global smaJSONstring

    names_lastrow_ordered = OrderedDict(zip(names, rows))

    smaJSONstring = json.dumps(OrderedDict(names_lastrow_ordered))

    #print(". Create OrderedDict from two lists and convert to JSON")
    #print (smaJSONstring)


def url_stringing():
    global URLstring

    node_id = "sbfspot"

    URLstring = emoncms_server + "/input/post?node=" + node_id + "&fulljson=" + str(smaJSONstring) + "&apikey=" + apikey

    #print(". Concatenate URL string")
    #print URLstring


def send_to_emonCMS():
    r = requests.get(URLstring)
    #print (r)


def main():

    # create a database connection
    conn = create_connection(database)
    with conn:
        list_headers(conn)

        display_last_from_table(conn)

        OrderedDict_to_JSON()

        url_stringing()

        send_to_emonCMS()

if __name__ == '__main__':
    main()
