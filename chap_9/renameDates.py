"""
Say your boss emails you thousands of files with American-style dates
(MM-DD-YYYY) in their names and needs them renamed to European-style
dates (DD-MM-YYYY). This boring task could take all day to do by
hand! Let’s write a program to do it instead.
Here’s what the program does:
• It searches all the filenames in the current working directory for
American-style dates.
• When one is found, it renames the file with the month and day swapped
to make it European-style.
"""
import shutil, os, re

# Create a regex that matches files with the American date format.
date_pattern = re.compile(r"""^(.*?)
(([01])?\d)-  # one or two digits for the month
(([0123])?\d)- # one or two digits for the day
((19|20)\d\d) # four digits for the year
(.*?)$       # all text after the date
""", re.VERBOSE)

print(os.getcwd())
# Loop over the files in the working directory.
os.chdir('.\\chap_9\\rename_dates_files')
for american_filename in os.listdir('.'):
    match = date_pattern.search(american_filename)

    # Skip files without a date.
    if match is None:
        continue

    # Get the different parts of the filename.
    beforePart = match.group(1)
    monthPart = match.group(2)
    dayPart = match.group(4)
    yearPart = match.group(6)
    afterPart = match.group(8)

    # Form the European-style filename.
    european_filename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # Get the full, absolute file paths.
    abs_working_dir = os.path.abspath('.')
    american_filename = os.path.join(abs_working_dir, american_filename)
    european_filename = os.path.join(abs_working_dir, european_filename)

    # Rename the files.
    print('Renaming "%s" to "%s"...' % (american_filename, european_filename))
    # shutil.move(american_filename, european_filename)
