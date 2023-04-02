#!/usr/bin/python3
""" Takes in argument and displays all values in
states table where name matches argument """
if __name__ == "__main__":
    """ not be executed when imported """
    import MySQLdb
    from sys import argv
    host = 'localhost'
    port = 3306
    username = argv[1]
    password = argv[2]
    name = argv[3]
    state = str(argv[4])

    conn = MySQLdb.connect(host=host,
                           port=port,
                           user=username,
                           passwd=password,
                           db=name
                           )
    cur = conn.cursor()
    sql = """SELECT * FROM states WHERE name LIKE BINARY 
          ORDER BY id ASC""".format(state)
    cur.execute(sql)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
