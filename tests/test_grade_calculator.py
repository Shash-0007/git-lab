import pytest

from src.grade_calculator import (
    get_status,
    calculate_average,
    calculate_grade,
    calculate_result,
)


def test_get_status_pass_boundary():
    assert get_status(40) == "Pass"
    assert get_status(75) == "Pass"


def test_get_status_fail_boundary():
    assert get_status(39.99) == "Fail"
    assert get_status(0) == "Fail"


def test_get_status_rejects_invalid_average():
    with pytest.raises(ValueError):
        get_status(101)


def test_calculate_average():
    assert calculate_average([80, 90, 70]) == 80


def test_average_with_decimal_result():
    assert calculate_average([70, 80, 76]) == pytest.approx(75.333333)


def test_empty_marks_raise_error():
    with pytest.raises(ValueError):
        calculate_average([])


@pytest.mark.parametrize("marks", [[-1, 50], [80, 101], ["x", 50]])
def test_invalid_marks_raise_error(marks):
    with pytest.raises(ValueError):
        calculate_average(marks)


def test_grade_boundaries():
    assert calculate_grade(90) == "A"
    assert calculate_grade(80) == "B"
    assert calculate_grade(70) == "C"
    assert calculate_grade(60) == "D"
    assert calculate_grade(59.99) == "F"


def test_invalid_average_raise_error():
    with pytest.raises(ValueError):
        calculate_grade(101)


def test_passed_result():
    result = calculate_result([60, 70, 80])
    assert result["average"] == 70
    assert result["passed"] is True
    assert result["status"] == "Pass"
    assert result["grade"] == "C"


def test_failed_result():
    result = calculate_result([20, 30, 35])
    assert result["passed"] is False
    assert result["status"] == "Fail"
    assert result["grade"] == "F"
