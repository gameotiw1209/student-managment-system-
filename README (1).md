# Student Management System 🎓

A terminal-based Student Management System built with Python using Object-Oriented Programming (OOP) concepts. This is a learning project to practice Python fundamentals like classes, file handling, and JSON-based data persistence.

---

## Features

- Add new students with name, section, roll number, and subject-wise marks
- View all students with formatted output
- Search students by name or roll number
- Update student details (name, section, or marks)
- Delete a student record
- View class statistics — topper and class average
- Data persists across sessions using a local JSON file

---

## Project Structure

```
student_management/
├── main.py        # Entry point and menu loop
├── manager.py     # StudentManager class — all CRUD operations
├── student.py     # Student class — blueprint for a student
└── README.md
```

---

## Tech Used

- Python 3.x
- OOP (Classes, Methods, Class Methods)
- JSON for data storage
- File handling (`json.load`, `json.dump`)

---

## How to Run

```bash
git clone https://github.com/gameotiw1209/student-management-system
cd student-management-system
python main.py
```

No external libraries needed — runs on pure Python.

---

## What I Learned

- Designing classes and separating concerns across files
- Using `@classmethod` and `__str__` in Python
- Reading and writing JSON for persistent storage
- Building a full CRUD system from scratch

---

## Author

**gameotiw1209** — built this as a learning project while studying Python OOP.
