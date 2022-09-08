"""Prime number identifier."""


def is_prime_number(number: int):

    list = [2, 3, 5, 7, 11]

    if number <= 0 or number == 1:
        print("Number must be > 1.")
        return False

    for i in range(len(list)):
        if number == list[i]:
            return True
        modulo = number % list[i]
        if modulo == 0:
            return False

    if True:
        return True


if __name__ == '__main__':
    print(is_prime_number(2))  # -> True
    print(is_prime_number(89))  # -> True
    print(is_prime_number(23))  # -> True
    print(is_prime_number(4))  # -> False
    print(is_prime_number(7))  # -> True
    print(is_prime_number(88))  # -> False

    print(is_prime_number(37))
