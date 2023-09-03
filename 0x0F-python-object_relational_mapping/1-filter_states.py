#!/usr/bin/python3
"""
List all states with a name starting with N (upper N)
"""

if __name__ == "__main__":
    """ not be executed when imported """
    import MySQLdb
    from sys import argv
    conn = MySQLdb.connect(host='localhost',
                           port=3306,
                           user=argv[1],
                           passwd=argv[2],
                           db=argv[3],
                           charset="utf8")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE BINARY 'N%'
                ORDER BY states.id ASC""")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
