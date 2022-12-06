# Import advent-of-code utils
import sys
sys.path.append('./common')
import utils
import pathlib
import re

# Define paths of commonly used files.
path = pathlib.Path(__file__).parent.resolve()
input_path = f"{path}\input.txt"
sample_path = f"{path}\sample.txt"


def has_matching_char(string: str) -> bool:
    if re.search(r'^.*(.).*\1.*$', string):
        return True
    else:
        return False

string = utils.read_file_as_string(sample_path)

# Problem A
count = 4
for i in range(len(string)):
    check_string = string[i] + string[i + 1] + string[i + 2] + string[i + 3]
    if not has_matching_char(check_string):
        print(count)
        break
    count += 1

# Problem B
count = 14
for i in range(len(string)):
    check_string = string[i] + string[i + 1] + string[i + 2] + string[i + 3] + string[i + 4] + string[i + 5] + string[i + 6] + string[i + 7] + string[i + 8] + string[i + 9] + string[i + 10] + string[i + 11] + string[i + 12] + string[i + 13]
    if not has_matching_char(check_string):
        print(count)
        break
    count += 1