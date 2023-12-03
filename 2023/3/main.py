# Import advent-of-code utils
from dataclasses import dataclass
import sys
sys.path.append('./common')
import utils
import pathlib

# Define paths of commonly used files.
path = pathlib.Path(__file__).parent.resolve()
input_path = f"{path}\input.txt"
sample_path = f"{path}\sample.txt"

symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "/"]
directions = ["NW", "N", "NE", "E", "SE", "S", "SW", "W"]

@dataclass
class GearPosition:
    col: int
    row: int
    firstNumber: int = 0
    secondNumber: int = 0

    def gearRatio(self) -> int:
        return self.firstNumber * self.secondNumber

    def hasFirstNumber(self) -> bool:
        return self.firstNumber > 0



def isSymbol(char: str):
    if char in symbols:
        return True
    return False

def isGearSymbol(char: str):
    if char == "*":
        return True
    return False

def isPeriod(char: str):
    if char == ".":
        return True
    return False

def isNumber(char: str):
    if not isSymbol(char) and not isPeriod(char):
        return True
    return False



# Construct Grid
data = utils.read_file_lines(input_path)
width = 0
height = 0
rows = []
values = []
for line in data:
    values = []
    for char in line:
        values.append(char)
    width = len(values)
    rows.append(values)
height = len(rows)

part_numbers = []
not_part_numbers = []
gear_positions: list[GearPosition] = []

def tileIsSymbol(col, row):
    # Check boundaries
    if col < 0 or col >= width:
        return False
    if row < 0 or row >= height:
        return False

    # Check if tile is symbol
    if isSymbol(rows[row][col]):
        return True
    return False

def tileIsGearSymbol(col, row):
    # Check boundaries
    if col < 0 or col >= width:
        return False
    if row < 0 or row >= height:
        return False

    # Check if tile is symbol
    if isGearSymbol(rows[row][col]):
        return True
    return False

def adjacentIsSymbol(col: int, row: int, direction: str):
    match direction:
        case "NW":
            row = row - 1
            col = col - 1
        case "N":
            row = row - 1
        case "NE":
            row = row - 1
            col = col + 1
        case "E":
            col = col + 1
        case "SE":
            row = row + 1
            col = col + 1
        case "S":
            row = row + 1
        case "SW":
            row = row + 1
            col = col - 1
        case "W":
            col = col - 1

    return tileIsSymbol(col, row)

def adjacentIsGearSymbol(col: int, row: int, direction: str):
    match direction:
        case "NW":
            row = row - 1
            col = col - 1
        case "N":
            row = row - 1
        case "NE":
            row = row - 1
            col = col + 1
        case "E":
            col = col + 1
        case "SE":
            row = row + 1
            col = col + 1
        case "S":
            row = row + 1
        case "SW":
            row = row + 1
            col = col - 1
        case "W":
            col = col - 1

    return [tileIsGearSymbol(col, row), col, row]

def adjacentSymbol(col, row):
    for direction in directions:
        if adjacentIsSymbol(col, row, direction):
            return True
    return False

def adjacentGearSymbol(col, row):
    for direction in directions:
        [a,b,c] = adjacentIsGearSymbol(col, row, direction)
        if a:
            return [a, b, c]
    return [False, 0, 0]

def determineNumber(row, numberStart, numberEnd, numberString):
    isPartNumber = False
    number = int(numberString)

    for col in range(numberStart, numberEnd + 1):
        if adjacentSymbol(col, row):
            isPartNumber = True
            break

    if isPartNumber:
        part_numbers.append(number)
    else:
        not_part_numbers.append(number)

def findGear(col, row) -> GearPosition:
    for gear in gear_positions:
        if gear.col == col and gear.row == row:
            return gear

def determineNumberGears(row, numberStart, numberEnd, numberString):
    number = int(numberString)

    for col in range(numberStart, numberEnd + 1):
        [a, gearCol, gearRow] = adjacentGearSymbol(col, row)
        if a:
            gear = findGear(gearCol, gearRow)
            if not gear.hasFirstNumber():
                gear.firstNumber = number
            else:
                gear.secondNumber = number
            break





# # Problem 1
# row = 0
# sum = 0
# part_numbers = []
# not_part_numbers = []
# for line in rows:
#     col = 0
#     numberFound = False
#     numberStart = -1
#     numberEnd = -1
#     numberString = ""
#     for char in line:
#         if not numberFound:
#             if isNumber(char):
#                 numberFound = True
#                 numberStart = col
#                 numberString += char
#         else:
#             if not isNumber(char):
#                 numberFound = False
#                 numberEnd = col - 1
#                 determineNumber(row, numberStart, numberEnd, numberString)
#                 numberStart = -1
#                 numberEnd = -1
#                 numberString = ""
#             else:
#                 numberString += char
#                 if col == (width - 1):
#                     determineNumber(row, numberStart, width - 1, numberString)
#         col += 1
#     row += 1
    

# for number in part_numbers:
#     sum += number
# print(sum)

# Problem 2
#Record Gear positions
row = 0
gear_positions: list[GearPosition] = []
for line in rows:
    col = 0
    for char in line:
        if isGearSymbol(char):
            gear_positions.append(GearPosition(col, row))
        col += 1
    row += 1


row = 0
sum = 0
part_numbers = []
not_part_numbers = []

for line in rows:
    col = 0
    numberFound = False
    numberStart = -1
    numberEnd = -1
    numberString = ""
    for char in line:
        if not numberFound:
            if isNumber(char):
                numberFound = True
                numberStart = col
                numberString += char
        else:
            if not isNumber(char):
                numberFound = False
                numberEnd = col - 1
                determineNumberGears(row, numberStart, numberEnd, numberString)
                numberStart = -1
                numberEnd = -1
                numberString = ""
            else:
                numberString += char
                if col == (width - 1):
                    determineNumberGears(row, numberStart, width - 1, numberString)
        col += 1
    row += 1
    

for gear in gear_positions:
    sum += gear.gearRatio()
print(sum)