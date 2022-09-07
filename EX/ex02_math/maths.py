"""Maths."""


def average(a: int, b: int, c: int, d: int):
    """Calculate the arithmetic mean of the obtained numbers."""
    arithmetic_average = 0
    if a:
        arithmetic_average += a * 1
    if b:
        arithmetic_average += b * 2
    if c:
        arithmetic_average += c * 3
    if d:
        arithmetic_average += d * 4
    return arithmetic_average


# print(average(2, 2, 2, 2))


def school_pressure(ects: int, weeks: int):
    """Calculates the student's required contribution each week."""
    study_hours = ects * 26  # How many hours a student needs to study
    hours_in_weeks = weeks * 7 * 24
    if hours_in_weeks > study_hours:
        return study_hours / weeks
    else:
        return -1


print(school_pressure(6, 1))
