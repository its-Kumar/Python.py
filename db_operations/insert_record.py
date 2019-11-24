import mysql.connector

conn = mysql.connector.connect(host="localhost", database="mydb", user="root", password='###')

cur = conn.cursor()
sql = "INSERT INTO EMPLOYEE (FIRST_NAME,LAST_NAME,AGE,SEX,INCOME)"\
    "VALUES ('ajay','chandra', 20, 'M', 20000),\
        ('Kumari' ,'shalini', 18 , 'F' , 10000),\
            ('Aditya', 'Kumar' ,20 , 'M' , 20002)"

cur.execute(sql)
conn.commit()
conn.close()
print("Data inserted successfully..!!")
