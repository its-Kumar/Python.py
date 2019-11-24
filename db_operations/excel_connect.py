import mysql.connector
from xlwt import Workbook

conn = mysql.connector.connect(host="localhost", database="mydb", user="root", password='mysql')

cur = conn.cursor()
wb = Workbook()
sheet1 = wb.add_sheet('sheet1')
sql = ("SELECT * FROM employee where FIRST_NAME ='kumar'")
cur.execute(sql)
row = cur.fetchone()
sheet1.write(0,0,"First Name")
sheet1.write(0,2,row[0])
sheet1.write(1,0,"Last Name")
sheet1.write(1,2,row[1])
sheet1.write(2,0,"Age")
sheet1.write(2,2,row[2])
sheet1.write(3,0,"Sex")
sheet1.write(3,2,row[3])
sheet1.write(4,0,"Income")
sheet1.write(4,2,row[4])
wb.save('test1.xls')
print("Done")
