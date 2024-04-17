### This is my repository for exercises and projects from the book [Automate the boring stuff with python](https://automatetheboringstuff.com/)

This repository contains my attempts at solving exercises and practice projects from the aforementioned book.

## Projects from chapter 7: Pattern matching with regular expressions

**What you'll find in the files:**
 * `regex_date_detection_test.py`: A simple test to match dates in the format DD/MM/YYYY. The code simply takes 8 predefined dates and tests if they are valid.
 * `regex_date_detection.py`: A more complete solution that takes as input everything from an internet page from the clipboard and searches for dates that match the pattern.
 * `regex_strip.py`: An exercise using regex to build a function that performs the same task as the `strip()` string method.
 * `regex_strong_password.py`: A function using regex to ensure that a password is strong, meaning it meets specific criteria (8 characters long, at least one uppercase letter, one lowercase letter, one special character, and one digit).
   
## Projects from chapter 8:

**What you'll find in the files:**
 * `sandwich_maker.py`: a program that asks the user for their sandwich preferences. This program stores the user's choices, validating them using PyInputPlus. In the file, you'll find a more sophisticated program than the one proposed in the book: instead of asking how many sandwiches the user wants and copying them, this program iterates over the menu, building one different sandwich at a time, and computes the total cost in the end for the n different sandwiches the user asked for. The program can also output how many copies of a particular sandwich the user wants.

## Projects from chapter 9:

**What you'll find in the files:**
 * `extended_mclip.pyw`: an extension of the `mclip` project given in the book with the addition of a `del` line command that deletes a given keyword from the shelf. Usage examples are given within the `.pyw` file.
 * `mad_libs.py`: a program that reads text files and lets the user add their own text where some pre defined words appears.
 * `regex_search.py`: a program that opens all .txt files in a folder and searches for any line that matches a user-supplied regular expression.
