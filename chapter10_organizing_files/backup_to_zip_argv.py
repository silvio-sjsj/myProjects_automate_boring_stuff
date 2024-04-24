# backup_to_zip_argv.py - Copies an entire folder and its contents into
# a zip file whose filename increments.
# Usage: python backup_to_zip_argv.py <source_folder_path> <backup_folder_path>
# Creates a zip file as backup in backup_folder_path from folder and files
# in source_folder_path
# Exits if not exactly three arguments were passed

import zipfile
import os
import sys

def backup_to_zip(source_folder, backup_folder):
    # Backup the entire contents of "source_folder" into a zip file.

    source_folder = os.path.abspath(source_folder) # Make sure source_folder is absolute

    # Make sure backup_folder is absolute
    backup_folder = os.path.abspath(backup_folder)

    # Figure out the filename this code should use based on what
    # files already exist.
    number = 1
    while True:
        zip_filename = os.path.basename(source_folder) + '_' + str(number) + '.zip'
        zip_path = os.path.join(backup_folder, zip_filename)
        if not os.path.exists(zip_path):
            break
        number += 1

    # Create the zip file.
    print('Creating %s...' % (zip_path))
    with zipfile.ZipFile(zip_path, 'w') as backup_zip:
        # Walk the entire folder tree and compress the files in each folder.
        for foldername, subfolders, filenames in os.walk(source_folder):
            print('Adding files in %s...' % (foldername))
            # Add the current folder to the zip file.
            backup_zip.write(foldername)

            # Add all the files in this folder to the zip file.
            for filename in filenames:
                if filename.startswith(os.path.basename(source_folder) + '_') and filename.endswith('.zip'):
                    continue # Don't backup the backup zip files.
                backup_zip.write(os.path.join(foldername, filename))
    print('Done.')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python backup_to_zip.py <source_folder_path> <backup_folder_path>")
        sys.exit(1)

    source_folder = sys.argv[1]
    backup_folder = sys.argv[2]

    backup_to_zip(source_folder, backup_folder)
