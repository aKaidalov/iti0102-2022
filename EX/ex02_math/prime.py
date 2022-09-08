"""Prime number identifier."""


def is_prime_number(number: int):

    if number <= 1:
        print("Number must be > 1.")
        return False

    for i in range(2, number):
        modulo = number % i     # Finds modulo
        if modulo == 0:     # If modulo is 0 then number divides more than by 1 and itself
            return False

    return True


if __name__ == '__main__':
    print(is_prime_number(2))  # -> True
    print(is_prime_number(89))  # -> True
    print(is_prime_number(23))  # -> True
    print(is_prime_number(4))  # -> False
    print(is_prime_number(7))  # -> True
    print(is_prime_number(88))  # -> False
    print(is_prime_number(5))  # True
    print(is_prime_number(8))  # False
