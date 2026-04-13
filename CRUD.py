import mysql.connector

#Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # add your password if set
)

cursor = conn.cursor()

#Create Database
cursor.execute("CREATE DATABASE IF NOT EXISTS student_db")
cursor.execute("USE student_db")

#Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    course VARCHAR(100)
)
""")



#CREATE OPERATION

def add_student(name, age, course):
    sql = "INSERT INTO students (name, age, course) VALUES (%s, %s, %s)"
    val = (name, age, course)
    cursor.execute(sql, val)
    conn.commit()
    print("Student Added Successfully")



#READ OPERATION

def view_students():
    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall()

    print("\n Student Records:")
    for row in result:
        print(row)


#UPDATE OPERATION

def update_student(student_id, name, age, course):
    sql = "UPDATE students SET name=%s, age=%s, course=%s WHERE id=%s"
    val = (name, age, course, student_id)
    cursor.execute(sql, val)
    conn.commit()
    print("Student Updated Successfully")



#DELETE OPERATION

def delete_student(student_id):
    sql = "DELETE FROM students WHERE id=%s"
    val = (student_id,)
    cursor.execute(sql, val)
    conn.commit()
    print("️Student Deleted Successfully")


