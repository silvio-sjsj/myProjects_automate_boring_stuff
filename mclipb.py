#! /home/.../.virtualenvs/boring/bin/python3
# extended_mclip.pyw - An extension of the multi-clipboard program.
# Usage: py.exe multi-clipboard.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe multi-clipboard.pyw <keyword> - Loads keyword to clipboard.
#        py.exe multi-clipboard.pyw list - Loads all keywords to clipboard.
#        py.exe multi-clipboard.pyw del <keyword> - delete keyword

import shelve
import pyperclip
import sys

shelf_path = "/home/.../mcb"

mcbShelf = shelve.open(shelf_path)

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()

elif len(sys.argv) == 3 and sys.argv[1].lower() == 'del':
    if sys.argv[2] in mcbShelf:
        del mcbShelf[sys.argv[2]]
        print(f"Deleted key '{sys.argv[2]}'")
    else:
        print(f"Key '{sys.argv[2]}' not found")

elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        keys = list(mcbShelf.keys())
        print(keys)
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()

"""
Examples:

python3 multi-clipboard.pyw save 'example': it will copy what's in the clipboard to a
'example' keyword

python3 multi-clipboard.pyw del 'example': it will delete the key 'example'

python3 multi-clipboard.pyw list: it will list every keyword to clipboard.
Just ctrl+V to paste them.

python3 multi-clipboard.pyw 'example': it will copy the content under 'example' to clipboard
"""
