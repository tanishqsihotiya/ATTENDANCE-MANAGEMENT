# 📚 Attendance Management System

A simple **Python-based Attendance Management System** designed to manage students, record attendance, and analyze attendance percentages.

## 🚀 Features

### 👨‍🎓 Student Management

* Add students
* Remove students
* Search for students
* View all students

### 📝 Attendance Management

* Mark students as **Present**
* Mark students as **Absent**
* View attendance records

### 📊 Attendance Analysis

* Calculate attendance percentage
* Check attendance eligibility
* Find the student with the highest attendance
* Find the student with the lowest attendance

## The application provides a menu-driven interface for accessing these features.

## 🛠️ Technologies Used

* **Python 3**
* Python modules
* Dictionaries
* Functions
* Loops
* Conditional statements
* Menu-driven programming

---

## 📁 Project Structure

```text
Attendance-Management-System/
│
├── main.py
├── m1.py
├── m2.py
├── m3.py
└── README.md
```

### Module Description

| File        | Purpose                      |
| ----------- | ---------------------------- |
| `main.py`   | Main program and menu system |
| `m1.py`     | Student management           |
| `m2.py`     | Attendance management        |
| `m3.py`     | Attendance analysis          |
| `README.md` | Project documentation        |

The main program imports the three modules as `m1`, `m2`, and `m3`.

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Attendance-Management-System.git
```

### 2. Open the project folder

```bash
cd Attendance-Management-System
```

### 3. Run the program

```bash
python main.py
```

---

## 🖥️ Main Menu

```text
==============================================
       ATTANDANCE MANAGEMENT
==============================================

1. Student Management
2. Attandance Management
3. Attandance Analysis
4. Exit
```

---

## 📌 Student Management

The Student Management section provides options to:

```text
1. Add Student
2. Remove Student
3. Search Student
4. View All Students
5. Back to Main Menu
```

---

## 📌 Attendance Management

The Attendance Management section allows users to:

```text
1. Mark Present
2. Mark Absent
3. View Attendance
4. Back to Main Menu
```

---

## 📊 Attendance Analysis

The system provides the following analysis options:

```text
1. Attendance Percentage
2. Check Eligibility
3. Highest Attendance
4. Lowest Attendance
5. Back to Main Menu
```

---

## 💡 How It Works

The application starts with an empty student and attendance dictionary:

```python
students = {}
attendance = {}
```

The main menu continuously accepts user input and directs the request to the appropriate module.

For example:

```python
if choice == "1":
    # Student Management

elif choice == "2":
    # Attendance Management

elif choice == "3":
    # Attendance Analysis

elif choice == "4":
    # Exit
```

---

## 🎯 Project Objective

The main objective of this project is to create a simple and user-friendly system for managing student information and attendance records while providing useful attendance analysis.

---

## 🔮 Future Improvements

Possible improvements include:

* 💾 Save data permanently using files or a database
* 🔐 Add user authentication
* 📅 Store attendance by date
* 📈 Generate attendance reports
* 📤 Export attendance to CSV/Excel
* 🖥️ Create a graphical user interface
* 🔎 Add advanced student search
* 🗄️ Use SQLite/MySQL for data storage

---

## 👨‍💻 Author

**Tanishq Sihotia**

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub!
