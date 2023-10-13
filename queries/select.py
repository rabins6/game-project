import connect_database


connection = connect_database.connect_database()


def select(query, table, where, additional_query=''):
    sql = f"SELECT {query} FROM {table}"

    if where != '':
        sql += f" WHERE {where}"

    if additional_query != '':
        sql += additional_query

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    if cursor.rowcount > 0:
        for row in result:
            return row
    return

