import mysql.connector

# Database configuration
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "password123",  # Replace with your MySQL password
    "database": "student_db"
}

# Establish database connection
def get_db_connection():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Add a new student
def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")

    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        query = "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, age, grade))
        conn.commit()
        print("Student added successfully!")
        conn.close()

# View all students
def view_students():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()

        print("\nAll Students:")
        for student in students:
            print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Grade: {student[3]}")
        conn.close()

# Update a student's details
def update_student():
    student_id = int(input("Enter the ID of the student to update: "))
    name = input("Enter new name: ")
    age = int(input("Enter new age: "))
    grade = input("Enter new grade: ")

    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        query = "UPDATE students SET name = %s, age = %s, grade = %s WHERE id = %s"
        cursor.execute(query, (name, age, grade, student_id))
        conn.commit()
        if cursor.rowcount:
            print("Student updated successfully!")
        else:
            print("No student found with the given ID.")
        conn.close()

# Delete a student
def delete_student():
    student_id = int(input("Enter the ID of the student to delete: "))

    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        query = "DELETE FROM students WHERE id = %s"
        cursor.execute(query, (student_id,))
        conn.commit()
        if cursor.rowcount:
            print("Student deleted successfully!")
        else:
            print("No student found with the given ID.")
        conn.close()

# Main menu
def main():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
