import mysql.connector


def delete(id_):
    conn = mysql.connector.connect(
        host="localhost", database="mydb", user="root", password="####"
    )

    if conn.is_connected():
        print("Connected to mydb database")

    cursor = conn.cursor()

    string = "delete from emp where id ='%d'"
    args = id_
    cursor.execute("select * from emp")

    try:
        cursor.execute(string % args)
        conn.commit()
        print("Record deleted")
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


empId = int(input("Enter Emp id : "))
delete(empId)
