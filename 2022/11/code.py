# Import advent-of-code utils
import sys
sys.path.append('./common')
import utils
import pathlib
import math

# Define paths of commonly used files.
path = pathlib.Path(__file__).parent.resolve()
input_path = f"{path}\input.txt"
sample_path = f"{path}\sample.txt"

def lcm(lst):
    lcm_temp = max(lst)
    while(True):
        if all(lcm_temp % x == 0 for x in lst):
            break
        lcm_temp = lcm_temp + 1
    return lcm_temp

class Monkey:
    def __init__(self, items: list[int], operator: str, operand: int, divisible: int, true_throw: int, false_throw: int):
        self.items: list[int] = items
        self.operator: str = operator
        self.operand: int = operand
        self.divisible: int = divisible
        self.true_throw: int = true_throw
        self.false_throw: int = false_throw
        self.inspection_count = 0        

    def inspect_item(self, item: int, worry_divided: bool = True, lcm: int = 0) -> int:
        worry_level: int = item 
        match self.operator:
            case "*":
                if self.operand == "old":
                    worry_level = worry_level * worry_level
                else:
                    worry_level = worry_level * int(self.operand)
            case "+":
                if self.operand == "old":
                    worry_level = worry_level + worry_level
                else:
                    worry_level = worry_level + int(self.operand)
        if worry_divided:
            worry_level = math.floor(worry_level / 3)

        if worry_level % self.divisible == 0:
            if worry_level >= lcm and lcm > 0:
                # When the worry_level gets bigger  than all of the monkey's divisors lowest common multiple then trim off the excess so the ints don't get too big.
                worry_level = worry_level % lcm
            monkeys[self.true_throw].items.append(worry_level)           
        else:
            if worry_level >= lcm and lcm > 0:
                # When the worry_level gets bigger  than all of the monkey's divisors lowest common multiple then trim off the excess so the ints don't get too big.
                worry_level = worry_level % lcm
            monkeys[self.false_throw].items.append(worry_level)

        self.inspection_count += 1

    def inspect_all_items(self, worry_divided: bool = True, lcm: int = 0):
        for item in self.items:
            self.inspect_item(item, worry_divided, lcm)
        self.items = []

data: list[str] = utils.read_file_lines(input_path)

# Problem A
# Parse Monkeys
monkeys: list[Monkey] = []
totals: list[int] = []
for i in range(0, len(data), 7):
    items: list[int] = utils.string_list_to_int_list(data[i + 1].split(":")[1].strip().split(","))
    operator: str = "*" if data[i + 2].__contains__("*") else "+"
    operand: str = data[i + 2].split(operator)[1].strip()
    divisible: int = int(data[i + 3].split("by")[1].strip())
    true_throw: int = int(data[i + 4].split("monkey")[1].strip())
    false_throw: int = int(data[i + 5].split("monkey")[1].strip())
    monkeys.append(Monkey(items, operator, operand, divisible, true_throw, false_throw))

# 20 Rounds of inspection
for i in range(20):
    for monkey in monkeys:
        monkey.inspect_all_items()

# Calculate monkey business
for monkey in monkeys:
    totals.append(monkey.inspection_count)
sorted_totals = sorted(totals, reverse=True)
monkey_business = sorted_totals[0] * sorted_totals[1]
print(monkey_business)

# Problem B
monkeys: list[Monkey] = []
totals: list[int] = []
for i in range(0, len(data), 7):
    items: list[int] = utils.string_list_to_int_list(data[i + 1].split(":")[1].strip().split(","))
    operator: str = "*" if data[i + 2].__contains__("*") else "+"
    operand: str = data[i + 2].split(operator)[1].strip()
    divisible: int = int(data[i + 3].split("by")[1].strip())
    true_throw: int = int(data[i + 4].split("monkey")[1].strip())
    false_throw: int = int(data[i + 5].split("monkey")[1].strip())
    monkeys.append(Monkey(items, operator, operand, divisible, true_throw, false_throw))

divisors = []
for monkey in monkeys:
    divisors.append(monkey.divisible)
lowest_common_multiple = lcm(divisors)

# 20 Rounds of inspection
for i in range(10000):
    for monkey in monkeys:
        monkey.inspect_all_items(worry_divided=False, lcm=lowest_common_multiple)

# Calculate monkey business
for monkey in monkeys:
    totals.append(monkey.inspection_count)
sorted_totals = sorted(totals, reverse=True)
monkey_business = sorted_totals[0] * sorted_totals[1]
print(monkey_business)
