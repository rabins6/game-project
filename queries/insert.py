import connect_database


connection = connect_database.connect_database()


def insert(table, field, value):
    sql = f"INSERT INTO {table} ({field}) VALUES ({value})"

    print(sql)

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    print(result)
    if cursor.rowcount > 0:
        for row in result:
            print(row)
    return

