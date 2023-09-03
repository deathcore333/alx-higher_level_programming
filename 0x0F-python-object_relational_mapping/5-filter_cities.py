#!/usr/bin/python3
"""
takes in the name of a state as an argument
and lists all cities of that state
"""
if __name__ == "__main__":
    """ not executed when imported """
    from sys import argv
    import MySQLdb

    username = argv[1]
    password = argv[2]
    database = argv[3]
    state = argv[4]
    host = 'localhost'
    port = 3306

    conn = MySQLdb.connect(
                           host=host,
                           port=port,
                           user=username,
                           passwd=password,
                           db=database,
                           charset='utf8'
                           )

    cur = conn.cursor()
    sql = """
        SELECT
            cities.name
        FROM
            cities
        INNER JOIN
            states
        ON
            cities.state_id=states.id
        WHERE
            states.name = %s
        ORDER BY
            cities.id ASC;
    """

    cur.execute(sql, (state,))
    query_rows = cur.fetchall()
    print(", ".join(i[0] for i in query_rows))
    cur.close()
    conn.close()
