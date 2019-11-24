import mysql.connector


def delete(id):
    conn = mysql.connector.connect(
        host="localhost", database="mydb", user="root", password='mysql')

    if conn.is_connected():
        print("Connected to mydb database")
    
    cursor = conn.cursor()

    str = "delete from emp where id ='%d'"
    args = (id)
    cursor.execute('select * from emp')

    try:
        cursor.execute(str % args)
        conn.commit()
        print("Record deleted")
    except:
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

empId = int(input("Enter Emp id : "))
delete(empId)
