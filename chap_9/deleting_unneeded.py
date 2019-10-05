#!/usr/bin/env python3
"""Walk a folder tree and print the names of files above a chosen size."""

import os

# .\\chap_9\\deleting_unneeded_files
folder = input("Enter the absolute path of the folder you'd like to search: ")

threshold = input("Enter the maximum file size that you'd"
                  " like to ignore (in megabytes): ")

for folders, subfolders, filenames in os.walk(folder):
    for filename in filenames:
        size = os.path.getsize(os.path.join(folders, filename))

        if size > float(threshold) * 10 ** 3:   # KB to byte conversion
            # >>> 10/3
            # 3.3333333333333335
            # >>> 10//3
            # 3
            # ** = 10 raised to the 3th power
            print(filename, '| Size = ', size // 10 ** 3, 'KB' '| Path =', 
os.path.join(folders, filename))
