import mysql.connector

conn = mysql.connector.connect(
    host="localhost", database="mydb", user="root", password='###')

cur = conn.cursor()
sql = """
    CREATE TABLE EMPLOYEE(
        FIRST_NAME CHAR(20) NOT NULL,
        LAST_NAME CHAR(20),
        AGE INT,
        SEX CHAR(1),
        INCOME FLOAT)
    """

cur.execute(sql)
conn.close()
print("Database Created successfully..!!")
