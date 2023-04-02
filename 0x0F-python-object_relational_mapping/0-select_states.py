#!/usr/bin/python3
"""
Script that lists all the states from the
the database 'hbtn_0e_0_usa'.
"""

import MySQLdb
from sys import argv

if __name__ = '__main__':
    """
    Access db and get states from db
    """
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states")

    for row in rows:
        print(row)
