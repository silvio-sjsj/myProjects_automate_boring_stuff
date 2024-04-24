#! python3
# backup_to_zip.py
# Copies an entire folder and its contents into
# a zip file whose filename increments.

import zipfile
import os

def backup_to_zip(folder):
    # Backup the entire contents of "folder" into a zip file.

    folder = os.path.abspath(folder) # Make sure folder is absolute

    # Specify the absolute path to store the zip files
    backup_folder = '~/backups'

    # Figure out the filename this code should use based on what
    # files already exist.
    number = 1
    while True:
        zip_filename = os.path.basename(folder) + '_' + str(number) + '.zip'
        zip_path = os.path.join(backup_folder, zip_filename)
        if not os.path.exists(zip_path):
            break
        number = number + 1

    # Create the zip file.
    print('Creating %s...' % (zip_path))
    backup_zip = zipfile.ZipFile(zip_path, 'w')

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        # Add the current folder to the zip file.
        backup_zip.write(foldername)

        # Add all the files in this folder to the zip file.
        for filename in filenames:
            if filename.startswith(os.path.basename(folder) + '_') and filename.endswith('.zip'):
                continue # Don't backup the backup zip files.
            backup_zip.write(os.path.join(foldername, filename))
    backup_zip.close()
    print('Done.')

# Prompt the user to input the folder path
folder_path = input("Enter the folder path to be backuped: ")

# Call the function with the user-provided folder path
backup_to_zip(folder_path)