import mysql.connector

# ########## Fetch one ##############

conn = mysql.connector.connect(
    host="localhost", database="mydb", user="root", password="####"
)
cur = conn.cursor()
cur.execute("SELECT * FROM EMPLOYEE")

row = cur.fetchone()
for i in range(cur.rowcount):
    # row = cur.fetchall()
    print(row[0])
    print(row[1])
    print(row[2])

conn.close()
"""
########### Fetch All ##############
import mysql.connector

conn = mysql.connector.connect(host="localhost",
                                database="mydb",
                                user="root",
                                password='mysql'
                                )
cur = conn.cursor()
cur.execute("SELECT * FROM EMPLOYEE")

rows = cur.fetchall()

for each in rows:
    print(each)


conn.close()
"""
