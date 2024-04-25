#! python3
# Program that fill gaps in numbering in filenames: if a folder contains files named
# such as x_01, x_009, x_101, it will rename those files to be x_1, x_2 and x_3. For a
# chosen folder, it will rename every file for every possible extension.
# Usage: python filling_gaps.py <source_folder_path> where <source_folder_path> is the
# folder for which the program will search for files to rename. And it is mandatory.
# Exits if less than 2 arguments are passed.

import os
import re
import sys
import shutil

def find_and_fix_gaps(folder_path, extension):
    # Create a set to store unique prefixes
    prefixes = set()

    # Iterate over all files in the folder
    for file_name in os.listdir(folder_path):
        # Extract the prefix using regex
        match = re.match(r"^(.+?)\d+\." + '|'.join(extension) + "$", file_name)
        if match:
            prefixes.add(match.group(1))

    # Iterate over unique prefixes
    for prefix in prefixes:
        # Compile regex pattern for the current prefix
        pattern = re.compile(rf"{prefix}(\d+)\.({'|'.join(extension)})")

        # Find all files in the folder that match the pattern
        files = [file for file in os.listdir(folder_path) if pattern.match(file)]

        # Sort the files based on their numbering
        files.sort(key=lambda x: int(pattern.match(x).group(1)))

        # Find any gaps in the numbering and rename files to close the gap
        target_number = 1
        for file in files:
            current_number = int(pattern.match(file).group(1))
            if current_number != target_number:
                new_name = f"{prefix}{target_number}.{file.split('.')[-1]}"
                print(f"Renaming {file} to {new_name}")
                shutil.move(os.path.join(folder_path, file), os.path.join(folder_path, new_name))
            target_number += 1

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python filling_gaps.py <source_folder_path>")
        sys.exit(1)

    source_folder = sys.argv[1]

    # Collect all unique file extensions in the source folder
    extensions = set()
    for filename in os.listdir(source_folder):
        if os.path.isfile(os.path.join(source_folder, filename)):
            file_extension = filename.split('.')[-1]
            extensions.add(file_extension)
    
    extensions = list(extensions)

    for item in extensions:
        find_and_fix_gaps(source_folder, item)