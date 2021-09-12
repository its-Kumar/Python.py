# install connector
# pip install mysql-connector-python

# import connector
import mysql.connector

# Global
__cnx = None


def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(
            user="kumar", password="password", host="localhost", database="my_db"
        )
    return __cnx
