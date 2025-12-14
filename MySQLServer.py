#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    try:
        # CONNECT TO MYSQL SERVER
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""   # CHANGE IF YOUR MYSQL HAS A PASSWORD
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # CREATE DATABASE (DOES NOT FAIL IF IT EXISTS)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print("Error while connecting to MySQL:", e)

    finally:
        # CLOSE CONNECTION
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
