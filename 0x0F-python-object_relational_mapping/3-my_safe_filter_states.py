#!/usr/bin/python3
"""
Takes in an argument and displays all values in the states tables of a database
where name matches the argument
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """ not be executed when imported """
    host = 'localhost'
    port = 3306
    username = argv[1]
    password = argv[2]
    name = argv[3]
    state = argv[4]

    conn = MySQLdb.connect(host=host,
                           port=port,
                           user=username,
                           passwd=password,
                           db=name,
                           charset="utf8"
                           )
    cur = conn.cursor()
    sql = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(sql, (state,))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
