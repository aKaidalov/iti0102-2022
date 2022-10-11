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
                option = "PM"
            time = tuple([hours, minutes, f"{option}"])         # tuple for adding "time" as a key value
            if time not in dic:
                dic[time] = [match.group(3).casefold()]
            else:
                if match.group(3).casefold() not in dic[time]:
                    dic[time].append(match.group(3).casefold())
    return dic


def get_info_sorted(input_string: str):
    """Sort all the info."""
    dic = get_formatted_time(input_string)
    new_dic = sorted(dic, key=lambda key: (key[2], key[0], key[1]))     # sort by AM then hours and minutes
    list_to_join = []
    modified_dic = {}
    for element in new_dic:
        if element[0] == 0:  # so we get 12:.. instead of 0:..
            list_to_join.append("12")
        else:
            if element[0] > 12:  # prevent getting 0 as answer if time is 12 (midday)
                new_hour = element[0] - 12
                list_to_join.append(str(new_hour))
            else:
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
        value = ", ".join(dic[key])
        if value != "":
            if time_width < len(key):
                time_width = len(key)
    for value in values:
        length = ", ".join(value)
        if entries_width < len(length):
            entries_width = len(length)
    if entries_width < 7:
        entries_width = 7
    return time_width, entries_width        # tuple()


def create_table(dic: dict, time_width: int, entries_width: int):
    """Create table."""
    final_string = ""
    if len(dic) != 0:
        line_width = 1 + (time_width + 2) + 1 + (entries_width + 2) + 1
        empty_str = ""
        final_string += f"{empty_str:{'-'}^{line_width}}\n"
        final_string += f"| {'time':{' '}>{time_width}} | {'entries':{' '}<{entries_width}} |\n"
        final_string += f"{empty_str:{'-'}^{line_width}}\n"
        for element in dic:
            value = ", ".join(dic[element])
            if value != "":
                final_string += f"| {element:{' '}>{time_width}} | {value:{' '}<{entries_width}} |\n"
        final_string += f"{empty_str:{'-'}^{line_width}}"
    else:
        final_string += "--------------------\n"
        final_string += "|  time | entries  |\n"
        final_string += "--------------------\n"
        final_string += "| No entries found |\n"
        final_string += "--------------------\n"
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
    print(create_schedule_string("wat 13:00 wat 10:00 teine 12:34 teine tekst 11:0 23-59  pikktekst 08:04 Lorem  21:59 nopoint 18:19 Donec 18.1 ds 09:01 Lorem 0!0 Lorem 0!0 Lorem 8:1 Lorem 8:3 Lorem 20:1 Lorem 20:0 Lorem 18:18 Lorem"))
    print(create_schedule_string("wat 11:00 teine tekst 11:0 jah ei 10:00 pikktekst "))
    print(create_schedule_string("s 11:34 12:45 .  15:03 correct 11:12"))
    print(create_schedule_string("start efgveiyl ccxypzs tzxvjykde ckbeozifyr txnqdfykad fxfwut dnuyiba 20B05   VAzPDxk ycqed nrasmb ixyhkaheiw 21?25   vAzpDxk fluukxwlbz okhuqoqts diaugkjbz 01A26 vBxyhpK olzikybv isvmj 0:2  CRMwbcAnw wzonq xkocyzd tbfucg qljbaexaqe ffpzm hgmtgf scwrwxtuyn zxnnghi 16=21    QcCRnuEwL rfwuumc 10!38 VAzpdXK mlata ijwvtq 11-42    VbxYhPK kxqmijjmt trqywl yndyruxny qkpkbple jycbf dkyrpghegw tfzejp qiyqlxl 16A27  qcCrnUewL 09!55 CRmWbcANw dgtrl bazmctbx dqqtspqmpc rsccghv hrmuiisi oosagc qzdwduqys dvqtxg ordizhkiqi 23?44  vBxYhPk ukiszjwel gujxipeuu 11a08  sSvkC fgwdkrovq khdqudtwtt xccvfw pvqrlhy rkcqigxx neqkykikir 04b15   CrmWBcANW laozyk sukdmonpk 15?52   QDVgPgbhfb mxlznz qlehj fpgvaittb fifnronrjw hoiixjnpv qyexm orjxmy opwdgxait -1a28  vbxyHPK wgezjlqya trkjut xbzbshhw ykakm mlvjqfd nrclpkh xvpojg zjmrsxfgdo trmsw 13B20  fNyOsB ggslfcadd fsveswow hurxho yqlojo 25a20    iaXAdUyRf"))
    create_schedule_file("schedule_input.txt", "schedule_output.txt")
