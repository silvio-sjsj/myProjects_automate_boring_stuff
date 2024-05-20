#!/home/silviojr/.virtualenvs/boring/bin/python3
# multi-clip.py - Saves and loads pieces of text to the clipboard.
# Usage: python3 multi-clip.py save <keyword> - Saves clipboard to keyword.
#        python3 multi-clip.py del <keyword> - Deletes keyword from storage.
#        python3 multi-clip.py <keyword> - Loads keyword to clipboard.
#        python3 multi-clip.py list - Loads all keywords to clipboard.

import shelve
import pyperclip
import sys
import pyinputplus as pyip

shelf_path = '/home/silviojr/Documents/mcb'
mcb_shelf = shelve.open(shelf_path)

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
    print(f"Saved clipboard content to keyword '{sys.argv[2]}'.")

# Delete a keyword.
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'del':
    if sys.argv[2] in mcb_shelf:
        user_input = pyip.inputYesNo(f"Do you want to delete the key '{sys.argv[2]}'? (yes/no): ")
        if user_input.lower() == 'yes':
            del mcb_shelf[sys.argv[2]]
            print(f"Deleted key '{sys.argv[2]}'.")
        else:
            print(f"Key '{sys.argv[2]}' not deleted.")
    else:
        print(f"Key '{sys.argv[2]}' not found.")

# List keywords or load content to clipboard.
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        keys_list = list(mcb_shelf.keys())
        print(keys_list)
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])
        print(f"Copied content for keyword '{sys.argv[1]}' to clipboard.")

mcb_shelf.close()