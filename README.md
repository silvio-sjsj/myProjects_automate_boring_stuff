### This is my repository for exercises and projects from the book [Automate the boring stuff with python](https://automatetheboringstuff.com/)

This repository contains my attempts at solving exercises and practice projects from the aforementioned book.

**What you'll find in the files:**
 * `map_it.py`: it gets an adress from command line and opens its map from google maps.

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

## Projects from chapter 10:

**What you'll find in the files:**
 * `add_pref_or_sufix.py`: adds a prefix or a sufix, as given by the user, to all files in a given folder that matches some pattern name given by the user. This is a program to be called from the terminal with 4 arguments: the program itself, the source folder, the pattern to match and a choice (prefix or sufix).
 * `add_prefix.py`: This program is to rename some number of files in a given folder. It is part of the "ideas for similar programs" given in the book. IT adds a given prefix to the start of a filename if it contains a given pattern.
 * `add_prefix2.py`: Similar to the program above but this one adds a prefix to all files in a given folder and all its subfolders.
 * `backup_to_zip.py`: this is the program given in the book with some minor changes like, for example, the folder to be backuped is given by the user as input to the program.
 * `backup_to_zip_argv.py`: the `backupToZip.py` program given in the book with some adjustments to make it better and more versatile: the folder to be backuped and the folder where the backup will be stored are inputs given as arguments by the user while calling the program from the terminal; in this way the program can backup any folder and store this backup where the user wants.
 * `filling_gaps.py`: this is the "Filling in the gaps" practice project proposed. This program receives as argument a source folder path given by the user and it renames every file in that folder for every extension it finds in there filling numbered gaps like, for example, if there are x_001, x_04, x_00099 etc to x_1, x_2, x_3 etc. It has some minor flaws like, for example, assuming that all the files to be renamed has some prefix before the numbers, like for example aa_0001, aa_009 and b_02, b_000082 and so on.
 * `rename_dates.py`: this is the code given in the book with some minor changes like, for example, the folders of american dates and european dates are not the same and are given to the program with their corresponding paths.
 * `selective_backup.py`: a program to backup only files in a given folder and its subfolders with a given extension provided by the user (any number of extensios are possible).
 * `selective_backup2.py`: a program to backup only files in a given folder and its subfolders that does NOT have the extensio(s) provided by the user.
 * `selective_copy.py`: copy all files in a folder and its subfolders to another folder that matches a given extension. The source folder, the target folder and the extension(s) are all provided by the user.
 
## Projects from chapter 11:

**What you'll find in the files:**
 * `debugging_coin_toss.py`: a simple guess game with two guesses between two options (really easy game to win). The original code had some bugs and here we try to find them and correct them.
 
## Projects from chapter 12:

**What you'll find in the files:**
 * `open_pages.py`: open a list of web pages from command line arguments. It doesn't need full page name but only what's between https://wwww. and .com. Example: gmail, youtube, github etc.
 * `weather.py`: The program opens up the openwather page for the city chosen and also prints some information on the screen. 
