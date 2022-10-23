"""Tests."""
import pytest
from solution import students_study


def test_students_study__evening_not_coffee_needed():
    """In the evening it doesn't matter weather we have coffee."""
    assert students_study(20, True) is False
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
