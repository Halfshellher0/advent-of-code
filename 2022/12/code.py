# Import advent-of-code utils
import sys
sys.path.append('./common')
import utils
import pathlib
import queue
from collections import namedtuple

# Define paths of commonly used files.
path = pathlib.Path(__file__).parent.resolve()
input_path = f"{path}\input.txt"
sample_path = f"{path}\sample.txt"
Position = namedtuple('Position',['x','y'])

data = utils.read_file_lines(input_path)
max_width = len(data[0])
max_height = len(data)
height_map: list[list[int]] = []
visited_map: list[list[int]] = []
height_row: list[int] = []
start_pos = Position(0, 0)
end_pos = Position(0, 0)
pos_queue = queue.Queue()
move_count = 0
nodes_left_in_layer = 1
nodes_in_next_layer = 0

def letter_height(item: str) -> int:
    priority_str = "abcdefghijklmnopqrstuvwxyz"
    return priority_str.find(item)

def queue_neighbors(pos: Position):
    global nodes_in_next_layer, visited_map, pos_queue
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_x = pos.x + dx
        new_y = pos.y + dy
        if new_x < 0 or new_x >= max_width or new_y < 0 or new_y >= max_height:
            continue
        elif visited_map[new_y][new_x]:
            continue
        pos_height = height_map[pos.y][pos.x]
        target_height = height_map[new_y][new_x]
        if target_height > (pos_height + 1):
            continue
        pos_queue.put(Position(new_x, new_y))
        nodes_in_next_layer += 1
        visited_map[new_y][new_x] = True

def reset_visited_map():
    for i in range(max_width):
        for j in range(max_height):
            visited_map[j][i] = False

# Problem A
y = 0
for row in data:
    height_row = []
    visited_row = []
    x = 0
    for tile in row:
        if tile == "S":
            height_row.append(letter_height("a"))
            start_pos = Position(x, y)
        elif tile == "E":
            height_row.append(letter_height("z"))
            end_pos = Position(x, y)
        else:
            height_row.append(letter_height(tile))
        visited_row.append(False)
        x += 1
    height_map.append(height_row)
    visited_map.append(visited_row)
    y += 1

reached_end = False
pos_queue.put(start_pos)
visited_map[start_pos.y][start_pos.x] = True
while len(pos_queue.queue) > 0:
    pos = pos_queue.get()
    if pos == end_pos:
        reached_end = True
        break
    queue_neighbors(pos)
    nodes_left_in_layer -= 1
    if nodes_left_in_layer == 0:
        nodes_left_in_layer = nodes_in_next_layer
        nodes_in_next_layer = 0
        move_count += 1
if reached_end:
    print(move_count)

# Problem B
height_map: list[list[int]] = []
visited_map: list[list[int]] = []
path_lengths: list[int] = []
y = 0
for row in data:
    height_row = []
    visited_row = []
    x = 0
    for tile in row:
        if tile == "S":
            height_row.append(letter_height("a"))
            start_pos = Position(x, y)
        elif tile == "E":
            height_row.append(letter_height("z"))
            end_pos = Position(x, y)
        else:
            height_row.append(letter_height(tile))
        visited_row.append(False)
        x += 1
    height_map.append(height_row)
    visited_map.append(visited_row)
    y += 1

for i in range(max_width):
    for j in range(max_height):
        move_count = 0
        nodes_left_in_layer = 1
        nodes_in_next_layer = 0
        pos_queue = queue.Queue()
        if height_map[j][i] == 0:
            reached_end = False
            pos_queue.put(Position(i, j))
            visited_map[j][i] = True
            while len(pos_queue.queue) > 0:
                pos = pos_queue.get()
                if pos == end_pos:
                    reached_end = True
                    break
                queue_neighbors(pos)
                nodes_left_in_layer -= 1
                if nodes_left_in_layer == 0:
                    nodes_left_in_layer = nodes_in_next_layer
                    nodes_in_next_layer = 0
                    move_count += 1
            if reached_end:
                path_lengths.append(move_count)
            reset_visited_map()
print(min(path_lengths))

