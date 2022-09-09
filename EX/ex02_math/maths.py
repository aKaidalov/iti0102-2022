"""Maths."""


def average(a: int, b: int, c: int, d: int):
    """Calculate the arithmetic mean of the obtained numbers."""
    return ((a * 1) + (b * 2) + (c * 3) + (d * 4)) / 4


def school_pressure(ects: int, weeks: int):
    """Calculate the student's required contribution each week."""
    study_hours = ects * 26  # How many hours a student needs to study
    hours_in_weeks = weeks * 7 * 24
    if hours_in_weeks > study_hours:
        return study_hours / weeks
    else:
        return -1


def add_fractions(a: int, b: int, c: int, d: int):
    """Add fractions."""
    if (b or d) == 0:
        return print("Can't divide by 0")
    elif b == d:
        numerator = a + c
        denominator = b
        return str(numerator) + "/" + str(denominator)
    else:
        numerator = a * d + c * b
        denominator = b * d
        return str(numerator) + "/" + str(denominator)


if __name__ == '__main__':
    print(average(1, 2, 3, 4))
    print("Weekly you need to spent: " + str(school_pressure(1, 0)) + " hours")
    print(add_fractions(1, 3, 1, 3))
