# Import advent-of-code utils
import sys
sys.path.append('./common')
import utils
import pathlib

# Define paths of commonly used files.
path = pathlib.Path(__file__).parent.resolve()
input_path = f"{path}\input.txt"
sample_path = f"{path}\sample.txt"

depths = utils.read_file_ints(sample_path)

# Problem A
# increased_count = 0
# prev_depth = 0
# for depth in depths:
#     if prev_depth > 0:
#         if depth > prev_depth:
#             increased_count += 1
#     prev_depth = depth
# print(increased_count)

# Problem B
# windows = []
# for i in range(len(depths) - 2):
#     windows.append(depths[i] + depths[i + 1] + depths[i + 2])
# prev_depth = 0
# increased_count = 0
# for depth in windows:
#     if prev_depth > 0:
#         if depth > prev_depth:
#             increased_count += 1
#     prev_depth = depth
# print(increased_count)