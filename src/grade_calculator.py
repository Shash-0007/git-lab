"""Functions for calculating student grades."""


def get_status(average):
    """Return Pass when the average is at least 40, otherwise Fail."""
    if not 0 <= average <= 100:
        raise ValueError("Average must be between 0 and 100")
    return "Pass" if average >= 40 else "Fail"


def calculate_average(marks):
    """Return the arithmetic mean of a list of marks."""
    if not marks:
        raise ValueError("Marks list cannot be empty")
    if any(not isinstance(mark, (int, float)) or mark < 0 or mark > 100 for mark in marks):
        raise ValueError("Marks must be numbers between 0 and 100")
    return sum(marks) / len(marks)


def calculate_grade(average):
    """Convert an average mark into a letter grade."""
    if not 0 <= average <= 100:
        raise ValueError("Average must be between 0 and 100")

    if average >= 90:
        return "A"
    if average >= 80:
        return "B"
    if average >= 70:
        return "C"
    if average >= 60:
        return "D"
    return "F"


def calculate_result(marks):
    """Return average, letter grade, and pass/fail status."""
    average = calculate_average(marks)
    return {
        "average": round(average, 2),
        "grade": calculate_grade(average),
        "status": get_status(average),
        "passed": average >= 40,
    }
