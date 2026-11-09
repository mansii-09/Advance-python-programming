
import pymysql


# Connect to MySQL server
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="root"
    
)

cursor = conn.cursor()

# Create database
cursor.execute("CREATE DATABASE IF NOT EXISTS tuition_fee_db")

conn.close()


# Connect to tuition_fee_db database
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="tuition_fee_db"
)

cursor = conn.cursor()


# Create students table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    class_name VARCHAR(50),
    monthly_fee INT
)
""")

print("Table ready")


# Add six sample students only when table is empty
cursor.execute("SELECT COUNT(*) FROM students")
count = cursor.fetchone()[0]

if count == 0:
    sample_students = [
        ("Aarav", "Class 8", 1000),
        ("Diya", "Class 9", 1200),
        ("Rohan", "Class 8", 1500),
        ("Mira", "Class 10", 1800),
        ("Kabir", "Class 7", 800),
        ("Nisha", "Class 9", 1300)
    ]

    cursor.executemany(
        "INSERT INTO students (name, class_name, monthly_fee) VALUES (%s, %s, %s)",
        sample_students
    )

    conn.commit()


# Add student function
def add_student(name, class_name, monthly_fee):
    query = """
    INSERT INTO students (name, class_name, monthly_fee)
    VALUES (%s, %s, %s)
    """

    cursor.execute(query, (name, class_name, monthly_fee))
    conn.commit()

    print("Student added successfully")


# View all students
def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    if rows:
        print("\nID   Name       Class        Monthly Fee")
        print("------------------------------------------")

        for row in rows:
            print(f"{row[0]:<5}{row[1]:<11}{row[2]:<13}{row[3]}")
    else:
        print("No students found")


# Search student by class
def search_class(class_name):
    query = "SELECT * FROM students WHERE class_name = %s"

    cursor.execute(query, (class_name,))
    rows = cursor.fetchall()

    if rows:
        print("\nID   Name       Class        Monthly Fee")
        print("------------------------------------------")

        for row in rows:
            print(f"{row[0]:<5}{row[1]:<11}{row[2]:<13}{row[3]}")
    else:
        print("No students found")


# Update student fee
def update_fee(student_id, monthly_fee):
    query = "UPDATE students SET monthly_fee = %s WHERE id = %s"

    cursor.execute(query, (monthly_fee, student_id))
    conn.commit()

    if cursor.rowcount == 0:
        print("No such student")
    else:
        print("Fee updated successfully")


# Delete student
def delete_student(student_id):
    query = "DELETE FROM students WHERE id = %s"

    cursor.execute(query, (student_id,))
    conn.commit()

    if cursor.rowcount == 0:
        print("No such student")
    else:
        print("Student deleted successfully")


# Menu loop
while True:
    print("\n===== TUITION FEE TRACKER =====")
    print("1. Add student")
    print("2. View all students")
    print("3. Search by class")
    print("4. Update fee")
    print("5. Delete student")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        class_name = input("Enter class: ")
        monthly_fee = int(input("Enter monthly fee: "))

        add_student(name, class_name, monthly_fee)

    elif choice == "2":
        view_students()

    elif choice == "3":
        class_name = input("Enter class name: ")
        search_class(class_name)

    elif choice == "4":
        student_id = int(input("Enter student ID: "))
        monthly_fee = int(input("Enter new monthly fee: "))

        update_fee(student_id, monthly_fee)

    elif choice == "5":
        student_id = int(input("Enter student ID: "))

        delete_student(student_id)

    elif choice == "0":
        print("Thank you!")
        break

    else:
        print("Invalid choice")


cursor.close()
conn.close()
