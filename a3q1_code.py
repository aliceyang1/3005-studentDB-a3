import psycopg

def connect_db():
    return psycopg.connect(
        dbname="school_db", 
        user="postgres", 
        password="5772570.", 
        host="localhost"
    )

def getAllStudents():
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM students;")
            for record in cur.fetchall():
                print(record)

def addStudent(firstName, lastName, email, enrollmentDate):
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);",
                        (firstName, lastName, email, enrollmentDate))

def updateStudentEmail(id, newEmail):
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE students SET email=%s WHERE student_id=%s;", (newEmail, id))

def deleteStudent(id):
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM students WHERE student_id=%s;", (id,))


# User interface function
def function_test():
    while True:
        print("\n")
        print("1. Get all students")
        print("2. Add a student")
        print("3. Update a student's email")
        print("4. Delete a student")
        print("5. Exit")
        choice = input("Enter your action(#): ")

        if choice == "1":
            getAllStudents()
        elif choice == "2":
            firstName = input("Enter first name: ")
            lastName = input("Enter last name: ")
            email = input("Enter email: ")
            enrollmentDate = input("Enter enrollment date (YYYY-MM-DD): ")
            addStudent(firstName, lastName, email, enrollmentDate)
        elif choice == "3":
            id = int(input("Enter student ID: "))
            newEmail = input("Enter new email: ")
            updateStudentEmail(id, newEmail)
        elif choice == "4":
            id = int(input("Enter student ID: "))
            deleteStudent(id)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Run the user interface
if __name__ == "__main__":
    function_test()