import os
from pathlib import Path

def get_total_size(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)
    return total_size

path = Path.cwd()  # Specify the path to your directory here
total_size = get_total_size(path)
print("Total size of all files:", total_size, "bytes")
