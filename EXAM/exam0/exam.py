"""Exam 0."""
from typing import Optional


def find_capital_letters(string1: str):
    """Find all capital letters."""
    result = ""
    for letter in string1:
        if letter.isupper():
            result += letter
    return result


def close_far(a: int, b: int, c: int):
    """
    Return if one value is "close" and other is "far".

    #2

    Given three ints, a b c, return true if one of b or c is "close" (differing from a by at most 1),
    while the other is "far", differing from both other values by 2 or more.

    close_far(1, 2, 10) => True
    close_far(1, 2, 3) => False
    close_far(4, 1, 3) => True
    """
    if abs(a - b) <= 1 and abs(a - c) >= 2 and abs(b - c) >= 2:
        return True
    elif abs(a - c) <= 1 and abs(a - b) >= 2 and abs(c - b) >= 2:
        return True
    else:
        return False


def get_names_from_results(results_string: str, min_result: int) -> list:
    """
    Given a string of names and scores, return a list of names where the score is higher than or equal to min_result.

    #3

    Results are separated by comma (,). Result contains a score and optionally a name.
    Score is integer, name can have several names separated by single space.
    Name part can also contain numbers and other symbols (except for comma).
    Return only the names which have the score higher or equal than min_result.
    The order of the result should be the same as in input string.

    get_names_from_results("ago 123,peeter 11", 0) => ["ago", "peeter"]
    get_names_from_results("ago 123,peeter 11,33", 10) => ["ago", "peeter"]  # 33 does not have the name
    get_names_from_results("ago 123,peeter 11", 100) => ["ago"]
    get_names_from_results("ago 123,peeter 11,kitty11!! 33", 11) => ["ago", "peeter",  "kitty11!!"]
    get_names_from_results("ago 123,peeter 11,kusti riin 14", 12) => ["ago", "kusti riin"]
    """
    participants = results_string.split(",")
    winners = []
    for participant in participants:
        name_and_result = participant.split(" ")
        if len(name_and_result) >= 2:
            result = name_and_result.pop(-1)
            if int(result) >= min_result:
                winners.append(" ".join(name_and_result))
    return winners


def tic_tac_toe(game: list) -> int:
    """
    Find game winner.

    #4

    The 3x3 table is represented as a list of 3 rows, each row has 3 element (ints).
    The value can be 1 (player 1), 2 (player 2) or 0 (empty).
    The winner is the player who gets 3 of her pieces in a row, column or diagonal.

    There is only one winner or draw. You don't have to validate whether the game is in correct (possible) state.
    I.e the game could have four 1s and one 0 etc.

    tic_tac_toe([[1, 2, 1], [2, 1, 2], [2, 2, 1]]) => 1
    tic_tac_toe([[1, 0, 1], [2, 1, 2], [2, 2, 0]]) => 0
    tic_tac_toe([[2, 2, 2], [0, 2, 0], [0, 1, 0]]) => 2

    :param game
    :return: winning player id
    """
    for row in game:
        if row[0] == row[1] == row[2]:
            return row[0]
    for i in range(3):
        if game[0][i] == game[1][i] == game[2][i]:
            return game[0][i]
    if game[0][0] == game[1][1] == game[2][2] or game[0][2] == game[1][1] == game[2][0]:
        return game[1][1]
    else:
        return 0


if __name__ == '__main__':
    print(find_capital_letters("SasSHa"))
    print(close_far(1, 2, 3))
    print(get_names_from_results("ago 123,peeter 11,kitty11!! 33", 11))
    print(tic_tac_toe([[2, 2, 2], [0, 2, 0], [0, 1, 0]]))
