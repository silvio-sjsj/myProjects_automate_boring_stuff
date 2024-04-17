"""
Create a Mad Libs program that reads in text files and lets the user add
their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB
appears in the text file.
"""

import re

def mad_libs(filename):
    # Read the content of the file
    with open(filename, 'r') as file:
        text = file.read()

    # Find all occurrences of ADJECTIVE, NOUN, ADVERB, and VERB
    placeholders = re.findall(r'ADJECTIVE|NOUN|ADVERB|VERB', text)

    # Replace each placeholder with user input
    for placeholder in placeholders:
        replacement = input(f"Enter {placeholder.lower()}: ")
        text = re.sub(placeholder, replacement, text, count=1)

    # Print the result
    print(text)

    # Save the result to a new file
    with open('mad_libs_result.txt', 'w') as file:
        file.write(text)

# Example usage
if __name__ == "__main__":
    filename = input("Enter the filename of the Mad Libs text file: ")
    mad_libs(filename)