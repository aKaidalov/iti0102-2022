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


