"""Create schedule from the given file."""
import re


def get_formatted_time(input_string: str):
    """Format 24 hour time to the 12 hour time."""
    dic = {}
    for match in re.finditer(r"(?<=\s)(\d{1,2})\D(\d{1,2})\s+([A-Za-z]*)", input_string):
        hours, minutes = int(match.group(1)), int(match.group(2))
        if 0 <= hours < 24 and 0 <= minutes < 60:
            if hours < 12:
                option = "AM"
            else:
                hours -= 12
                option = "PM"
            time = tuple([hours, minutes, f"{option}"])         # tuple for adding "time" as a key value
            if time not in dic:
                dic[time] = [match.group(3)]
            else:
                dic[time].append(match.group(3))
    return dic


def get_info_sorted(input_string: str):
    """Sort all the info."""
    dic = get_formatted_time(input_string)
    new_dic = sorted(dic, key=lambda key: (key[2], key[0], key[1]))     # sort by AM then hours and minutes
    list_to_join = []
    modified_dic = {}
    for element in new_dic:
        list_to_join.append(str(element[0]))
        if element[1] < 10:
            new_element_1 = f"{element[1]:02}"      # change hours format int -> str. Add 0, so we get single minutes as 00...09
        else:
            new_element_1 = str(element[1])
        list_to_join.append(new_element_1)
        time = ":".join(list_to_join)       # get "11:00"
        new_key = time + " " + element[2]       # get "11:00 PM"
        modified_dic[new_key] = dic[element]
        list_to_join = []       # prepare list for new iteration
    return modified_dic


def get_table_sizes(dic: dict):
    """Get the maximum sizes for table."""
    time_width = 0
    entries_width = 0
    values = dic.values()
    for key in dic:
        if time_width < len(key):
            time_width = len(key)
    for value in values:
        length = ",".join(value)
        if entries_width < len(length):
            entries_width = len(length)
    return time_width, entries_width        # tuple()


def create_table(dic: dict, time_width: int, entries_width: int):
    """Create table."""
    final_string = ""
    line_width = 1 + (time_width + 2) + 1 + (entries_width + 2) + 1
    empty_str = ""
    final_string += f"{empty_str:{'-'}^{line_width}}\n"
    final_string += f"| {'time':{' '}>{time_width}} | {'entries':{' '}<{entries_width}} |\n"
    final_string += f"{empty_str:{'-'}^{line_width}}\n"
    for element in dic:
        value = ",".join(dic[element])
        if value != '':
            final_string += f"| {element:{' '}>{time_width}} | {value:{' '}<{entries_width}} |\n"
        else:
            final_string += f"{empty_str:{'-'}^{line_width}}\n"
            final_string += f"| {'No entries found':{' '}^{line_width - 4}} |\n"
            final_string += f"{empty_str:{'-'}^{line_width}}\n"
    final_string += f"{empty_str:{'-'}^{line_width}}"
    return final_string


def create_schedule_file(input_filename: str, output_filename: str) -> None:
    """Create schedule file from the given input file."""
    with open(f"{input_filename}.txt", encoding="utf-8") as file:
        input_string = file.read()
    dic = get_info_sorted(input_string)
    width = get_table_sizes(dic)
    time_max_width, entries_max_width = width[0], width[1]
    string = create_table(dic, time_max_width, entries_max_width)
    with open(f"{output_filename}.txt", "w", encoding="utf-8") as file:
        file.write(string)


def create_schedule_string(input_string: str) -> str:
    """Create schedule string from the given input string."""
    dic = get_info_sorted(input_string)
    width = get_table_sizes(dic)
    time_max_width, entries_max_width = width[0], width[1]
    string = create_table(dic, time_max_width, entries_max_width)
    return string


if __name__ == '__main__':
    print(create_schedule_string("wat 13:00 wat 10:00 teine tekst 11:0 23-59 canusemigrbibrt pikktekst 08:04 Lorem  21:59 nopoint 18:19 Donec 18.1 ds 09:01 Lorem 0!0 Lorem 8:1 Lorem 8:3 Lorem 20:1 Lorem 20:0 Lorem 18:18 Lorem"))
    print(create_schedule_string("wat 11:00 teine tekst 11:0 jah ei 10:00 pikktekst "))
    create_schedule_file("schedule_input.txt", "schedule_output.txt")
