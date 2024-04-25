#! python3
# Usage: python add_pref_or_sufix.py <source_folder_path> \
# <pattern to match> <choice: prefix or sufix>"), where <source_folder_path> is the
# folder with subfolders for which the program will search for files to rename,
# <pattern to match> is the given pattern in filenames that the program will look
# for and <choice: prefix or sufix> is a choice to be made by the user: 'prefix' will
# add a given prefix to filenames and 'sufix' will add a sufix.
# Exits if not exactly four arguments were passed

import os
import re
import sys
import shutil

def add_prefix(directory, re_pattern, prefix):
    # Walk through the directory tree and process files in all subfolders
    for root, _, files in os.walk(directory):
        # The regular expression pattern to match filenames containing "re_pattern"
        pattern = re.compile(rf'.*{re_pattern}.*')
        
        # Filter filenames that match the pattern
        pattern_files = [filename for filename in files if pattern.match(filename)]
        
        # Rename the matched files with the specified prefix
        for filename in pattern_files:
            # Construct the new filename with the prefix
            new_filename = prefix + '_' + filename
            
            # Get the full path of the file
            filepath = os.path.join(root, filename)
            new_filepath = os.path.join(root, new_filename)
            
            # Rename the file
            shutil.move(filepath, new_filepath)
            
            print(f"File '{filename}' renamed to '{new_filename}' with prefix '{prefix}'.")

def add_sufix(directory, re_pattern, sufix):
    # Walk through the directory tree and process files in all subfolders
    for root, _, files in os.walk(directory):
        # The regular expression pattern to match filenames containing "re_pattern"
        pattern = re.compile(rf'.*{re_pattern}.*')
        
        # Filter filenames that match the pattern
        pattern_files = [filename for filename in files if pattern.match(filename)]
        
        # Rename the matched files with the specified prefix
        for filename in pattern_files:
            # Construct the new filename with the prefix
            new_filename = filename + '_' + sufix
            
            # Get the full path of the file
            filepath = os.path.join(root, filename)
            new_filepath = os.path.join(root, new_filename)
            
            # Rename the file
            shutil.move(filepath, new_filepath)
            
            print(f"File '{filename}' renamed to '{new_filename}' with sufix '{sufix}'.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python add_pref_or_sufix.py <source_folder_path> \
                                                  <pattern to match> \
                                                  <choice: prefix or sufix>")
        sys.exit(1)

    source_folder = sys.argv[1]
    regex_pattern = sys.argv[2]
    choice = sys.argv[3]

    if choice == 'prefix':
        prefix_to_add = input("Type the prefix to be added in all filenames: ")
        add_prefix(source_folder, regex_pattern, prefix_to_add)
    
    if choice == 'sufix':
        sufix_to_add = input("Type the sufix to be added in all filenames: ")
        add_sufix(source_folder, regex_pattern, sufix_to_add)