#!/usr/bin/env python
import os
from pathlib import Path

input_path = input("\n👋 Howdy? Enter the path desired: ")

question_path = input("\n👋 Do you want to create folders (press 1) or files (press 2)?: ")

try:
    val = int(question_path)
except Exception:
    print("Woooo, invalid input ❌")

if question_path == 1:
    print("folder")
else:
    print("files")
