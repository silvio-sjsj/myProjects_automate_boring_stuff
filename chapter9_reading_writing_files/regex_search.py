"""Regex Search
Write a program that opens all .txt files in a folder and searches for any
line that matches a user-supplied regular expression. The results should
be printed to the screen.
"""

import os
import re

def search_files(folder_path, regex):
    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            print(f"Searching in file: {file_path}")
            with open(file_path, "r") as file:
                # Read each line and search for the regex pattern
                for line_number, line in enumerate(file, 1):
                    if re.search(regex, line):
                        print(f"Match found in {filename} at line {line_number}: {line.strip()}")

def main():
    folder_path = input("Enter the folder path: ")
    regex_pattern = input("Enter the regular expression: ")
    search_files(folder_path, regex_pattern)

if __name__ == "__main__":
    main()