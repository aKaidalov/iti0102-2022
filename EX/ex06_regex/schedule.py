"""Create schedule from the given file."""
import re


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
    """Sort times by AM and PM."""
    dic = get_formatted_time(input_string)
    keys = dic.keys()
    am_list = []
    pm_list = []
    for key in keys:
        if "AM" in key:
            am_list.append(key)
        else:
            pm_list.append(key)
    return [am_list, pm_list]


def sorted_am_or_pm_hours(midday_list: list):
    """Sort by hours."""
    hours = []
    new_am_or_pm_list = []
    for element in midday_list:
        el = element.split(":")
        if int(el[0]) not in hours:     # convert el[0] in int because hours list consists of int elements
            hours.append(int(el[0]))
    hours_were_sorted = sorted(hours)
    for h in hours_were_sorted:     # 'h' stands for hour
        for e in midday_list:       # 'e' stands for element
            control = e.split(":")
            if h == int(control[0]) and control[0] not in new_am_or_pm_list:
                new_am_or_pm_list.append(e)
    return new_am_or_pm_list


# minutes = []
#     new_minutes_list = []
#     for element in am_or_pm_hours_list:
#         elem = element.split(":")       # ['11', '00 PM']
#         el = elem[1].split(" ")         # ['00', 'PM']
#         if int(el[0]) not in minutes:  # convert el[0] in int because minutes list consists of int elements
#             minutes.append(int(el[0]))
#     minutes_were_sorted = sorted(minutes)
#
#  new_minutes_list_to_sort = []       # if there is more than 1 same hour with dif. minutes
def sorted_by_minutes(am_or_pm_hours_list: list):
    """Sort by minutes."""
    hours = []
    hours_to_count = []
    new_minutes_list = []
    new_minutes_list_to_sort = []
    for element in am_or_pm_hours_list:
        el = element.split(":")
        hours_to_count.append(int(el[0]))
        if int(el[0]) not in hours:  # convert el[0] in int because hours list consists of int elements
            hours.append(int(el[0]))
    hours_were_sorted = sorted(hours)
    for h in hours_were_sorted:       # 'h' stands for hour
        if hours_to_count.count(h) > 1:      # works if in main list is more than 1 same hour. For sorting minutes for same hour
            for e in am_or_pm_hours_list:       # 'e' stands for element
                pre_control = e.split(":")
                if int(pre_control[0]) == h:
                    control = pre_control[1].split(" ")
                    if control[0] not in new_minutes_list:
                        new_minutes_list_to_sort.append(int(control[0]))
            new_minutes_list_to_sort = sorted(new_minutes_list_to_sort)
            for i in new_minutes_list_to_sort:      # sort founded minutes for same hour
                for ele in am_or_pm_hours_list:     # for matching element
                    elem = ele.split(":")  # ['11', '00 PM']
                    if int(elem[0]) == h:
                        el = elem[1].split(" ")  # ['00', 'PM']
                        if i == int(el[0]):
                            new_minutes_list.append(ele)
                            break       # the meaning is only one, so we stop further looking
            new_minutes_list_to_sort = []  # if there is more than 1 same hour with dif. minutes
        else:
            for hour in am_or_pm_hours_list:
                elem = hour.split(":")
                if h == int(elem[0]):  # convert el[0] in int because hours list consists of int elements
                    new_minutes_list.append(hour)
                    break
    return new_minutes_list


def create_schedule_file(input_filename: str, output_filename: str) -> None:
    """Create schedule file from the given input file."""
    pass


def create_schedule_string(input_string: str):      # -> str: Ubral dlja proverki
    """Create schedule string from the given input string."""
    am_and_pm_lists = sorted_am_and_pm(input_string)
    am_list = am_and_pm_lists[0]
    pm_list = am_and_pm_lists[1]
    am_sorted_hours = sorted_am_or_pm_hours(am_list)
    pm_sorted_hours = sorted_am_or_pm_hours(pm_list)
    sorted_time = sorted_by_minutes(am_sorted_hours)
    sorted_time_pm = sorted_by_minutes(pm_sorted_hours)
    for element in sorted_time_pm:
        sorted_time.append(element)
    return sorted_time


if __name__ == '__main__':
    print(create_schedule_string("wat 13:00 wat 10:00 teine tekst 11:0 23-59 canuseminustherege pikktekst 08:04 Lorem  21:59 nopoint 18:19 Donec 18.1 ds 09:01 Lorem 0:0 Lorem 8:1 Lorem 8:3 Lorem 20:1 Lorem 20:0 Lorem 18:18 Lorem"))
    create_schedule_file("schedule_input.txt", "schedule_output.txt")
