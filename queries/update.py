import connect_database


connection = connect_database.connect_database()


def update(table, field_and_value, where):
    sql = f"UPDATE {table} SET {field_and_value} WHERE {where}"

    cursor = connection.cursor()
    cursor.execute(sql)