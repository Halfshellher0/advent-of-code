# Import advent-of-code utils
import sys
sys.path.append('./common')
import utils
import pathlib

# Define paths of commonly used files.
path = pathlib.Path(__file__).parent.resolve()
input_path = f"{path}\input.txt"
sample_path = f"{path}\sample.txt"

trees = []

def is_visible(x: int, y: int) -> bool:
    if x == 0 or x == (len(trees) - 1) or y == 0 or y == (len(trees[0]) - 1):
        # On a boundary
        return True
    
    tree_height = trees[x][y]

    # Check North
    north_visible = True
    for j in range(y-1,-1,-1):
        if trees[x][j] >= tree_height:
            north_visible = False
    
    # Check South
    south_visible = True
    for j in range(y+1,len(trees[0])):
        if trees[x][j] >= tree_height:
            south_visible = False

    # Check West
    west_visible = True
    for i in range(x-1,-1,-1):
        if trees[i][y] >= tree_height:
            west_visible = False

    # Check East
    east_visible = True
    for i in range(x+1,len(trees)):
        if trees[i][y] >= tree_height:
            east_visible = False

    if not north_visible and not south_visible and not west_visible and not east_visible:
        return False
    return True

def scenic_score(x: int, y: int):
    if x == 0 or x == (len(trees) - 1) or y == 0 or y == (len(trees[0]) - 1):
        # On a boundary
        return 0

    tree_height = trees[y][x]

    if x == 2 and y == 3:
        pass

    # Check North
    north_trees = 0
    for j in range(y-1,-1,-1):
        if trees[j][x] < tree_height:
            north_trees += 1
        else:
            north_trees += 1
            break
    
    # Check South
    south_trees = 0
    for j in range(y+1,len(trees[0])):
        if trees[j][x] < tree_height:
            south_trees += 1
        else:
            south_trees += 1
            break
            

    # Check West
    west_trees = 0
    for i in range(x-1,-1,-1):
        if trees[y][i] < tree_height:            
            west_trees += 1
        else:
            west_trees += 1
            break 

    # Check East
    east_trees = 0
    for i in range(x+1,len(trees)):
        if trees[y][i] < tree_height:
            east_trees += 1 
        else:
            east_trees += 1
            break
            
    scenic_score = max(north_trees,1) * max(south_trees,1) * max(west_trees,1) * max(east_trees,1)
    if scenic_score == 3:
        pass
    return scenic_score


# Load tree height data
data = utils.read_file_lines(input_path)
for row in data:
    tree_row = []
    for i in range(len(row)):
        tree_row.append(int(row[i]))
    trees.append(tree_row)

# Problem A
visible_count = 0
for y in range(len(trees[0])):
    for x in range(len(trees)):
        if is_visible(x,y):
            visible_count += 1
print(visible_count)

# Problem B
scenic_scores = []
for y in range(len(trees[0])):
    for x in range(len(trees)):
        scenic_scores.append(scenic_score(x,y))
print(max(scenic_scores))

