"""MX OOP."""


class Student:
    """Student class."""
    def __init__(self, name: str):
        """
        Person constructor.

        :param name: First name of the person.
        :param finished: By default is False.
        """
        self.name = name
        self.finished = False


if __name__ == '__main__':
    student = Student("John")
    print(student.name)  # John
    print(student.finished)  # False
