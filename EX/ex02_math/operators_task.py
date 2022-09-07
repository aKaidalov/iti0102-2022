"""Math operators."""


def add(x: int, y: int):
    """Add x to y."""
    return x + y


def sub(x: int, y: int):
    """Subtract y from x."""
    return x - y


def multiply(x: int, y: int):
    """Multiply x by y."""
    return x * y


def div(x: int, y: int):
    """Divide x by y."""
    return x / y


def modulus(x: int, y: int):
    """Divide x by y and return remainder. Use an arithmetic operator."""
    return x % y


def floor_div(x: int, y: int):
    """Divide x by y and floor the value. Use an arithmetic operator."""
    return x // y


def exponent(x: int, y: int):
    """Calculate x raised to the power of y."""
    return x ** y


def first_greater_or_equal(x: int, y: int):
    """If x is greater or equal than y then return True. If not then return False."""
    if x >= y:
        return True
    else:
        return False


def second_less_or_equal(x: int, y: int):
    """If y is less or equal than x then return True. If not then return False."""
    if y <= x:
        return True
    else:
        return False


def x_is_y(x: int, y: int):
    """If x value is the same as y value then return True. If not then return False."""
    if x == y:
        return True
    else:
        return False


def x_is_not_y(x: int, y: int):
    """If x value is not the same as y value then return True. If not then return False."""
    if x != y:
        return True
    else:
        return False


def if_else(a: int, b: int, c: int, d: int):
    """
    Create a program that has 4 numeric parameters.

    Multiply parameters 1-2 (multiply a by b) by each other and divide parameters 3-4 (divide c by d) by each other.
    Next check and return the greater value. If both values are the same then return 0 (number zero).
    """
    multiplication = a * b
    division = c / d
    if multiplication > division:
        return multiplication
    elif multiplication == division:
        return 0
    else:
        return division


def surface(a: int, b: int):
    """Add the missing parameters to calculate the surface of a rectangle. Calculate and return the value of the S."""
    return a * b


def volume(a: int, b: int, c: int):
    """Add the missing parameters to calculate the volume of a cuboid. Calculate and return the value of the volume."""
    return a * b * c


def clock(days: int, hours: int, minutes: int, seconds: int):
    """Convert all received time unit values to minutes and return the number of minutes received."""
    # days *= 1440
    # hours *= 60
    # seconds /= 60
    # minutes += days + hours + seconds
    # return minutes
    return minutes + (days * 1440) + (hours * 60) + (seconds / 60)


def calculate(num1: int, operand1: int, operand2: int):
    if num1 == 0:
        return operand1 + operand2
    elif num1 == 1:
        return operand1 - operand2
    elif num1 == 2:
        return operand1 * operand2
    elif num1 == 3:
        return operand1 / operand2
    else:
        print("The first number should be between 0...3")


if __name__ == '__main__':
    print(add(1, -2))  # -1
    print(sub(5, 5))  # 0
    print(multiply(5, 5))  # 25
    print(div(15, 5))  # 3
    print(modulus(9, 3))  # 0
    print(floor_div(3, 2))  # 1
    print(exponent(5, 5))  # 3125
    print(first_greater_or_equal(1, 2))  # False
    print(second_less_or_equal(5, 5))  # True
    print(x_is_y(1, 2))  # False
    print(x_is_not_y(1, 2))  # True
    print(if_else(1, 3, 5, 99))  # 3
    print(if_else(2, 1, 10, 5))  # 0
    print(surface(1, 2))  # 2
    print(volume(5, 5, 5))  # 125
    print(clock(0, 0, 1, 15))  # 1.25
    print(clock(0, 1, 5, 0))  # 65
    # Try "calculate" here
    print(calculate(1, 5, 2))  # 3
