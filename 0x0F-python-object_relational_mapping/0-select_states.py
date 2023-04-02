#!/usr/bin/python3
"""
Script that lists all the states from the
the database 'hbtn_0e_0_usa'.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access database and get states from database
    """
    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=user,
                           passwd=passwd, db=db, charset="utf-8")

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    # HERE I have to know SQL to grab all states in the database
    query_rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
