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

# Initialize
movements: list[str] = utils.read_file_lines(input_path)
Position = namedtuple('Position',['x','y'])
head_position = Position(0, 0)
tail_position = Position(0, 0)
tail_visited_positions = []

#Problem B
knot_positions = [Position(0, 0), Position(0, 0), Position(0, 0), Position(0, 0), Position(0, 0), Position(0, 0), Position(0, 0), Position(0, 0), Position(0, 0), Position(0, 0)]
nine_visited_positions = []

def record_tail_position() -> None:
    for visited_position in tail_visited_positions:
        if tail_position == visited_position:
            return None
    tail_visited_positions.append(tail_position)

def record_nine_position() -> None:
    for visited_position in nine_visited_positions:
        if knot_positions[9] == visited_position:
            return None
    nine_visited_positions.append(knot_positions[9])

def is_adjacent() -> bool:
    if abs(head_position.x - tail_position.x) > 1 or abs(head_position.y - tail_position.y) > 1:
        return False
    return True

def is_adjacent_2(pos1: Position, pos2: Position) -> bool:
    if abs(pos1.x - pos2.x) > 1 or abs(pos1.y - pos2.y) > 1:
        return False
    return True

def move_tail_pos() -> Position:
    x = head_position.x - tail_position.x
    y = head_position.y - tail_position.y
    x = -1 if x < -1 else x
    x = 1 if x > 1 else x
    y = -1 if y < -1 else y
    y = 1 if y > 1 else y
    return Position(tail_position.x + x, tail_position.y + y)

def move_tail_pos_2(pos1: Position, pos2: Position) -> Position:
    x = pos1.x - pos2.x
    y = pos1.y - pos2.y
    x = -1 if x < -1 else x
    x = 1 if x > 1 else x
    y = -1 if y < -1 else y
    y = 1 if y > 1 else y
    return Position(pos2.x + x, pos2.y + y)

def move_head(direction: str, magnitude: int) -> None:
    global head_position, tail_position
    match direction:
        case "U":
            for i in range(magnitude):
                head_position = Position(head_position.x, head_position.y + 1)
                move_tail()
        case "D":
            for i in range(magnitude):
                head_position = Position(head_position.x, head_position.y - 1)
                move_tail()
        case "L":
            for i in range(magnitude):
                head_position = Position(head_position.x - 1, head_position.y)
                move_tail()
        case "R":
            for i in range(magnitude):
                head_position = Position(head_position.x + 1, head_position.y)
                move_tail()

def move_head_2(direction: str, magnitude: int) -> None:
    global knot_positions
    match direction:
        case "U":
            for i in range(magnitude):
                knot_positions[0] = Position(knot_positions[0].x, knot_positions[0].y + 1)
                move_tail_long()
        case "D":
            for i in range(magnitude):
                knot_positions[0] = Position(knot_positions[0].x, knot_positions[0].y - 1)
                move_tail_long()
        case "L":
            for i in range(magnitude):
                knot_positions[0] = Position(knot_positions[0].x - 1, knot_positions[0].y)
                move_tail_long()
        case "R":
            for i in range(magnitude):
                knot_positions[0] = Position(knot_positions[0].x + 1, knot_positions[0].y)
                move_tail_long()

def move_tail() -> None:
    global tail_position
    if not is_adjacent():
        tail_position = move_tail_pos()
        record_tail_position()

def move_tail_long() -> None:
    global knot_positions
    for i in range(9):
        if not is_adjacent_2(knot_positions[i], knot_positions[i + 1]):
            knot_positions[i + 1] = move_tail_pos_2(knot_positions[i], knot_positions[i + 1])
    record_nine_position()


# Problem A
record_tail_position()
for movement in movements:
    instruction = movement.split(" ")
    move_head(instruction[0], int(instruction[1]))
print(len(tail_visited_positions))

#Problem B
record_nine_position()
for movement in movements:
    instruction = movement.split(" ")
    move_head_2(instruction[0], int(instruction[1]))
print(len(nine_visited_positions))

