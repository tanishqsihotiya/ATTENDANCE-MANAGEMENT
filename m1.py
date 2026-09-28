def add_student(students):
    student_id = int(input("Enter student ID: "))
    name = input("Enter student name: ")

    if student_id in students:
        print("Student already exists.")
    else:
        students[student_id] = name
        print("Student added successfully.")

def remove_student(students):
    student_id = int(input("Enter student ID: "))

    if student_id in students:
        del students[student_id]
        print("Student removed successfully.")
    else:
        print("Student not found.")

def search_student(students):
    student_id = int(input("Enter student ID: "))

    if student_id in students:
        print("Student ID:", student_id)
        print("Student Name:", students[student_id])
    else:
        print("Student not found.")

def view_students(students):
    if len(students) == 0:
        print("No students available.")
    else:
        print("\nStudent List:")

        for student_id, name in students.items():
            print(student_id, "-", name)