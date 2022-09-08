"""Caesar cipher."""


def encode(message: str, shift: int):
    for element in message:
        if shift > 26:
            shift %= 26
        if 122 < ord(element) < 97:
            return False
        elif element == " ":
            print(" ", end="")
            continue
        else:
            element_num = ord(element) + shift
            if element_num > 122:
                element_num = 96 + (element_num - 122)
                element = chr(element_num)
            else:
                element = chr(element_num)
            print(element, end="")


if __name__ == '__main__':
    print(encode("i like turtles", 6))  # -> o roqk zaxzrky
    print(encode("o roqk zaxzrky", 20))  # -> i like turtles
    print(encode("example", 1))  # -> fybnqmf
    print(encode("don't change", 0))  # -> don't change
    print(encode('the quick brown fox jumps over the lazy dog.', 7))  # -> aol xbpjr iyvdu mve qbtwz vcly aol shgf kvn.