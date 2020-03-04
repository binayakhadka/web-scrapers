import os

dir_name = os.getcwd()
directory = os.listdir(dir_name)

for item in directory:
    if item.endswith(".png"):
        os.remove(os.path.join(dir_name, item))