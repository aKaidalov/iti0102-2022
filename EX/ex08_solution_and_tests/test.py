"""Tests."""
import pytest
from solution import students_study
from solution import lottery


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
    """Evening edge true case True."""
    assert students_study(18, True) is True
    # assert students_study(24, True) is True


def test_student_study__evening_edge_case_coffee_false():
    """Evening edge false case False."""
    assert students_study(18, False) is True
    # assert students_study(24, False) is True


def test_student_study__day_edge_case_coffee_true():
    """Day edge case True."""
    assert students_study(17, True) is True


def test_student_study__day_edge_case_coffee_false():
    """Day edge case False."""
    assert students_study(17, False) is False


def test_student_study__night_edge_case_coffee_true():
    """Night edge case True."""
    assert students_study(1, True) is False
    # assert students_study(4, True) is False


def test_student_study__night_edge_case_coffee_false():
    """Night edge case False."""
    assert students_study(1, False) is False
    # assert students_study(4, False) is False


# lottery
# ----------------------------------------------------------------------------------------------------------------------

def test_lottery__all_fives():
    """When all numbers are fives."""
    assert lottery(5, 5, 5) == 10
