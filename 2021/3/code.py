# Import advent-of-code utils
import sys
sys.path.append('./common')
import utils
import pathlib

# Define paths of commonly used files.
path = pathlib.Path(__file__).parent.resolve()
input_path = f"{path}\input.txt"
sample_path = f"{path}\sample.txt"

binary_strings = utils.read_file_lines(input_path)

# Problem A
gamma = ""
epsilon = ""
for i in range(0, len(binary_strings[0])):
    count_0 = 0
    count_1 = 0
    for binary_string in binary_strings:
        if binary_string[i] == "0":
            count_0 += 1
        else:
            count_1 += 1
    if count_0 > count_1:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"
gamma_rate = utils.binary_string_to_int(gamma)
epsilon_rate = utils.binary_string_to_int(epsilon)
print(gamma_rate * epsilon_rate)

# Problem B
remaining_ox_strings = binary_strings
remaining_co2_strings = binary_strings
ox = 0
co2 = 0
for i in range(0, len(binary_strings[0])):
    count_0 = 0
    count_1 = 0
    for binary_string in remaining_ox_strings:
        if binary_string[i] == "0":
            count_0 += 1
        else:
            count_1 += 1
    if count_0 > count_1:
        remaining_ox_strings = [ox_string for ox_string in remaining_ox_strings if ox_string[i] == "0"]
    elif count_1 > count_0:
        remaining_ox_strings = [ox_string for ox_string in remaining_ox_strings if ox_string[i] == "1"]
    else:
        remaining_ox_strings = [ox_string for ox_string in remaining_ox_strings if ox_string[i] == "1"]
    if len(remaining_ox_strings) == 1:
        ox = utils.binary_string_to_int(remaining_ox_strings[0])
        break

for i in range(0, len(binary_strings[0])):
    count_0 = 0
    count_1 = 0
    for binary_string in remaining_co2_strings:
        if binary_string[i] == "0":
            count_0 += 1
        else:
            count_1 += 1
    if count_0 > count_1:
        remaining_co2_strings = [co2_string for co2_string in remaining_co2_strings if co2_string[i] == "1"]
    elif count_1 > count_0:
        remaining_co2_strings = [co2_string for co2_string in remaining_co2_strings if co2_string[i] == "0"]
    else:
        remaining_co2_strings = [co2_string for co2_string in remaining_co2_strings if co2_string[i] == "0"]

    if len(remaining_co2_strings) == 1:
        co2 = utils.binary_string_to_int(remaining_co2_strings[0])
        break
print(ox * co2)