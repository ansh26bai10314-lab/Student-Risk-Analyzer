# Project Statement & Scope Document

## Problem Statement

Educational institutions and instructors often struggle to efficiently track individual student academic performance, monitor attendance, and identify students who are academically at risk. Manual analysis of marks, attendance, and study habits is time-consuming and prone to human error. Without automated monitoring, educators may fail to provide timely interventions or customized recommendations to struggling students before final assessments occur.

There is a need for a lightweight, automated system that processes student inputs, evaluates performance metrics, assesses risk factors, and provides actionable feedback alongside class-wide analytics.

---

## Scope of the Project

The **Student Academic Performance Analysis System** is designed as a foundational, Command-Line Interface (CLI) tool to handle core data processing and analytics for educational datasets.

### In Scope
- Input validation and exception handling for user data entry.
- Processing student profiles, including subject marks, attendance rates, and daily study habits.
- Calculation of key metrics: total marks, average scores, and letter grade assignment.
- Assessment of individual risk levels (High, Medium, Low) based on academic thresholds and attendance percentages.
- Automated generation of actionable recommendations tailored to individual performance gaps.
- Computation of class-wide summary statistics (class average, top-performing student, risk level counts).
- Console-based summary reporting for individual students and entire batches.

### Out of Scope
- Graphical User Interface (GUI) or web application interface.
- Database persistence (data is currently stored in-memory during execution).
- Multi-teacher/multi-role user authentication and access control.
- Automated generation of downloadable PDF/CSV reports.

---

## Target Users

1. **Educators and Teachers:** Primary users who need to evaluate individual student performance, identify top performers, and track overall class progress quickly.
2. **Academic Counselors and Tutors:** Professionals requiring early warning indicators (risk level assessments) to identify struggling students and provide targeted academic interventions.
3. **Students:** Learners seeking actionable insights and structured recommendations on how to improve their study habits, attendance, and academic grades.

---

## High-Level Features

- **Data Input & Safe Parsing:** Interactive command-line collection of student records with robust input validation against non-numeric entries.
- **Grade & Performance Evaluation:** Automatic calculation of overall averages and rule-based letter grade assignment (`A`, `B`, `C`, `D`).
- **Automated Risk Assessment:** Multi-factor logic evaluating attendance and average marks to assign risk categories (`Low`, `Medium`, `High`).
- **Personalized Actionable Feedback:** Smart rule engine that outputs tailored guidance (e.g., advising extra tutoring, revision on weak subjects, or increasing daily study hours).
- **Class Analytics Engine:** Batch processing function calculating class average marks, identifying the highest-achieving student, and aggregating risk distribution counters.
- **Formatted Report Generator:** Clean, structured console report rendering for individual student profiles and whole-class metrics.