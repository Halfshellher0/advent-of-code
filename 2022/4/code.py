# Import advent-of-code utils
import sys
sys.path.append('./common')
import utils
import pathlib

# Define paths of commonly used files.
path = pathlib.Path(__file__).parent.resolve()
input_path = f"{path}\input.txt"
sample_path = f"{path}\sample.txt"

def range_to_int_array(elf_range: str) -> list:
    nums = []
    ends = elf_range.split('-')
    start = int(ends[0])
    end = int(ends[1])
    for i in range(start, end + 1):
        nums.append(i)
    return nums

def pair_to_ints(pairing: str) -> list:
    ints = []
    pairs = pairing.split(',')
    for range in pairs:
        ints.append(range_to_int_array(range))
    return ints

def one_pair_contained(ints: list) -> bool:
    int_set = set(ints[0]).intersection(ints[1])
    if len(int_set) == len(ints[0]) or len(int_set) == len(ints[1]):
        return True
    return False

def pairs_overlap(ints: list) -> bool:
    int_set = set(ints[0]).intersection(ints[1])
    if len(int_set) > 0:
        return True
    return False


pairings = utils.read_file_lines(input_path)

# Problem A
contained_count = 0
for pairing in pairings:
    if one_pair_contained(pair_to_ints(pairing)):
        contained_count += 1
print(contained_count)

# Problem B
overlapped_count = 0
for pairing in pairings:
    if pairs_overlap(pair_to_ints(pairing)):
        overlapped_count += 1
print(overlapped_count)

