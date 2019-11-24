import mysql.connector

conn = mysql.connector.connect(host="localhost", database="mydb", user="root", password='mysql')
cur = conn.cursor()
cur.execute("SELECT FIRST_NAME,LAST_NAME,AGE FROM EMPLOYEE WHERE FIRST_NAME='KUMAR'")

row = cur.fetchone()
print(row)

conn.close()
