"""Tests."""
import pytest
from solution import students_study
from solution import lottery
from solution import fruit_order


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
    assert students_study(24, True) is True


def test_student_study__evening_edge_case_coffee_false():
    """Evening edge false case False."""
    assert students_study(18, False) is True
    assert students_study(24, False) is True


def test_student_study__day_edge_case_coffee_true():
    """Day edge case True."""
    assert students_study(17, True) is True


def test_student_study__day_edge_case_coffee_false():
    """Day edge case False."""
    assert students_study(17, False) is False


def test_student_study__night_edge_case_coffee_true():
    """Night edge case True."""
    assert students_study(1, True) is False
    assert students_study(4, True) is False


def test_student_study__night_edge_case_coffee_false():
    """Night edge case False."""
    assert students_study(1, False) is False
    assert students_study(4, False) is False


# lottery
# ----------------------------------------------------------------------------------------------------------------------


def test_lottery__all_fives():
    """When all numbers are fives."""
    assert lottery(5, 5, 5) == 10


def test_lottery__all_same_positive():
    """When all numbers are the same and positive."""
    assert lottery(2, 2, 2) == 5


def test_lottery__all_same_negative():
    """When all numbers are the same and negative."""
    assert lottery(-2, -2, -2) == 5


def test_lottery__all_same_zero():
    """When all numbers are zeros."""
    assert lottery(0, 0, 0) == 5


def test_lottery__a_b_same_c_diff():
    """When a and b are same and c is different."""
    assert lottery(3, 3, 4) == 0


def test_lottery__a_c_same_b_diff():
    """When a and c are same and b is different."""
    assert lottery(5, 3, 5) == 0


def test_lottery__b_c_same_a_diff():
    """When b and c are same and a is different."""
    assert lottery(3, 4, 4) == 1


def test_lottery__all_diff():
    """When all are different."""
    assert lottery(2, 3, 4) == 1


# fruit order
# ----------------------------------------------------------------------------------------------------------------------


def test_fruit_order__all_zero():
    """When all are zeros."""
    assert fruit_order(0, 0, 0) == 0


def test_fruit_order__zero_amount_zero_small():
    """When order amount and amount of small baskets are equal to zero."""
    assert fruit_order(0, 3, 0) == 0


def test_fruit_order__zero_amount_zero_big():
    """Order amount and big baskets are 0."""
    assert fruit_order(6, 0, 0) == 0


def test_fruit_order__zero_amount_others_not_zero():
    """Only order amount is 0."""
    assert fruit_order(2, 3, 0) == 0


# big -----------------------------------------------
def test_fruit_order__only_big_exact_match():
    """Amount of big baskets is equal to order amount and small baskets are 0."""
    assert fruit_order(0, 2, 10) == 0


def test_fruit_order__only_big_not_enough():
    """Only big baskets are not enough."""
    assert fruit_order(0, 1, 6) == -1


def test_fruit_order__only_big_not_enough_but_multiple_of_5():
    """Only big baskets are not enough but order amount is multiple of 5."""
    assert fruit_order(0, 1, 10) == -1


def test_fruit_order__only_big_more_than_required_match():
    """Only amount of big baskets is more than required match."""
    assert fruit_order(0, 3, 10) == 0


def test_fruit_order__only_big_more_than_required_no_match():
    """Only amount of big baskets is more than required no match."""
    assert fruit_order(0, 2, 7) == -1


# small ---------------------------------------------
def test_fruit_order__only_small_exact_match():
    """Amount of small baskets is equal to order amount and big baskets are 0."""
    assert fruit_order(3, 0, 3) == 3


def test_fruit_order__only_small_not_enough():
    """Only small baskets are not enough."""
    assert fruit_order(6, 0, 7) == -1


def test_fruit_order__only_small_match_more_than_5_smalls():
    """Only small match(more than 5 smalls)."""
    assert fruit_order(9, 0, 9) == 9


def test_fruit_order__only_small_more_than_required():
    """Only smalls are more than required."""
    assert fruit_order(10, 0, 9) == 9


# all ---------------------------------------------
def test_fruit_order__match_with_more_than_5_smalls():
    """
    Fruit order match with more than 5 smalls.

    Covers also fruit_order__all_positive_exact_match.
    """
    assert fruit_order(6, 2, 16) == 6


def test_fruit_order__use_all_smalls_some_bigs():
    """All smalls and some bigs."""
    assert fruit_order(4, 3, 9) == 4


def test_fruit_order__use_some_smalls_all_bigs():
    """Some smalls and all bigs."""
    assert fruit_order(2, 2, 11) == 1


def test_fruit_order__use_some_smalls_some_bigs():
    """Some smalls and some bigs."""
    assert fruit_order(4, 3, 12) == 2


def test_fruit_order__not_enough():
    """Not enough."""
    assert fruit_order(2, 2, 14) == -1


def test_fruit_order__enough_bigs_not_enough_smalls():
    """Enough bigs and not enough smalls."""
    assert fruit_order(2, 2, 8) == -1


def test_fruit_order__not_enough_with_more_than_5_smalls():
    """Not enough with more than 5 smalls."""
    assert fruit_order(7, 1, 15) == -1


def test_fruit_order__enough_bigs_not_enough_smalls_large_numbers():
    """Enough bigs and not enough smalls in large numbers."""
    assert fruit_order(54, 1000, 5059) == -1
