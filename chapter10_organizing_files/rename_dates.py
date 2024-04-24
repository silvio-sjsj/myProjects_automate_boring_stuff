#! python3
# rename_dates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY.

import shutil
import os
import re
from pathlib import Path

american_file_dir = Path() / "automate_boring_stuff/" / "chapter10_organizing_files" / "american_dates"
european_file_dir = Path() / "automate_boring_stuff/" / "chapter10_organizing_files" / "european_dates"

# Create a regex that matches files with the American date format.
date_pattern = re.compile(r"""^(.*?) # all text before the date
    ((0|1)?\d)-     # one or two digits for the month
    ((0|1|2|3)?\d)- # one or two digits for the day
    ((19|20)\d\d)   # four digits for the year (must start with 19 or 20)
    (.*?)$          # all text after the date
    """, re.VERBOSE)

# Loop over the files in the working directory.
for amer_filename in os.listdir(american_file_dir):
    mo = date_pattern.search(amer_filename)

    # Skip files without a date.
    if mo == None:
        continue

    # Get the different parts of the filename.
    before_part = mo.group(1)
    month_part  = mo.group(2)
    day_part    = mo.group(4)
    year_part   = mo.group(6)
    after_part  = mo.group(8)

    # Form the European-style filename.
    euro_filename = before_part + day_part + '-' + month_part + '-' + year_part + after_part

    amer_filename = os.path.join(american_file_dir, amer_filename)
    euro_filename = os.path.join(european_file_dir, euro_filename)

    # Rename the files.
    print('Renaming "%s" to "%s"...' % (amer_filename, euro_filename))
    shutil.copy(amer_filename, euro_filename) # uncomment after testing