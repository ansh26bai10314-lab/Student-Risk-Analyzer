"""
Configuration settings and constants for the Student Academic Performance Analysis System.
"""

# Academic Grade Boundaries (Average Mark)
GRADE_BOUNDARIES = {
    "A": 85.0,
    "B": 70.0,
    "C": 50.0,
    # Below 50 is Grade "D"
}

# Risk Level Thresholds
RISK_THRESHOLDS = {
    "HIGH": {"attendance": 60.0, "average": 50.0},
    "MEDIUM": {"attendance": 75.0, "average": 60.0},
}

# Recommendation Criteria
RECOMMENDATION_THRESHOLDS = {
    "ATTENDANCE_MIN": 75.0,
    "SUPPORT_AVERAGE_MIN": 50.0,
    "WEAK_SUBJECT_AVERAGE_MIN": 65.0,
    "STUDY_HOURS_MIN": 3.0,
}