import os

# Directory path where folders will be created
dir_path = "F:/AWS/program/"



# Create directories named 1 to 9
for name in range(1, 10):
    os.mkdir(os.path.join(dir_path, str(name)))
