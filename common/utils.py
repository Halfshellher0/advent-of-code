def read_file_lines(file_path: str) -> list:
    """Read all of the lines of a file into a string array"""
    lines = []
    file = open(file_path, "r")
    raw_lines = file.readlines()
    for line in raw_lines:
        lines.append(line.strip())
    return lines

def read_file_ints(file_path: str) -> list:
    """Read all of the lines of a file into an int array"""
    lines = []
    file = open(file_path, "r")
    raw_lines = file.readlines()
    for line in raw_lines:
        lines.append(int(line.strip()))
    return lines

def find_common_char(strings: list) -> str:
    """Find the character that is common between two or more strings"""
    if len(strings) > 1:
        char_set = set(strings[0])
        for i in range(1, len(strings)):
            char_set = char_set.intersection(strings[i])
        for s in char_set:
            return s