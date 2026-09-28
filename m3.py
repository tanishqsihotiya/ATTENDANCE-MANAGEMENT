def attendance_percentage(records):

    total_days = len(records)

    if total_days == 0:
        return 0

    present_days = sum(records)

    percentage = (present_days / total_days) * 100

    return percentage


def at_percent(attendance):

    print("----- Attendance Percentage -----")

    for name, records in attendance.items():

        percentage = attendance_percentage(records)

        print(f"{name}: {percentage:.2f}%")


def analyze_attendance(attendance):

    print("\n----- Attendance Analysis -----")

    for name, records in attendance.items():

        percentage = attendance_percentage(records)

        if percentage >= 75:
            status = "Eligible"
        else:
            status = "Not Eligible"

        print(f"{name}: {percentage:.2f}% - {status}")


def highest_attendance(attendance):

    highest_student = ""
    highest_percentage = -1

    for name, records in attendance.items():

        percentage = attendance_percentage(records)

        if percentage > highest_percentage:
            highest_percentage = percentage
            highest_student = name

    if highest_student != "":
        print(
            f"Highest Attendance: {highest_student} "
            f"({highest_percentage:.2f}%)"
        )
    else:
        print("No attendance records available.")


def lowest_attendance(attendance):

    lowest_student = ""
    lowest_percentage = 101

    for name, records in attendance.items():

        percentage = attendance_percentage(records)

        if percentage < lowest_percentage:
            lowest_percentage = percentage
            lowest_student = name

    if lowest_student != "":
        print(
            f"Lowest Attendance: {lowest_student} "
            f"({lowest_percentage:.2f}%)"
        )
    else:
        print("No attendance records available.")