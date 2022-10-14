"""Files."""
import csv


def read_file_contents(filename: str) -> str:
    """
    Read file contents into string.

    In this exercise, we can assume the file exists.

    :param filename: File to read.
    :return: File contents as string.
    """
    with open(filename) as f:
        return f.read()


def read_file_contents_to_list(filename: str) -> list:
    """
    Read file contents into list of lines.

    In this exercise, we can assume the file exists.
    Each line from the file should be a separate element.
    The order of the list should be the same as in the file.

    List elements should not contain new line.

    :param filename: File to read.
    :return: List of lines.
    """
    with open(filename) as f:
        list = f.readlines()
        new_list = []
        for element in list:
            new_list.append(element.strip("\n"))
        return new_list


def read_csv_file(filename: str) -> list:
    """
    Read CSV file into list of rows.

    Each row is also a list of "columns" or fields.

    CSV (Comma-separated values) example:
    name,age
    john,12
    mary,14

    Should become:
    [
      ["name", "age"],
      ["john", "12"],
      ["mary", "14"]
    ]

    Use csv module.

    :param filename: File to read.
    :return: List of lists.
    """
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        list = []
        for row in csv_reader:
            list.append(row)
        return list


def write_contents_to_file(filename: str, contents: str) -> None:
    """
    Write contents to file.

    If the file does not exist, create it.

    :param filename: File to write to.
    :param contents: Content to write to.
    :return: None
    """
    with open(filename, "w") as csv_file:
        csv_file.write(contents)


def write_lines_to_file(filename: str, lines: list) -> None:
    """
    Write lines to file.

    Lines is a list of strings, each represents a separate line in the file.

    There should be no new line in the end of the file.
    Unless the last element itself ends with the new line.

    :param filename: File to write to.
    :param lines: List of string to write to the file.
    :return: None
    """
    with open(filename, "w") as file:
        for row in lines:
            if lines.index(row) == len(lines) - 1:
                file.writelines(row)
            else:
                file.writelines(row + '\n')


def write_csv_file(filename: str, data: list) -> None:
    """
    Write data into CSV file.

    Data is a list of lists.
    List represents lines.
    Each element (which is list itself) represents columns in a line.

    [["name", "age"], ["john", "11"], ["mary", "15"]]
    Will result in csv file:

    name,age
    john,11
    mary,15

    Use csv module here.

    :param filename: Name of the file.
    :param data: List of lists to write to the file.
    :return: None
    """
    with open(filename, "w", newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        for row in data:
            csv_writer.writerow(row)


def read_csv_file_for_last_function(filename: str, delimiter: str) -> list:
    """Read CSV file into list of rows."""
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=delimiter)
        list = []
        for row in csv_reader:
            list.append(row)
        return list


def write_csv_file_for_last_function(filename: str, data: list) -> list:
    """Write data into CSV file."""
    first_row = ["name", "town", "date"]
    with open(filename, "w", newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(first_row)
        for row in data:
            csv_writer.writerow(row)


def merge_dates_and_towns_into_csv(dates_filename: str, towns_filename: str, csv_output_filename: str) -> None:
    """
    Merge information from two files into one CSV file.

    Dates file contains names and dates. Separated by colon.
    john:01.01.2001
    mary:06.03.2016

    You don't have to validate the date.
    Every line contains name, colon and date.

    Towns file contains names and towns. Separated by colon.
    john:london
    mary:new york

    Every line contains name, colon and town name.
    There are no headers in the input files.

    Those two files should be merged by names.
    The result should be a csv file:

    name,town,date
    john,london,01.01.2001
    mary,new york,06.03.2016

    Applies for the third part:
    If information about a person is missing, it should be "-" in the output file.

    The order of the lines should follow the order in dates input file.
    Names which are missing in dates input file, will follow the order
    in towns input file.
    The order of the fields is: name,town,date

    name,town,date
    john,-,01.01.2001
    mary,new york,-

    Hint: try to reuse csv reading and writing functions.
    When reading csv, delimiter can be specified.

    :param dates_filename: Input file with names and dates.
    :param towns_filename: Input file with names and towns.
    :param csv_output_filename: Output CSV-file with names, towns and dates.
    :return: None
    """
    names_and_dates_list = read_csv_file_for_last_function(dates_filename, ':')
    names_and_towns_list = read_csv_file_for_last_function(towns_filename, ':')
    dic = {}
    list = []

    # Add all names with dates to the dictionary. Names are unique.
    for name_and_date in names_and_dates_list:
        if name_and_date[1] == "":
            name_and_date[1] = "-"
        dic[name_and_date[0]] = [name_and_date[1]]
    # find towns for people in the dict
    for name_and_town in names_and_towns_list:
        if name_and_town[1] == "":
            name_and_town[1] = "-"
        if name_and_town[0] in dic:
            dic[name_and_town[0]].insert(0, name_and_town[1])
        else:       # if person has only town
            dic[name_and_town[0]] = [name_and_town[1], "-"]
    # Add all dict values to list.
    for key in dic:
        if len(dic[key]) == 2:      # if there are town and date
            row = [key, dic[key][0], dic[key][1]]
            list.append(row)
        else:       # if town is missing
            row = [key, "-", dic[key][0]]
            list.append(row)

    write_csv_file_for_last_function(csv_output_filename, list)


if __name__ == '__main__':
    # data = [["name", "age"], ["john", "11"], ["mary", "15"]]
    # print(read_csv_file("all_files/ex_1/filename.txt"))
    print(merge_dates_and_towns_into_csv("all_files/ex_1/dates_filename.txt", "all_files/ex_1/towns_filename.txt", "all_files/ex_1/csv_output_filename.txt"))
