#!/usr/bin/python3
"""
scripts that lists all the cities from the database
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """ not execute when imported """

    username = argv[1]
    password = argv[2]
    database = argv[3]
    server = 'localhost'
    port = 3306

    conn = MySQLdb.connect(host=server,
                           port=port,
                           user=username,
                           passwd=password,
                           db=database
                           )

    cur = conn.cursor()
    sql = """
          SELECT
                cities.id, cities.name, states.name
          FROM
                cities
          INNER JOIN
                states ON
                    cities.state_id=states.id"""
    cur.execute(sql)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(raw)
    cur.close()
    conn.close()
