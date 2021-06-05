#!/usr/bin/env python
import os
from pathlib import Path

path = os.getcwd()
print("The current working directory is %s" % path)

input_path = path

print(input_path)

question_path = input(
    "\n👋 Do you want to create folders (press 1) or files (press 2)?: "
)

try:
    val = int(question_path)
except Exception:
    print("Woooo, invalid input ❌")

if question_path == str(1):
    try:
        folders_names = input(
            "\n📂 Specify the name of the folders (space for separation): "
        )
        folders_to_create = folders_names.split()

        parent_dir = input_path

        for folder in folders_to_create:
            print(folder)
            os.mkdir(os.path.join(parent_dir, str(folder)))
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s " % path)
else:
    files_names = input("\n📃 Specify the name of the file: ")
    # files_to_create = files_names.split()

    file_name = f"{files_names}.txt"
    f = open(file_name, "a+")  # open file in append mode
    f.write("export {};")
    f.close()
