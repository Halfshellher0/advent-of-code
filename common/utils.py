def read_file_lines(file_path: str) -> list[str]:
    """Read all of the lines of a file into a string array"""
    lines = []
    file = open(file_path, "r")
    raw_lines = file.readlines()
    for line in raw_lines:
        lines.append(line.strip())
    return lines

def read_file_ints(file_path: str) -> list[int]:
    """Read all of the lines of a file into an int array"""
    lines = []
    file = open(file_path, "r")
    raw_lines = file.readlines()
    for line in raw_lines:
        lines.append(int(line.strip()))
    return lines

def read_file_lines_whitespace(file_path: str) -> list[str]:
    """Read all of the lines of a file into a string array (keeps whitespace characters)"""
    lines = []
    file = open(file_path, "r")
    raw_lines = file.readlines()
    for line in raw_lines:
        lines.append(line.replace("\n", ""))
    return lines

def read_file_as_string(file_path: str) -> str:
    """Read all of the lines of a file into a single string"""
    lines = []
    file = open(file_path, "r")
    raw_lines = file.readlines()
    string = ""
    for line in raw_lines:
        string += line.strip()
    return string

def find_common_char(strings: list) -> str:
    """Find the character that is common between two or more strings"""
    if len(strings) > 1:
        char_set = set(strings[0])
        for i in range(1, len(strings)):
            char_set = char_set.intersection(strings[i])
        for s in char_set:
            return s

def binary_string_to_int(string: str) -> int:
    """Convert a binary string to an int"""
    return int(string, 2)

def string_list_to_int_list(string_list) -> list[int]:
    """Convert a list of strings into a list of ints"""
    return [int(i) for i in string_list]
