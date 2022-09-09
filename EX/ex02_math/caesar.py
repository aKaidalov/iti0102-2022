"""Caesar cipher."""


def encode(message: str, shift: int):
    """Encode a message using a Caesar cipher."""
    new_message: str = ""
    if shift > 26:  # If shift = 26 than it is the same letter
        shift %= 26  # Skips useless laps (lap = 26) and finds useful shift
    for element in message:  # Loop checks every letter per iteration
        if ord(element) > 122 or 97 > ord(element):  # Elements that not from a...z
            new_message += element  # Leave item the same
        else:
            new_element = ord(element) + shift
            if new_element > 122:
                new_element = 96 + (new_element - 122)  # Searches for element in range from a...z
                new_message += chr(new_element)  # Adds new element
            else:
                new_message += chr(new_element)
    return new_message


if __name__ == '__main__':
    print(encode("i like turtles", 6))  # -> o roqk zaxzrky
    print(encode("o roqk zaxzrky", 20))  # -> i like turtles
    print(encode("example", 1))  # -> fybnqmf
    print(encode("don't change", 0))  # -> don't change
    print(encode('the quick brown fox jumps over the lazy dog.', 7))  # -> aol xbpjr iyvdu mve qbtwz vcly aol shgf kvn.