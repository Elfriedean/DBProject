import mysql.connector
def add(Student_id, First_name, Last_name, Department_id): 
    db = mysql.connector.connect(
        host="localhost", 
        user="root",      
        password="123456",  
        database="su164" 
    )
    cursor = db.cursor()
    cursor.execute("INSERT INTO student (Student_id, First_name, Last_name, Department_id) VALUES (%s, %s, %s, %s)", (Student_id, First_name, Last_name, Department_id))
    print("Student added")
    db.commit()

def delete(Student_id):
    db = mysql.connector.connect(
        host="localhost",
        user = "root",
        password ="123456",
        database = "su164"
    )
    cursor = db.cursor()
    cursor.execute("DELETE FROM student WHERE Student_id = %s", (Student_id,))
    print("Student deleted")
    db.commit()

def show():
    db = mysql.connector.connect(
        host="localhost",
        user = "root",
        password ="123456",
        database = "su164"
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM student")
    result = cursor.fetchall()
    for row in result:
        print(row)

def search(Student_id):
    db = mysql.connector.connect(
        host="localhost",
        user = "root",
        password ="123456",
        database = "su164"
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM student WHERE Student_id = %s", (Student_id,))
    result = cursor.fetchall()
    for row in result:
        print(row)

def update(Student_id, First_name, Last_name, Department_id):
    db = mysql.connector.connect(
        host="localhost",
        user = "root",
        password ="123456",
        database = "su164"
    )
    cursor = db.cursor()
    cursor.execute("UPDATE student SET First_name = %s, Last_name = %s, Department_id = %s WHERE Student_id = %s", (First_name, Last_name, Department_id, Student_id))
    print("Student updated")
    db.commit()


while True:
    print("1. Add student")
    print("2. Delete student")
    print("3. Show student")
    print("4. Search student")
    print("5. Update student")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        Student_id = input("Enter Student ID: ")
        First_name = input("Enter First Name: ")
        Last_name = input("Enter Last Name: ")
        Department_id = int(input("Enter Department ID: "))
        add(Student_id, First_name, Last_name, Department_id)
    elif choice == 2:
        Student_id = int(input("Enter Student ID: "))
        delete(Student_id)
    elif choice == 3:
        show()
    elif choice == 4:
        Student_id = int(input("Enter Student ID: "))
        search(Student_id)
    elif choice == 5:
        Student_id = int(input("Enter Student ID: "))
        First_name = input("Enter First Name: ")
        Last_name = input("Enter Last Name: ")
        Department_id = int(input("Enter Department ID: "))
        update(Student_id, First_name, Last_name, Department_id)
    elif choice == 6:
        break
    else:
        print("Invalid choice")
