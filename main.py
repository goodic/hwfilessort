import os

class File:
    def __init__(self, name, fullname, lines):
        self.name = name
        self.fullname = fullname
        self.lines = lines

    def __lt__(self, other):
        if not isinstance(other, File):
            print("Error")
        else:
            return self.lines < other.lines


def count_lines(fullname):
    lines = 0
    with open(fullname, encoding="utf-8") as f:
        for line in f:
            lines += 1
    return lines


def get_reestr(dir_name):
    files = os.listdir(dir_name)
    reestr = []
    for file in files:
        fullname = os.path.join(dir_name, file)
        lines = count_lines(fullname)
        reestr.append(File(file, fullname, lines))
    reestr.sort()
    return reestr


def make_summary(dir_name):
    reestr = get_reestr(dir_name)
    new_line = '\n'
    result = ''
    for file in reestr:
        result += str(file.name) + new_line
        result += str(file.lines) + new_line
        with open(file.fullname, encoding="utf-8") as f:
            for line in f:
                result += line
        result += new_line
    return result


dir_name = 'sorted'
print(make_summary(dir_name))
