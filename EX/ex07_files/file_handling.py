"""Files."""
import csv
from datetime import datetime


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


def write_csv_file_for_last_function(filename: str, data: list):
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
        else:  # if person has only town
            dic[name_and_town[0]] = [name_and_town[1], "-"]
    # Add all dict values to list.
    for key in dic:
        if len(dic[key]) == 2:  # if there are town and date
            row = [key, dic[key][0], dic[key][1]]
            list.append(row)
        else:  # if town is missing
            row = [key, "-", dic[key][0]]
            list.append(row)

    write_csv_file_for_last_function(csv_output_filename, list)


# 2.osa
# ----------------------------------------------------------------------------------------------------------------------


def read_csv_file_into_list_of_dicts(filename: str) -> list:
    """
    Read csv file into list of dictionaries.

    Header line will be used for dict keys.

    Each line after header line will result in a dict inside the result list.
    Every line contains the same number of fields.

    Example2:

    name,age,sex
    John,12,M
    Mary,13,F

    Header line will be used as keys for each content line.
    The result:
    [
      {"name": "John", "age": "12", "sex": "M"},
      {"name": "Mary", "age": "13", "sex": "F"},
    ]

    If there are only header or no rows in the CSV-file,
    the result is an empty list.

    The order of the elements in the list should be the same
    as the lines in the file (the first line becomes the first element etc.)

    :param filename: CSV-file to read.
    :return: List of dictionaries where keys are taken from the header.
    """
    list = []
    dic = {}
    with open(filename) as csv_file:
        header = csv_file.readline().strip("\n").split(",")  # Take a first line as a keys value
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:  # Starts from second row, because the first line was already taken
            counter = 0
            for el in row:
                if el == "-":
                    dic[header[counter]] = None
                else:
                    dic[header[counter]] = el
                counter += 1  # to prevent an error with two elements ("-","-")
            list.append(dic)
            dic = {}
    return list


def write_list_of_dicts_to_csv_file(filename: str, data: list) -> None:
    """
    Write list of dicts into csv file.

    Data contains a list of dictionaries.
    Dictionary key represents the field.

    Example data:
    [
      {"name": "john", "age": "23"}
      {"name": "mary", "age": "44"}
    ]
    Will become:
    name,age
    john,23
    mary,44

    The order of fields/headers is not important.
    The order of lines is important (the same as in the list).

    Example:
    [
      {"name": "john", "age": "12"},
      {"name": "mary", "town": "London"}
    ]
    Will become:
    name,age,town
    john,12,
    mary,,London

    Fields which are not present in one line will be empty.

    The order of the lines in the file should be the same
    as the order of elements in the list.

    :param filename: File to write to.
    :param data: List of dictionaries to write to the file.
    :return: None
    """
    result = []
    # make header
    header = set()
    for element in data:
        keys = element.keys()  # receive dict_keys([age, name]). Control with debug.
        for key in keys:
            header.add(key)
    # add first row
    header_list = list(header)
    result.append(header_list)
    # sort data
    for dict in data:
        inner_list = []
        for element in header_list:
            if element in dict:
                inner_list.append(dict[element])
            else:
                inner_list.append("")
        result.append(inner_list)
    # write to csv file
    if result != [[]]:
        write_csv_file(filename, result)
    else:
        with open(filename, "w") as file:
            file.write("")


# 3.osa
# ----------------------------------------------------------------------------------------------------------------------


def read_csv_file_into_list_of_dicts_using_datatypes(filename: str) -> list:
    """
    Read data from file and cast values into different datatypes.

    If a field contains only numbers, turn this into int.
    If a field contains only dates (in format dd.mm.yyyy), turn this into date.
    Otherwise the datatype is string (default by csv reader).
    Example:
    name,age
    john,11
    mary,14
    Becomes ('age' is int):
    [
      {'name': 'john', 'age': 11},
      {'name': 'mary', 'age': 14}
    ]
    But if all the fields cannot be cast to int, the field is left to string.
    Example:
    name,age
    john,11
    mary,14
    ago,unknown
    Becomes ('age' cannot be cast to int because of "ago"):
    [
      {'name': 'john', 'age': '11'},
      {'name': 'mary', 'age': '14'},
      {'name': 'ago', 'age': 'unknown'}
    ]
    Example:
    name,date
    john,01.01.2020
    mary,07.09.2021
    Becomes:
    [
      {'name': 'john', 'date': datetime.date(2020, 1, 1)},
      {'name': 'mary', 'date': datetime.date(2021, 9, 7)},
    ]
    Example:
    name,date
    john,01.01.2020
    mary,late 2021
    Becomes:
    [
      {'name': 'john', 'date': "01.01.2020"},
      {'name': 'mary', 'date': "late 2021"},
    ]
    Value "-" indicates missing value and should be None in the result
    Example:
    name,date
    john,-
    mary,07.09.2021
    Becomes:
    [
      {'name': 'john', 'date': None},
      {'name': 'mary', 'date': datetime.date(2021, 9, 7)},
    ]
    None value also doesn't affect the data type
    (the column will have the type based on the existing values).
    The order of the elements in the list should be the same
    as the lines in the file.
    For date, strptime can be used:
    https://docs.python.org/3/library/datetime.html#examples-of-usage-date
    """
    list_with_dicts_and_strings = read_csv_file_into_list_of_dicts(filename)
    breakloop = False

    if not list_with_dicts_and_strings:
        return []

    list_of_types = [0 for i in range(
        len(list_with_dicts_and_strings[0]))]  # 0 - ne nado ismenjat' tip. 1 - izmenit na int, 2- na datetime
    for info in list_with_dicts_and_strings:
        counter = 0
        if breakloop:
            break
        for element1 in info:
            if info[element1] is not None:
                if not info[element1].isdigit():
                    try:
                        datetime.strptime(info[element1], '%d.%m.%Y')
                        list_of_types[counter] = 2
                    except ValueError:
                        list_of_types[counter] = 0
                        breakloop = True
                elif info[element1].isdigit():
                    list_of_types[counter] = 1
                else:
                    list_of_types[counter] = 0
                    breakloop = True
            counter += 1
    print(list_of_types)
    return change_types(list_of_types, list_with_dicts_and_strings)


def change_types(a: list, b: list) -> list:
    """Change types."""
    print(b)
    for i in b:
        counter = 0
        for key, value in i.items():
            if a[counter] == 1 and i[key] is not None and i[key].isdigit():
                i[key] = int(i[key])
            elif a[counter] == 2 and i[key] is not None and not i[key].isdigit():
                i[key] = datetime.strptime(i[key], '%d.%m.%Y')
                i[key] = i[key].date()
            counter += 1
    return b


if __name__ == '__main__':
    # data1 = [["name", "age"], ["john", "11"], ["mary", "15"]]
    # data2 = [{"name": "john", "age": "23"}, {"name": "mary", "age": "44"}]
    data2 = []
    # print(read_csv_file("all_files/ex_1/filename.txt"))
    # print(merge_dates_and_towns_into_csv("all_files/ex_1/dates_filename.txt", "all_files/ex_1/towns_filename.txt", "all_files/ex_1/csv_output_filename.txt"))
    # print(read_csv_file_into_list_of_dicts("all_files/ex_2/filename2.txt"))
    # print(write_list_of_dicts_to_csv_file("all_files/ex_2/csv_output_filename.txt", data2))
    print(read_csv_file_into_list_of_dicts_using_datatypes("all_files/ex_3/filename3.txt"))
