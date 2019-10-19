#! python 3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.
#  you run the program by entering this into the command line
# mapit 870 Valencia St, San Francisco, CA 94110

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:    
    # Get address from command line.
    address = ' '.join(sys.argv[1:]) #[1:] is equivalent to "1 to end"
else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
