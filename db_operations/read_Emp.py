import mysql.connector

conn = mysql.connector.connect(
    host="localhost", database="mydb", user="root", password="####"
)

if conn.is_connected():
    print("Connected to mydb database")

cursor = conn.cursor()

cursor.execute("select * from emp")
"""
row = cursor.fetchone()
while row is not None:
    print(row)
    row = cursor.fetchone()
"""
rows = cursor.fetchall()
print("Total no of rows : ", cursor.rowcount)

for row in rows:
    print(row)

cursor.close()
conn.close()
