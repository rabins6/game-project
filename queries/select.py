import connect_database


connection = connect_database.connect_database()


def select(query, table, where):
    print(query)
    print(table)
    sql = f"SELECT {query} FROM {table}"

    if where != '':
        sql += f" WHERE {where}"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    if cursor.rowcount > 0:
        for row in result:
            print(row)
    return

