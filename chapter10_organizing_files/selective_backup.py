#! python3
# Usage: python selective_backup.py <source_folder_path> \
# <backup_folder_path> <choices: extensions>"), where <source_folder_path> is the
# folder for which the program will search for files to backup,
# <backup_folder_path> is the folder for which the program will copy the files for, and
# <choice: extensions> are the extensions given by the user of the files that will
# be backuped. At least one choice has to be made.
# Exits if less than 4 arguments are passed.

import os
import re
import sys
import zipfile

def find_and_copy_files(source_folder, backup_folder, choices, zip_filename):
    # Create the target folder if it doesn't exist
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    # Create a list to store the files to be zipped
    files_to_zip = []

    for choice in choices:
        
        # Regular expression pattern to match file extension
        pattern = re.compile(r'\.' + re.escape(choice) + '$', re.IGNORECASE)

        # Walk through the source folder and copy files with the specified extension
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                if pattern.search(file):
                    source_path = os.path.join(root, file)
                    files_to_zip.append(source_path)

    # Path for the backup zip file
    zip_path = os.path.join(backup_folder, zip_filename)
    print('Creating %s...' % (zip_path))

    # Create a zip file
    with zipfile.ZipFile(zip_path, 'w') as backup_zip:
        # Add each file to the zip file
        for file_to_zip in files_to_zip:
            backup_zip.write(file_to_zip, os.path.relpath(file_to_zip, source_folder))

    print('Done.')

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python selective_backup.py <source_folder_path> \
                                                 <backup_folder_path> \
                                                 <choices: extensions>")
        sys.exit(1)

    source_folder = sys.argv[1]
    backup_folder = sys.argv[2]
    choices = sys.argv[3:]
    zip_filename = input("Type the filename of the zip file that will be created\
                          for backup: ")
    find_and_copy_files(source_folder, backup_folder, choices, zip_filename)