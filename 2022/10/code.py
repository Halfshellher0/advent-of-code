# Import advent-of-code utils
import sys
sys.path.append('./common')
import utils
import pathlib
from collections import namedtuple

# Define paths of commonly used files.
path = pathlib.Path(__file__).parent.resolve()
input_path = f"{path}\input.txt"
sample_path = f"{path}\sample.txt"

instructions: list[str] = utils.read_file_lines(input_path)

def is_lit(position: int, x: int) -> bool:
    position = position % 40
    if position in [x-1, x, x+1]:
        return True
    return False

def print_crt(pixels: list[bool]) -> None:
    i = 0
    data = ""
    for pixel in pixels:
        if pixel:
            data += "#"
        else:
            data += "."
        i += 1
        if i == 40:
            data += "\n"
            i = 0
    print(data)

#Problem A
cycle: int = 1
x: int = 1
signal_strength_total: int = 0
for instruction in instructions:
    # Beginning of cycle
    instruction = instruction.split(" ")
    cycle_increase = 0
    add_amount = 0
    match instruction[0]:
        case "noop":
            cycle_increase = 1
        case "addx":
            cycle_increase = 2
            add_amount = int(instruction[1])
    
    for i in range(cycle_increase):
        # During cycle        
        if cycle in [20, 60, 100, 140, 180, 220]:
            signal_strength_total += x * cycle        
        cycle += 1
    
    # End of cycle
    x += add_amount
print(signal_strength_total)

#Problem B
cycle: int = 1
x: int = 1
pixels: list[bool] = []
for instruction in instructions:
    # Beginning of cycle
    instruction = instruction.split(" ")
    cycle_increase = 0
    add_amount = 0
    match instruction[0]:
        case "noop":
            cycle_increase = 1
        case "addx":
            cycle_increase = 2
            add_amount = int(instruction[1])
    
    for i in range(cycle_increase):
        # During cycle       
        pixels.append(is_lit(cycle - 1, x))      
        cycle += 1
    
    # End of cycle
    x += add_amount
print_crt(pixels)
