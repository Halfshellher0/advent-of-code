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

winning_rows = [
    [0, 1, 2, 3, 4],
    [5, 6, 7, 8, 9],
    [10, 11, 12, 13, 14],
    [15, 16, 17, 18, 19],
    [20, 21, 22, 23, 24],
    [0, 5, 10, 15, 20],
    [1, 6, 11, 16, 21],
    [2, 7, 12, 17, 22],
    [3, 8, 13, 18, 23],
    [4, 9, 14, 19, 24]
]

class Bingo_Table:
    def __init__(self, numbers: list):
        self.numbers = numbers
        self.marked = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        self.won = False

    def mark(self, num: int) -> bool:
        if self.won:
            return False
        for i in range(25):
            if not self.marked[i] and self.numbers[i] == num:
                self.marked[i] = True
                break
        return True

    def sum_unmarked(self) -> int:
        sum = 0
        for i in range(25):
            if not self.marked[i]:
                sum += self.numbers[i]
        return sum
    
    def check_row(self, row: list) -> bool:
        for i in row:
            if not self.marked[i]:
                return False
        return True
    
    def check_win(self) -> bool:
        for winning_row in winning_rows:
            if self.check_row(winning_row):
                self.won = True
                return True
        return False

    def reset(self) -> None:
        self.won = False
        self.marked = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        
def process_row(row) -> list:
    nums = row.split(' ')
    return [i for i in nums if i != '']


bingo_data = utils.read_file_lines(input_path)
numbers_to_call = utils.string_list_to_int_list(bingo_data[0].split(','))

# Make bingo tables
bingo_tables = []
for i in range(2, len(bingo_data) - 4, 6):
    numbers = []
    numbers += utils.string_list_to_int_list(process_row(bingo_data[i]))
    numbers +=  utils.string_list_to_int_list(process_row(bingo_data[i+1]))
    numbers +=  utils.string_list_to_int_list(process_row(bingo_data[i+2]))
    numbers += utils.string_list_to_int_list(process_row(bingo_data[i+3]))
    numbers +=  utils.string_list_to_int_list(process_row(bingo_data[i+4]))
    bingo_tables.append(Bingo_Table(numbers))

# Problem A
answer = 0
game_won = False
for num in numbers_to_call:
    if game_won:
        break
    for bingo_table in bingo_tables:
        bingo_table.mark(num)
        if bingo_table.check_win():
            answer = bingo_table.sum_unmarked() * num
            game_won = True
            break
print(answer)

# Reset bingo table state
for bingo_table in bingo_tables:
    bingo_table.reset()
    

# Problem B
won_boards = 0
last_board = False
for num in numbers_to_call:
    if last_board:
        break
    for bingo_table in bingo_tables:
        if bingo_table.mark(num):
            if bingo_table.check_win():
                won_boards += 1
                if won_boards == len(bingo_tables):
                    answer = bingo_table.sum_unmarked() * num
                    last_board = True
                    break
print(answer)




