"""Code containing solution to the practice project 'Date detection'"""
import pyperclip
import re

"""
Write a regular expression that can detect dates in the DD/MM/YYYY for-
mat. Assume that the days range from 01 to 31, the months range from 01
to 12, and the years range from 1000 to 2999. Note that if the day or month
is a single digit, it’ll have a leading zero.
The regular expression doesn’t have to detect correct days for each
month or for leap years; it will accept nonexistent dates like 31/02/2020 or
31/04/2021. Then store these strings into variables named month, day, and
year, and write additional code that can detect if it is a valid date. April,
June, September, and November have 30 days, February has 28 days, and
the rest of the months have 31 days. February has 29 days in leap years.
Leap years are every year evenly divisible by 4, except for years evenly divis-
ible by 100, unless the year is also evenly divisible by 400. Note how this cal-
culation makes it impossible to make a reasonably sized regular expression
that can detect a valid date.
"""

# Regular expression for date in MM/DD/YYYY or DD/MM/YYYY format
dateRegex = re.compile(r'''(
    (0?[1-9]|1[0-2])                # month (with or without leading zero)
    /                               # separator
    (0?[1-9]|[12][0-9]|3[01])       # day (with or without leading zero)
    /                               # separator
     (\d{2}|\d{4})                  # year (two or four digits)
    )''', re.VERBOSE)

matches = []

# For an example, open your web browser at:
# https://missing.csail.mit.edu/

# Find matches in clipboard text.
text = str(pyperclip.paste())

for groups in dateRegex.findall(text):
    matches.append(groups[0])
    
#Print the matches
if len(matches) > 0:
    print('Found dates:')
    for match in matches:
        print(match)
else:
    print('No dates found in MM/DD/YYYY or DD/MM/YYYY format.')