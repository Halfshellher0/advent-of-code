# Import advent-of-code utils
import sys
sys.path.append('./common')
import utils
import pathlib

# Define paths of commonly used files.
path = pathlib.Path(__file__).parent.resolve()
input_path = f"{path}\input.txt"
sample_path = f"{path}\sample.txt"

def split_rucksack(rucksack: str) -> list:
    half = int(len(rucksack) / 2)
    return [rucksack[:half], rucksack[half:]]

def calc_priority(item: str) -> int:
    priority_str = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return priority_str.find(item)

rucksacks = utils.read_file_lines(input_path)

# Problem A
sum = 0
for rucksack in rucksacks:
    compartments = split_rucksack(rucksack)
    common_item = utils.find_common_char([compartments[0], compartments[1]])
    sum += calc_priority(common_item)
print(sum)

# Problem B
sum = 0
for i in range(0, len(rucksacks), 3):
    common_item = utils.find_common_char([rucksacks[i], rucksacks[i + 1], rucksacks[i + 2]])
    sum += calc_priority(common_item)
print(sum)
