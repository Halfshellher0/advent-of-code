# Import advent-of-code utils
import sys
sys.path.append('./common')
import utils
import pathlib

# Define paths of commonly used files.
path = pathlib.Path(__file__).parent.resolve()
input_path = f"{path}\input.txt"
sample_path = f"{path}\sample.txt"

dirs = []

class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

class Dir:
    def __init__(self, name: str, parent):
        self.name = name        
        self.parent = parent
        self.dirs = []
        self.files = []

    def sub_dir(self, name: str):
        for dir in self.dirs:
            if dir.name == name:
                return dir

    def add_sub_dir(self, name: str):
        self.dirs.append(Dir(name, self))
    
    def add_file(self, name: str, size: int):
        self.files.append(File(name, size))

    def size(self):
        size = 0
        for file in self.files:
            size += file.size
        for dir in self.dirs:
            size += dir.size()
        return size

def construct_tree(data: str, root: Dir):
    current_dir = None    
    i = 0
    while i < len(data):
        line = data[i]
        if line[:4] == "$ cd":
            dir_name = line[5:]
            if dir_name == "/":
                current_dir = root
            elif dir_name == "..":
                current_dir = current_dir.parent
            else:
                current_dir = current_dir.sub_dir(dir_name)
        elif line[:4] == "$ ls":
            i += 1            
            while i < len(data) and data[i][0] != "$":
                ls_result = data[i].split(" ")
                if ls_result[0] == "dir":
                    current_dir.add_sub_dir(ls_result[1])
                else:
                    current_dir.add_file(ls_result[1], int(ls_result[0]))
                i += 1
            i -= 1
        i += 1

def tree_to_list(root: Dir) -> None:
    dirs.append(root)
    for dir in root.dirs:
        tree_to_list(dir)

def find_lt_100k() -> int:
    total = 0
    for dir in dirs:
        if dir.size() < 100000:
            total += dir.size()
    return total

data = utils.read_file_lines(sample_path)
root_Dir = Dir("/", None) 
construct_tree(data, root_Dir)
tree_to_list(root_Dir)

# Problem A
print(find_lt_100k())

# Problem B
used_space = root_Dir.size()
free_space = 70000000 - used_space
threshold = 30000000 - free_space
above_threshold_dirs = []
for dir in dirs:
    dir_size = dir.size()
    if dir_size >= threshold:
        above_threshold_dirs.append(dir_size)
print(min(above_threshold_dirs))