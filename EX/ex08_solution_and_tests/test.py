"""Tests."""
import pytest
from solution import students_study


def test_students_study__evening_not_coffee_needed():
    """In the evening it doesn't matter weather we have coffee."""
    assert students_study(20, True) is True
    assert students_study(20, False) is True


def test_students_study__night_to_study():
    """
    Test case.

    time 20-24 (evening)
    coffee is True (coffee not needed).

    Expected: True
    :return:
    """
    assert students_study(2, True) is False
    assert students_study(2, False) is False


def test_students_study__day_hours_to_study():
    """Right day hours to study."""
    assert students_study(5, True) is True
    assert students_study(5, False) is False


def test_student_study__evening_edge_case_coffee_true():
    """Evening edge true cases."""
    assert students_study(24, True) is True
    assert students_study(18, True) is True


def test_student_study__evening_edge_case_coffee_false():
    """Evening edge false cases."""
    assert students_study(25, False) is False


def test_student_study__day_edge_case_coffee_true():
    """day edge cases."""
    assert students_study(16, True) is True


def test_student_study__day_edge_case_coffee_false():
    """day edge cases."""
    assert students_study(17, False) is False