import mysql.connector


def connect_database():
    return mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='visit_wonder',
        user='root',
        password='1472',
        autocommit=True
    )


connect_database()
