import re

# Regular expression to match DD/MM/YYYY format
date_regex = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(1000|1[0-9]{3}|2[0-9]{3})$'
date_regex = re.compile(date_regex, re.VERBOSE)

# Test input
test_dates = [
    "31/02/2020",
    "29/02/2021",
    "30/04/2021",
    "31/06/2022",
    "15/12/2023",
    "01/01/2024",
    "25/02/2025",
    "31/04/2026"
]

# Loop through test dates
for date_str in test_dates:
    match = re.match(date_regex, date_str)
    if match:
        # Extract day, month, and year from the matched groups
        day = int(match.group(1))
        month = int(match.group(2))
        year = int(match.group(3))
        
        # Check for valid date
        valid = True
        if month in [4, 6, 9, 11] and day > 30:
            valid = False
        elif month == 2:
            if day > 28 and (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0)):
                valid = False
            elif day > 29:
                valid = False
        elif day > 31:
            valid = False
        
        # Print validation result
        if valid:
            print(f"{date_str} is a valid date.")
        else:
            print(f"{date_str} is not a valid date.")
    else:
        print(f"{date_str} does not match the expected format.")
