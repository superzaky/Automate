#! python3
# backupToZip.py
# Copies an entire folder and its contents into
# a zip file whose filename increments.

import zipfile, os

def backupToZip(folder):
    # Backup the entire contents of "folder" into a zip file.

    folder = os.path.abspath(folder) # make sure folder is absolute
    # Figure out the filename this code should used based on 
    # what files already exist.
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        # if not os.path.exists(zipFilename):
        if not os.path.exists(folder + '\\' + zipFilename):
            break
        number = number + 1

    # Create the zip file.
    print('Creating %s...' % (zipFilename))
    # backupZip = zipfile.ZipFile(zipFilename, 'w')
    backupZip = zipfile.ZipFile('.\\chap_9\\backupToZip_folder\\' + zipFilename, 'w')

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        # Add the current folder to the ZIP file.
        backupZip.write(foldername)
        # backupZip.write('.\\chap_9\\backupToZip_folder\\' + zipFilename) <-- zorgt voor problemen
        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            if filename.startswith(os.path.basename(folder) + '_') and filename.endswith('.zip'):
                continue # don't backup the backup ZIP files
            backupZip.write(os.path.join(foldername, filename))
           

    backupZip.close()
    print('Done.')

backupToZip('.\\chap_9\\backupToZip_folder')
