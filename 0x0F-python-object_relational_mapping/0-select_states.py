#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


if __name__ == "__main__":
    """ not be executed when imported """
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=user,
                           passwd=passwd, db=db, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    # HERE I have to know SQL to grab all states in my database
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
