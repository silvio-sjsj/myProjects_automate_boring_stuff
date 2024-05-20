#!/home/silviojr/.virtualenvs/boring/bin/python3
# open_pages.py - Open a list of internet pages in new tabes in the default browser.
# Usage: python3 open_pages.py page1, page2, ..., pageN
# Open pages 1, 2 to N if N pages are given as argument in the command line, otherwise
# open a list of pages from a keyword 'web-pages' saved in a mcb file.

import shelve
import webbrowser
import sys

shelf_path = '/home/silviojr/Documents/mcb'
mcb_shelf = shelve.open(shelf_path)

if len(sys.argv) > 1:
    # Exclude the script name from the command-line arguments
    pages = sys.argv[1:]
else:
    pages = mcb_shelf['web-pages'].split(', ')
    #pyperclip.copy(pages)

for page in pages:
    webbrowser.open_new_tab('https://' + page + '.com')