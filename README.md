# Student Academic Performance Analysis System

A comprehensive Python-based CLI application designed to analyze student academic performance, assess risk levels, generate automated improvement recommendations, and calculate class-wide metrics.

---

## Overview

The **Student Academic Performance Analysis System** collects academic and behavioral data for students (including subject marks, attendance percentage, and daily study hours). It evaluates individual student statistics, determines letter grades, calculates academic risk, generates tailored actionable recommendations, and aggregates class-wide statistics such as overall class averages and top performers.

---

## Features

- **Robust Input Handling:** Safe CLI input validation for integers and float values to prevent runtime crashes.
- **Academic Evaluation:** Automatically computes total marks, overall average, and letter grades (`A`, `B`, `C`, `D`).
- **Risk Assessment:** Evaluates student academic risk (`Low`, `Medium`, `High`) based on attendance and average scores.
- **Smart Recommendations:** Generates customized advice based on study hours, attendance, and subject marks.
- **Class-Level Analytics:**
  - Calculates class average performance.
  - Identifies top-performing students.
  - Generates distribution reports for risk levels across the class.
- **Comprehensive Student Reports:** Displays formatted summary cards for each evaluated student.

---

## Technologies & Tools Used

- **Language:** Python 3.x
- **Core Libraries Used:** Built-in Python Standard Modules (`sys`, `builtins` - no external dependencies required)

---

## Steps to Install & Run the Project

### Prerequisites

Ensure Python 3.6 or higher is installed on your system. You can verify your installation by running:

```bash
python --version
```

### Installation

1. **Clone or Download the Repository:**
   ```bash
   git clone https://github.com/your-username/student-performance-analysis.git
   cd student-performance-analysis
   ```

2. **Save the Code File:**
   Ensure your Python script is saved in the directory (e.g., as `main.py`).

### Running the Application

Execute the script using your terminal or command prompt:

```bash
python main.py
```

---

## Instructions for Testing

1. **Launch the Program:** Run `python main.py` in your terminal.
2. **Single Student Test:**
   - Enter values when prompted for Student ID, Name, Attendance, Subject Marks (3 subjects), and Daily Study Hours.
   - **Input Validation Check:** Try entering letters (e.g., `"abc"`) when prompted for numerical values to confirm error handling prompts user to enter a valid number.
3. **Class Data Test:**
   - Enter the total number of students (e.g., `3`).
   - Enter test data for each student:
     - **Student 1 (High Performance):** Marks: `90, 85, 95`, Attendance: `90`, Study Hours: `4`
     - **Student 2 (Average Performance):** Marks: `65, 70, 60`, Attendance: `80`, Study Hours: `3`
     - **Student 3 (At Risk):** Marks: `40, 45, 50`, Attendance: `55`, Study Hours: `1.5`
4. **Verify Outputs:**
   - Confirm individual report cards display expected grades (`A`, `B`, `C`, or `D`) and risk levels (`Low`, `Medium`, `High`).
   - Check that the class average and top performer match calculated values.
   - Ensure the risk counts correctly summarize the dataset.

---

## Screenshots (Optional)

### Terminal Execution & Output Example

```text
Enter Student ID: 101
Enter Student Name: Alice Smith
Enter Student Attendance Percentage: 88.5
Enter marks of student in subject 1: 85
Enter marks of student in subject 2: 90
Enter marks of student in subject 3: 88
Enter Student Study Hours per day: 4.5

Student Data Saved Successfully.
Student: Alice Smith
Marks: (85.0, 90.0, 88.0)
Total: 263.0
Average: 87.67
Grade: A
Risk Level: Low

Recommendations (according to me):
- WELL DONE! Continue the current study plan.
------------------------------
Class Summary:
Class Average: 87.67
Total Students: 1
Top Student: Alice Smith
Top Average: 87.67
Risk Counts: {'Low': 1, 'Medium': 0, 'High': 0}
------------------------------
```
