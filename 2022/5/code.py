# Import advent-of-code utils
import sys
sys.path.append('./common')
import utils
import pathlib
import queue
import re

# Define paths of commonly used files.
path = pathlib.Path(__file__).parent.resolve()
input_path = f"{path}\input.txt"
sample_path = f"{path}\sample.txt"

crate_stacks = []

def construct_stacks(crate_data: list[str]) -> list:
    num_stacks = int((len(crate_data[0]) + 1) / 4)
    for i in range(num_stacks):
        # Create a LifoQueue for each crate stack
        crate_stacks.append(queue.LifoQueue())
    stack_height = -1
    for line in crate_data:
        if line.__contains__("]"):
            # Crates on this row
            stack_height += 1
        else: 
            break
    for x in range(1, len(crate_data[0]), 4):
        for y in range(stack_height, -1, -1):
            if not crate_data[y][x] == " ":
                stack_num = int((x - 1) / 4)
                crate_stacks[stack_num].put(crate_data[y][x])      

def perform_moves(crate_data: list[str]) -> None:
    for line in crate_data:
        if line and line[0] == "m":
            instruction = line[5:]
            num_crates = int(instruction.split(' ')[0])
            from_stack = int(instruction.split("from")[1].split("to")[0].strip()) -1
            to_stack = int(instruction.split("to")[1].strip()) -1
            for i in range(num_crates):
                crate_stacks[to_stack].put(crate_stacks[from_stack].get())

def perform_moves_multi_pick(crate_data: list[str]) -> None:
    for line in crate_data:
        if line and line[0] == "m":
            instruction = line[5:]
            num_crates = int(instruction.split(' ')[0])
            from_stack = int(instruction.split("from")[1].split("to")[0].strip()) -1
            to_stack = int(instruction.split("to")[1].strip()) -1
            temp_stack = queue.LifoQueue()
            for i in range(num_crates):
                temp_stack.put(crate_stacks[from_stack].get())
            for i in range(num_crates):
                crate_stacks[to_stack].put(temp_stack.get())      
            
            


crate_data = utils.read_file_lines_whitespace(input_path)

# Problem A
crate_stacks = []
construct_stacks(crate_data)
perform_moves(crate_data)
message = ""
for crate_stack in crate_stacks:
    message += crate_stack.get()
print(message)

# Problem B
crate_stacks = []
construct_stacks(crate_data)
perform_moves_multi_pick(crate_data)
message = ""
for crate_stack in crate_stacks:
    message += crate_stack.get()
print(message)

