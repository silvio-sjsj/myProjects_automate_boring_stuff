import shelve
import webbrowser
import sys

shelf_path = '/home/silviojr/mcb'

mcbShelf = shelve.open(shelf_path)

if len(sys.argv) > 1:
    # Exclude the script name from the command-line arguments
    pages = sys.argv[1:]
else:
    pages = mcbShelf['web-pages'].split(', ')
    #pyperclip.copy(pages)

for page in pages:
    webbrowser.open_new_tab('https://' + page + '.com')