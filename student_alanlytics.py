"""
Core business logic and analytics functions for evaluating student data.
"""

from typing import Dict, List, Tuple, Any
from config import (
    GRADE_BOUNDARIES,
    RISK_THRESHOLDS,
    RECOMMENDATION_THRESHOLDS,
)


def calculate_total(marks: Tuple[float, ...]) -> float:
    """Calculates the sum of marks for a student."""
    return sum(marks)


def calculate_average(marks: Tuple[float, ...]) -> float:
    """Calculates the arithmetic mean of marks."""
    if not marks:
        return 0.0
    return calculate_total(marks) / len(marks)


def calculate_grade(average: float) -> str:
    """Determines letter grade based on calculated average."""
    if average >= GRADE_BOUNDARIES["A"]:
        return "A"
    elif average >= GRADE_BOUNDARIES["B"]:
        return "B"
    elif average >= GRADE_BOUNDARIES["C"]:
        return "C"
    return "D"


def calculate_risk(attendance: float, average: float) -> str:
    """Determines student risk level based on attendance and average grade."""
    if (
        attendance < RISK_THRESHOLDS["HIGH"]["attendance"]
        or average < RISK_THRESHOLDS["HIGH"]["average"]
    ):
        return "High"
    elif (
        attendance < RISK_THRESHOLDS["MEDIUM"]["attendance"]
        or average < RISK_THRESHOLDS["MEDIUM"]["average"]
    ):
        return "Medium"
    return "Low"


def create_recommendation(
    student: Dict[str, Any], average: float
) -> List[str]:
    """Generates personalized action items based on student metrics."""
    recommendations = []

    if (
        student["attendance"]
        < RECOMMENDATION_THRESHOLDS["ATTENDANCE_MIN"]
    ):
        recommendations.append("Improve attendance")

    if average < RECOMMENDATION_THRESHOLDS["SUPPORT_AVERAGE_MIN"]:
        recommendations.append("Attend extra academic support")

    if average < RECOMMENDATION_THRESHOLDS["WEAK_SUBJECT_AVERAGE_MIN"]:
        recommendations.append("Revise WEAK subjects")

    if student["study_hours"] < RECOMMENDATION_THRESHOLDS["STUDY_HOURS_MIN"]:
        recommendations.append("Increase daily study hours")

    if not recommendations:
        recommendations.append(
            "WELL DONE! Continue the current study plan."
        )

    return recommendations


def class_summary(students: List[Dict[str, Any]]) -> float:
    """Calculates and returns overall class average performance."""
    if not students:
        return 0.0
    total_average = sum(
        calculate_average(s["marks"]) for s in students
    )
    return total_average / len(students)


def find_top_students(
    students: List[Dict[str, Any]]
) -> Tuple[Dict[str, Any], float]:
    """Identifies top performing student and their average grade."""
    if not students:
        return {}, 0.0

    top_student = students[0]
    top_average = calculate_average(top_student["marks"])

    for student in students[1:]:
        current_average = calculate_average(student["marks"])
        if current_average > top_average:
            top_student = student
            top_average = current_average

    return top_student, top_average


def count_risk_levels(students: List[Dict[str, Any]]) -> Dict[str, int]:
    """Aggregates students across different risk tiers."""
    risk_counts = {"Low": 0, "Medium": 0, "High": 0}

    for student in students:
        avg = calculate_average(student["marks"])
        risk = calculate_risk(student["attendance"], avg)
        if risk in risk_counts:
            risk_counts[risk] += 1

    return risk_counts