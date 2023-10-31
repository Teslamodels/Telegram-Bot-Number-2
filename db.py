import psycopg2
from psycopg2 import Error


def create_new_table():
    try:
        connection = psycopg2.connect(user = "DB_USER", password = "DB_PASSWORD", host = "localhost", port = 5432, database = "DB_BOT")
        cursor=connection.cursor()
        create_account = """CREATE TABLE Account(
                                ID SERIAL PRIMARY KEY,
                                full_name VARCHAR(1000) NOT NULL,
                                age NUMERIC NOT NULL,
                                avatar VARCHAR(1000) NOT NULL,
                                phone_number VARCHAR(1000) NOT NULL
                                );"""
        cursor.execute(create_account)
        connection.commit()
        print("Success")
    

    except (Exception, Error) as error:
        print("Error", error)


    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Closed")