"""Code containing my solution to the practice project 'strong password detection'"""
import re

"""
Strong Password Detection
Write a function that uses regular expressions to make sure the password
string it is passed is strong. A strong password is defined as one that is at
least eight characters long, contains both uppercase and lowercase charac-
ters, and has at least one digit. You may need to test the string against mul-
tiple regex patterns to validate its strength.
"""

def is_strong_password(password):
    # Check if the password is at least eight characters long
    if len(password) < 8:
        return False
    
    # Check if the password contains both uppercase and lowercase characters
    if not re.search(r'[a-z]', password) or not re.search(r'[A-Z]', password):
        return False

    # Check if the password contains at least one special character
    if not re.search(r'[!@#$%^&*()-_=+{};:,<.>]', password):
        return False

    # Check if the password contains at least one digit
    if not re.search(r'\d', password):
        return False
    
    return True

# Test the function
password1 = "StrongPassword#123"
password2 = "weakpass_"
password3 = "NoNumsHere"
password4 = "all_lowercase123"
password5 = "ALLUPPERCASE"
password6 = "AnothERStrong333?"
password7 = "Short_#"
password8 = "anotherweak1"
password9 = "99#$VeRy_StROnG12"

print(is_strong_password(password1))  # True
print(is_strong_password(password2))  # False
print(is_strong_password(password3))  # False
print(is_strong_password(password4))  # False
print(is_strong_password(password5))  # False
print(is_strong_password(password6))  # True
print(is_strong_password(password7))  # False
print(is_strong_password(password8))  # False
print(is_strong_password(password9))  # True