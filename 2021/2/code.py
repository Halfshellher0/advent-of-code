# Import advent-of-code utils
import sys
sys.path.append('./common')
import utils
import pathlib

# Define paths of commonly used files.
path = pathlib.Path(__file__).parent.resolve()
input_path = f"{path}\input.txt"
sample_path = f"{path}\sample.txt"

directions = utils.read_file_lines(input_path)

# Problem A
horizontal_pos = 0
depth = 0
for direction in directions:
    split = direction.split(' ')
    movement_dir = split[0]
    movement_amt = int(split[1])
    if movement_dir == "forward":
        horizontal_pos += movement_amt
    elif movement_dir == "down":
        depth += movement_amt
    elif movement_dir == "up":
        depth -= movement_amt
print(horizontal_pos * depth)

# Problem B
horizontal_pos = 0
depth = 0
aim = 0
for direction in directions:
    split = direction.split(' ')
    movement_dir = split[0]
    movement_amt = int(split[1])
    if movement_dir == "forward":
        horizontal_pos += movement_amt
        depth += aim * movement_amt
    elif movement_dir == "down":
        aim += movement_amt
    elif movement_dir == "up":
        aim -= movement_amt
print(horizontal_pos * depth)