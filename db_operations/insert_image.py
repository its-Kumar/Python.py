import mysql.connector

conn = mysql.connector.connect(
    host="localhost", database="mydb", user="root", password='####')


photo = open('photo.png',"rb")
show_photo = photo.read()

cur = conn.cursor()

cur.execute("INSERT INTO images VALUES(1, %s)", (show_photo,) )
conn.commit()
conn.close()
print("image inserted successfully..!!")
