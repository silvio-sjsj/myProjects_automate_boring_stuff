#! python3
# Usage: python selective_copy.py <source_folder_path> \
# <target_folder> <choices: extensions>"), where <source_folder_path> is the
# folder for which the program will search for files to copy,
# <target_folder> is the folder for which the program will copy the files for, and
# <choice: extensions> are the extensions given by the user of the files that will
# be copied. At least one choice has to be made.
# Exits if less than 4 arguments are passed.

import os
import re
import sys
import shutil

def find_and_copy_files(source_folder, target_folder, choices):
    # Create the target folder if it doesn't exist
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    for choice in choices:
        
        # Regular expression pattern to match file extension
        pattern = re.compile(r'\.' + re.escape(choice) + '$', re.IGNORECASE)

        # Walk through the source folder and copy files with the specified extension
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                if pattern.search(file):
                    source_path = os.path.join(root, file)
                    target_path = os.path.join(target_folder, file)
                    shutil.copy(source_path, target_path)
                    print(f"Copied '{file}' to '{target_folder}'")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python selective_copy.py <source_folder_path> \
                                               <target_folder> \
                                               <choices: extensions>")
        sys.exit(1)

    source_folder = sys.argv[1]
    target_folder = sys.argv[2]
    choices = sys.argv[3:]

    find_and_copy_files(source_folder, target_folder, choices)