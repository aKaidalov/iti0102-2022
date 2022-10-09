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
        if int(el[0]) not in hours:     # convert el[0] in int because hours list consists of int
            hours.append(int(el[0]))
    hours_were_sorted = sorted(hours)
    for h in hours_were_sorted:
        for e in midday_list:
            control = e.split(":")
            if h == int(control[0]) and control[0] not in new_am_or_pm_list:
                new_am_or_pm_list.append(e)
    return new_am_or_pm_list


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
    return am_sorted_hours, pm_sorted_hours


if __name__ == '__main__':
    print(create_schedule_string("wat 13:00 wat 10:00 teine tekst 11:0 23-59 canuseminustherege pikktekst 08:01 Lorem  21:59 nopoint 18:19 Donec 18.1 ds 09:01 Lorem 0:0 Lorem 8:4 Lorem"))
    create_schedule_file("schedule_input.txt", "schedule_output.txt")
