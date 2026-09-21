# 🎓 Student Data Organizer

A simple **Python console-based Student Data Organizer** for managing student information through an easy menu. 🐍💻

## ✨ Features

| Option | Feature | Description |
|---|---|---|
| 1️⃣ | Add Student | Add ID, name, age, grade, DOB and subjects |
| 2️⃣ | Display All Students | View all students stored in memory |
| 3️⃣ | Update Student | Update a student's name and age |
| 4️⃣ | Delete Student | Delete a student using Student ID |
| 5️⃣ | Display Subjects | Show the subjects offered |
| 6️⃣ | Exit | Close the program |

---

## 🧑‍🎓 Student Data

Each student is stored as a Python dictionary:

```python
student = {
    "id": student_id,
    "name": name,
    "age": age,
    "grade": grade,
    "dob": dob,
    "subjects": subjects_list
}
```

All students are stored in:

```python
students_list = []
```

The program defines these offered subjects:

```python
OFFERED_SUBJECTS = ("Math", "Science", "English", "History", "Art")
```

---

## 🧠 How It Works

### 1️⃣ Add Student

Choose `1`, then enter:

- 🆔 Student ID
- 👤 Name
- 🎂 Age
- 🏆 Grade
- 📅 Date of Birth
- 📚 Subjects

Subjects are entered like:

```text
Math, Science, English
```

The code uses `.split(',')` and `.strip()` to turn this into:

```python
["Math", "Science", "English"]
```

Then the student is added:

```python
students_list.append(student)
```

### 2️⃣ Display All Students 👀

Choose `2`.

If there are no students:

```text
No students found.
```

Otherwise, the program loops through `students_list` and displays the stored information.

### 3️⃣ Update Student Information ✏️

Choose `3` and enter the Student ID.

The program searches for the matching student.

The current version allows you to update:

- 👤 Name
- 🎂 Age

Press **Enter** to skip a field.

> 💡 Grade, DOB and subjects are not updated by the current option 3.

### 4️⃣ Delete Student 🗑️

Choose `4` and enter the Student ID.

The program uses `enumerate()` to find the student's position:

```python
for i, stu in enumerate(students_list):
```

Then removes the matching student:

```python
del students_list[i]
```

### 5️⃣ Display Subjects 📚

Choose `5` to display:

```text
Math
Science
English
History
Art
```

### 6️⃣ Exit 🚪

Choose `6`.

The program uses:

```python
break
```

to stop the `while True` menu loop.

---

## 🗺️ Program Flow

```text
▶️ Start
   ↓
👋 Welcome Message
   ↓
📋 Show Menu
   ↓
Choose an option
   ├── 1️⃣ Add Student
   ├── 2️⃣ Display Students
   ├── 3️⃣ Update Student
   ├── 4️⃣ Delete Student
   ├── 5️⃣ Display Subjects
   └── 6️⃣ Exit
             ↓
        🔄 Back to Menu
```

---

## 🧰 Python Concepts Used

- 🐍 **Functions** — `main()`
- 📋 **Lists** — `students_list`
- 🗂️ **Dictionaries** — student records
- 🔁 **while loop** — keeps the menu running
- 🔄 **for loop** — processes students and subjects
- 🔀 **if / elif / else** — menu decisions
- 🛑 **break** — exits the loop
- 🔎 **enumerate()** — finds a student's list index
- ⌨️ **input()** — gets user data
- 🔢 **int()** — converts ID and age to numbers
- ✂️ **strip() / split()** — cleans and separates subjects

---

## ▶️ How to Run

### Step 1 — Install Python 🐍

Check your Python version:

```bash
python --version
```

### Step 2 — Save the program

```text
student_data_organizer.py
```

### Step 3 — Run

```bash
python student_data_organizer.py
```

---

## 🖥️ Example

```text
Welcome to the Student Data Organizer!

Select an option:
1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit

Enter your choice:
```

Example of adding a student:

```text
Enter your choice: 1

Enter student details:

Student ID: 101
Name: Rahul
Age: 20
Grade: A
Date of Birth (YYYY-MM-DD): 2006-05-12
Subjects (comma-separated): Math, Science, English

Student added successfully!
```

---

# 📸 Screenshots

The images below are **linked directly from this README**, so they will display automatically on GitHub when the `screenshots` folder is uploaded with the README.

## 🧑‍💻 Add Student Code

![Add Student Code](./screenshots/add_student_code.png)

[🔗 Open Full Image](./screenshots/add_student_code.png)

### 🧑‍💻 2. Display & Update Code

![Display and Update Code](./screenshots/02_display_update_code.png)

[🔗 Open Display & Update Screenshot](./screenshots/02_display_update_code.png)

---

### 🧑‍💻 3. Delete, Subjects & Exit Code

![Delete, Subjects & Exit Code](./screenshots/03_delete_subjects_exit_code.png)

[🔗 Open Delete / Subjects / Exit Screenshot](./screenshots/03_delete_subjects_exit_code.png)

---

### 🖥️ 4. Program Menu Output

![Program Menu Output](./screenshots/04_program_menu_output.png)

[🔗 Open Program Output Screenshot](./screenshots/04_program_menu_output.png)

---

## 📁 GitHub Project Structure

**Important:** Keep the screenshots inside the `screenshots` folder so the README image links work correctly.

```text
Student-Data-Organizer/
│
├── student_data_organizer.py
├── README.md
│
└── screenshots/
    ├── 01_add_student_code.png
    ├── 02_display_update_code.png
    ├── 03_delete_subjects_exit_code.png
    └── 04_program_menu_output.png
```

---

## ⚠️ Current Limitations

This version stores data **only in memory**, so data is lost when the program closes.

Other limitations:

- Student IDs are not explicitly checked for duplicates.
- Entered subjects are not validated against `OFFERED_SUBJECTS`.
- Update currently changes only name and age.
- Grade, DOB and subjects are not updated from option 3.

---

## 🚀 Future Improvements

You can make this project more advanced by adding:

- 💾 Save data to a JSON file
- 🗄️ SQLite or MySQL database
- 🔐 Login/authentication
- ✅ Student ID validation
- 📚 Subject validation
- ✏️ Full student editing
- 🔍 Search by ID or name
- 📊 Grade/marks calculations
- 📈 Student reports
- 🖥️ Tkinter GUI
- 🌐 Flask/Django web version

---

## 🎯 Learning Goal

This mini project shows how to combine:

**Lists + Dictionaries + Loops + Conditions + Functions + User Input**

into a small real-world Python application.

```text
Input → Process → Store → Display → Update/Delete
```

---

## 👨‍💻 Author

**Student Data Organizer — Python Mini Project** 🐍💻

Made for learning and practicing Python fundamentals.

⭐ **Happy Coding! 🚀**
