#!/usr/bin/env python
import os
from pathlib import Path

path = os.getcwd()
print("The current working directory is %s" % path)

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
        parent_dir = path

        for folder in folders_to_create:
            print(folder)
            os.mkdir(os.path.join(path, str(folder)))
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s " % path)
else:
    try:
        files_names = input("\n📃 Specify the name of the file: ")
        # files_to_create = files_names.split()

        file_name_py = f"{files_names}.py"
        file_name_sb_tsx = f"{files_names}.stories.tsx"
        file_name_sb_js = f"{files_names}.stories.js"
        file_name_sb_js = f"{files_names}.stories.ts"
        file_name_js = f"{files_names}.js"
        file_name_ts = f"{files_names}.ts"
        file_name_test_ts = f"{files_names}.test.ts"
        file_name_test_js = f"{files_names}.test.js"
        file_name_test_jsx = f"{files_names}.test.jsx"
        file_name_test_tsx = f"{files_names}.test.tsx"
        file_name_html = f"{files_names}.html"
        file_name_css = f"{files_names}.css"
        file_name_sass = f"{files_names}.sass"
        file_name_less = f"{files_names}.less"
        file_name_cpp = f"{files_names}.c++"
        file_name_java = f"{files_names}.java"
        file_name_json = f"{files_names}.json"

        f = open(file_name_py, "a+")
        f.write("export {};")
        f.close()

    except os.error:
        print("❌ Error")
    else:
        print("✅ File created")
