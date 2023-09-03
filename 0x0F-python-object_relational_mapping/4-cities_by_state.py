#!/usr/bin/python3
"""lists all cities from the database"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    username = argv[1]
    password = argv[2]
    database = argv[3]
    server = 'localhost'
    port = 3306

    conn = MySQLdb.connect(
                           host=server,
                           port=port,
                           user=username,
                           passwd=password,
                           db=database,
                           charset="utf8"
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
        print(row)
    cur.close()
    conn.close()
