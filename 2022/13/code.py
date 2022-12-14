# Import advent-of-code utils
import sys
sys.path.append('./common')
import utils
import pathlib
import json

# Define paths of commonly used files.
path = pathlib.Path(__file__).parent.resolve()
input_path = f"{path}\input.txt"
sample_path = f"{path}\sample.txt"



# returns true if in the right order
def compare(left, right) -> int:
    if type(left) == int and type(right) == int:
        if left < right:
            return 1
        elif left > right:
            return 0
        return -1
    elif type(left) == list and type(right) == int:
        new_right = [right]
        check = compare(left, new_right)
        if check > -1:
            return check
    elif type(left) == int and type(right) == list:
        new_left = [left]
        check = compare(new_left, right)
        if check > -1:
            return check
    else:
        # Both are lists
        min_count = min(len(left), len(right))
        for i in range(min_count):
            check = compare(left[i], right[i])
            if check > -1:
                return check
        if len(left) < len(right):
            return 1
        elif len(left) > len(right):
            return 0
        return -1
    return -1

data = utils.read_file_lines(input_path)

# Problem A
index = 0
sum_index = 0
for i in range(0, len(data), 3):
    index += 1
    line1 = "{ \"obj\":" + data[i] + "}"
    line2 = "{ \"obj\":" + data[i + 1] + "}"
    left = json.loads(line1)['obj']
    right = json.loads(line2)['obj']
    if compare(left, right):
        sum_index += index
print(sum_index)

# Problem B
unsorted_packets = []
sorted_packets = []
line1 = "{ \"obj\": [[2]] }"
line2 = "{ \"obj\": [[6]] }"
json1 = json.loads(line1)['obj']
json2 = json.loads(line2)['obj']
unsorted_packets.append(json1)
unsorted_packets.append(json2)
for i in range(0, len(data), 3):
    index += 1
    line1 = "{ \"obj\":" + data[i] + "}"
    line2 = "{ \"obj\":" + data[i + 1] + "}"
    unsorted_packets.append(json.loads(line1)['obj'])
    unsorted_packets.append(json.loads(line2)['obj'])

length = len(unsorted_packets)

while len(sorted_packets) < length:
    leftmost_packet = unsorted_packets[len(unsorted_packets) - 1]
    if len(unsorted_packets) > 1:
        for packet in unsorted_packets:
            if packet != leftmost_packet and not compare(leftmost_packet, packet):
                leftmost_packet = packet
    unsorted_packets.remove(leftmost_packet)
    sorted_packets.append(leftmost_packet)

i1 = 0
i2 = 0
i = 0
for packet in sorted_packets:
    i += 1
    if packet == json1:
        i1 = i
    elif packet == json2:
        i2 = i
print(i1 * i2)




