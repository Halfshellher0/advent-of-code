# Import advent-of-code utils
import sys
sys.path.append('./common')
import utils
import pathlib

# Define paths of commonly used files.
path = pathlib.Path(__file__).parent.resolve()
input_path = f"{path}\input.txt"
sample_path = f"{path}\sample.txt"


# Problem 1
max_red = 12
max_green = 13
max_blue = 14
sum = 0
data = utils.read_file_lines(input_path)
for line in data:
    game_possible = True
    split = line.split(":")
    game = int(split[0].split(" ")[1])
    subsets = split[1].split(";")
    for subset in subsets:
        cubes = subset.split(",")
        for cube in cubes:
            cube = cube.strip()
            split = cube.split(" ")
            num_cubes = int(split[0])
            color_cube = split[1]
            match color_cube:
                case "red":
                    if num_cubes > max_red:
                        game_possible = False
                        break
                case "green":
                    if num_cubes > max_green:
                        game_possible = False
                        break
                case "blue":
                    if num_cubes > max_blue:
                        game_possible = False
                        break
    if game_possible:
        sum += game
print(sum)


# Problem 2
sum = 0
data = utils.read_file_lines(input_path)
for line in data:
    max_red = 0
    max_green = 0
    max_blue = 0
    split = line.split(":")
    game = int(split[0].split(" ")[1])
    subsets = split[1].split(";")
    for subset in subsets:
        cubes = subset.split(",")
        for cube in cubes:
            cube = cube.strip()
            split = cube.split(" ")
            num_cubes = int(split[0])
            color_cube = split[1]
            match color_cube:
                case "red":
                    if num_cubes > max_red:
                        max_red = num_cubes
                case "green":
                    if num_cubes > max_green:
                        max_green = num_cubes
                case "blue":
                    if num_cubes > max_blue:
                        max_blue = num_cubes
    cube_power = max_red * max_green * max_blue
    sum += cube_power
print(sum)
