"""Create schedule from the given file."""
import re


# def create_table(...):
#     """Create table."""
#
# def get_table_sizes(...):
#     """Get the maximum sizes for table."""
#
# def get_hours_sorted(input_string: str):
#     """Sort hours in 24 format."""
#     dic = {}
#     for match in re.finditer(r"(?<=\s)(\d{1,2})\D(\d{1,2})\s+([A-Za-z]+)", input_string):
#         hours, minutes = int(match.group(1)), int(match.group(2))
#         if 0 <= hours < 24 and 0 <= minutes < 60:
#             hour = int(match.group(1))
#             if hour not in dic:
#                 dic[hour] = [int(match.group(2))]
#             else:
#                 dic[hour].append(int(match.group(2)))
#     return sorted(dic.items())


def get_formatted_time(input_string: str):
    """Format 24 hour time to the 12 hour time."""
    dic = {}
    for match in re.finditer(r"(?<=\s)(\d{1,2})\D(\d{1,2})\s+([A-Za-z]+)", input_string):
        hours, minutes = int(match.group(1)), int(match.group(2))
        if 0 <= hours < 24 and 0 <= minutes < 60:
            if hours < 12:
                option = "AM"
            else:
                hours -= 12
                option = "PM"
            if minutes < 10:
                minutes = f"{minutes:02}"       # adds 0, so we get single minutes as 00...09
            time = f"{hours}:{minutes} {option}"
            if time not in dic:
                dic[time] = [match.group(3)]
            else:
                dic[time].append(match.group(3))
    return dic


def sorted_am_and_pm(input_string: str):
    """Sort times."""
    dic = get_formatted_time(input_string)
    keys = dic.keys()
    new_dic = {}        # for sorting dic
    for key in keys:
        split = key.split(":")
        hour = int(split[0])
        double_split = split[1].split(" ")      # split minutes and AM/PM
        minutes = int(double_split[0])
        midday = double_split[1]
        time = [hour, minutes]
        if midday not in new_dic:
            new_dic[midday] = [time]
        else:
            new_dic[midday].append(time)
    return new_dic


def sorted_hours(input_string: str):
    """Sort times."""
    dic = sorted_am_and_pm(input_string)
    keys = sorted(dic.keys())
    new_dic = {}
    hours_in_dic = {}
    for key in keys:        # to get AM and then PM
        for element in dic[key]:        # element = time [11, 1]
            if element[0] not in hours_in_dic:
                hours_in_dic[element[0]] = [element[1]]
            else:
                hours_in_dic[element[0]].append(element[1])
        if key not in new_dic:
            new_dic[key] = [sorted(hours_in_dic.items())]
        else:
            new_dic[key].append(sorted(hours_in_dic.items()))

    return new_dic


def create_schedule_file(input_filename: str, output_filename: str) -> None:
    """Create schedule file from the given input file."""
    pass


def create_schedule_string(input_string: str) -> str:
    """Create schedule string from the given input string."""
    pass


if __name__ == '__main__':
    print(sorted_hours("wat 13:00 teine tekst 11:0 23-59 canuseminustherege pikktekst 08:01 Lorem  21:59 nopoint 18:19 Donec 18.1 ds"))
    create_schedule_file("schedule_input.txt", "schedule_output.txt")
