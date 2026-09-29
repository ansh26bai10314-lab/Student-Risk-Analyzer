"""
Main application execution module for Student Academic Performance Analysis.
"""

from typing import Dict, Any, List
from utils import read_int, read_float, read_positive_int
from student_analytics import (
    calculate_average,
    calculate_grade,
    calculate_risk,
    create_recommendation,
    class_summary,
    find_top_students,
    count_risk_levels,
)


def input_single_student() -> Dict[str, Any]:
    """Interactively captures details for a single student."""
    student = {}
    student["id"] = read_int("Enter Student ID: ")
    student["name"] = input("Enter Student Name: ").strip()
    student["attendance"] = read_float("Enter Student Attendance Percentage: ")

    m1 = read_float("Enter marks for Subject 1: ")
    m2 = read_float("Enter marks for Subject 2: ")
    m3 = read_float("Enter marks for Subject 3: ")
    student["marks"] = (m1, m2, m3)

    student["study_hours"] = read_float("Enter Daily Study Hours: ")
    return student


def generate_student_report(student: Dict[str, Any]) -> None:
    """Prints a detailed performance report for an individual student."""
    avg = calculate_average(student["marks"])
    grade = calculate_grade(avg)
    risk = calculate_risk(student["attendance"], avg)
    recommendations = create_recommendation(student, avg)

    print("\n" + "=" * 40)
    print(f" STUDENT REPORT: {student['name'].upper()}")
    print("=" * 40)
    print(f"Student ID    : {student['id']}")
    print(f"Attendance    : {student['attendance']:.2f}%")
    print(f"Subject Marks : {student['marks']}")
    print(f"Study Hours   : {student['study_hours']} hrs/day")
    print(f"Average Mark  : {round(avg, 2)}")
    print(f"Grade         : {grade}")
    print(f"Risk Level    : {risk}")
    print("\nRecommendations:")
    for rec in recommendations:
        print(f" - {rec}")
    print("=" * 40)


def main():
    print("=" * 50)
    print("  STUDENT ACADEMIC PERFORMANCE ANALYSIS SYSTEM")
    print("=" * 50)

    n = read_positive_int("\nEnter total number of students to analyze: ")
    students: List[Dict[str, Any]] = []

    for i in range(n):
        print(f"\n--- Entry {i + 1} of {n} ---")
        student = input_single_student()
        students.append(student)

    print("\n[INFO] All student records captured successfully.\n")

    # Generate individual reports
    print("\n" + "#" * 40)
    print("       INDIVIDUAL PERFORMANCE REPORTS")
    print("#" * 40)
    for student in students:
        generate_student_report(student)

    # Generate aggregate class analytics
    c_avg = class_summary(students)
    top_student, top_avg = find_top_students(students)
    risk_counts = count_risk_levels(students)

    print("\n" + "#" * 40)
    print("         CLASS AGGREGATE SUMMARY")
    print("#" * 40)
    print(f"Total Students Analyzed : {len(students)}")
    print(f"Class Average           : {round(c_avg, 2)}")
    print(f"Top Performing Student  : {top_student.get('name', 'N/A')} ({round(top_avg, 2)} avg)")
    print("\nRisk Level Distribution:")
    for risk_tier, count in risk_counts.items():
        print(f" - {risk_tier:<8}: {count} student(s)")
    print("#" * 40 + "\n")


if __name__ == "__main__":
    main()