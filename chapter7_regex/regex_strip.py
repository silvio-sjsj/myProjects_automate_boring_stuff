# Regex Version of the strip() Method
'''
Write a function that takes a string and does the same thing as the strip()
string method. If no other arguments are passed other than the string to
strip, then whitespace characters will be removed from the beginning and
end of the string. Otherwise, the characters specified in the second argu-
ment to the function will be removed from the string.
'''

import re

def custom_strip(s, chars=None):
    if chars is None:
        # If no specific characters are provided, strip whitespace
        return re.sub(r'^\s+|\s+$', '', s)
    
    # Otherwise, strip the characters specified in the second argument
    pattern = f'^[{re.escape(chars)}]+|[{re.escape(chars)}]+$'
    return re.sub(pattern, '', s)

# Test the function
test_string = "   Hello, World!   "
print(custom_strip(test_string))  # Output: "Hello, World!"

custom_chars = " !"
print(custom_strip(test_string, custom_chars))  # Output: "Hello, World"
