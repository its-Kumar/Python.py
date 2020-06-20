import mysql.connector

conn = mysql.connector.connect(
    host="localhost", database="mydb", user="root", password='####')

cur = conn.cursor()
sql = "UPDATE employee SET AGE=21 WHERE FIRST_NAME = 'kumar'"

cur.execute(sql)
conn.commit()
conn.close()
print("Data updated successfully..!!")
