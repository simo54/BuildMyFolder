#!/usr/bin/env python
import os

from file_ext import declare_extensions
from pathlib import Path

path = os.getcwd()

print("The current working directory is %s" % path)

question_path = input(
    "\nš Do you want to create folders (press 1) or files (press 2)?: "
)

try:
    val = int(question_path)
except Exception:
    print("Woooo, invalid input ā")

if question_path == str(1):
    try:
        folders_names = input(
            "\nš Specify the name of the folder(s) (space for separation): "
        )
        folders_to_create = folders_names.split()

        for folder in folders_to_create:
            os.mkdir(os.path.join(path, str(folder)))
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s " % path)
else:
    try:
        files_names = input(
            "\nš Specify the name of the file(s) (space for separation): ")
        file_extension = input(
            "\nš Declare files extension(s) (space for separation): ")

        declare_extensions(files_names, file_extension)
    except os.error:
        print("ā Error")
    else:
        print("ā File created")
