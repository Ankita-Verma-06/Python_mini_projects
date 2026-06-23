%%writefile grading_system.py

def calculate_grade(percentage):
    """Calculates letter grade based on overall percentage."""
    if percentage >= 90: return "A+"
    elif percentage >= 80: return "A"
    elif percentage >= 70: return "B"
    elif percentage >= 60: return "C"
    elif percentage >= 50: return "D"
    else: return "F"

def process_student_marks(marks_dict):
    """Computes total, average percentage, and final grade from a marks dictionary."""
    if not marks_dict:
        return 0, 0.0, "F"
    
    total_marks = sum(marks_dict.values())
    num_subjects = len(marks_dict)
    percentage = total_marks / num_subjects
    grade = calculate_grade(percentage)
    
    return total_marks, round(percentage, 2), grade
