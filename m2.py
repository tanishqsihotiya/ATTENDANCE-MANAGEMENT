def mark_present(attendance):
    name = input("Enter student name: ")

    if name in attendance:
        attendance[name].append(1)
        print(name, "marked Present.")
    else:
        print("Student not found.")


def mark_absent(attendance):
    name = input("Enter student name: ")

    if name in attendance:
        attendance[name].append(0)
        print(name, "marked Absent.")
    else:
        print("Student not found.")


def view_attendance(attendance):
    if not attendance:
        print("No students found.")
        return

    print("\n--- Attendance Record ---")

    for name, records in attendance.items():
        print(name, ":", records)
