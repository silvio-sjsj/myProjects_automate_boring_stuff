#! python3
#! python3
# add_prefix2.py - Add a given prefix to the start of a filename if it contains
# a given pattern.
# Usage: python add_prefix.py <source_folder_path> <pattern to match>
# <prefix to add>, where <source_folder_path> is the folder with subfolder for
# for which the program will search for files, <pattern to match> is the given
# pattern in filenames and <prefix to add> is the prefix to be added to the
# filename.
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

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python add_prefix2.py <source_folder_path> <pattern to match>  \
                                            <prefix to add>")
        sys.exit(1)

    source_folder = sys.argv[1]
    regex_pattern = sys.argv[2]
    prefix_to_add = sys.argv[3]

    add_prefix(source_folder, regex_pattern, prefix_to_add)