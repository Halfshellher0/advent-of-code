# Import advent-of-code utils
import sys
sys.path.append('./common')
import utils
import pathlib

# Define paths of commonly used files.
path = pathlib.Path(__file__).parent.resolve()
input_path = f"{path}\input.txt"
sample_path = f"{path}\sample.txt"
sample_path2 = f"{path}\sample2.txt"

# Problem 1
data = utils.read_file_lines(input_path)
sum = 0
for line in data:
    numbers = 0
    number = 0
    firstDigit = -1
    lastDigit = -1
    for char in line:
        if str(char).isdigit():
            numbers += 1
            if numbers == 1:
                firstDigit = int(char)
                number += int(char) * 10
            elif numbers > 1:
                lastDigit = int(char)
    if lastDigit == -1:
        lastDigit = firstDigit
    number += lastDigit
    sum += number
print(sum)

# Problem 2
data = utils.read_file_lines(input_path)
sum = 0
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for line in data:
    num = 0
    minValue = -1
    minIndex = 999999999
    maxValue = -1
    maxIndex = -1
    finalNumber = -1

    for number in numbers:
        leftNumber = line.find(numbers[num])
        leftWord = line.find(words[num])
        if leftNumber == -1:
            leftNumber = 999999999
        if leftWord == -1:
            leftWord = 999999999
        leftPos = min(leftNumber, leftWord)
        if leftPos < minIndex:
            minValue = num
            minIndex = leftPos

        rightNumber = line.rfind(numbers[num])
        rightWord = line.rfind(words[num])
        rightPos = max(rightNumber, rightWord)
        if rightPos > maxIndex:
            maxValue = num
            maxIndex = rightPos
        num += 1
    
    if maxValue == -1:
        maxValue = minValue
    finalNumber = 10 * minValue + maxValue
    sum += finalNumber
print(sum)