import os
import pathlib
import shutil

year = input("Enter year:")
day = input("Enter day:")
template_path = pathlib.Path(__file__).parent.resolve() / "code_template.py"
path = pathlib.Path(__file__).parent.parent.resolve()

path = path / year / day
if not os.path.exists(path):
    os.mkdir(path)

shutil.copyfile(template_path, path / "code.py")
with open(path / "input.txt", 'w') as new_file: 
   pass
with open(path / "sample.txt", 'w') as new_file: 
   pass 