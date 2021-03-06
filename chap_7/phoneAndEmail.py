#! python3
# # phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.
import pyperclip
import re

phoneRegex = re.compile(r'''(    
    (\d{3}|\(\d{3}\))?                # area code    
    (\s|-|\.)?                        # separator    
    (\d{3})                           # first 3 digits    
    (\s|-|\.)                         # separator    
    (\d{4})                           # last 4 digits    
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension    
    )''', re.VERBOSE)

# Create email regex.
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username     
    @                      # @ symbol    
    [a-zA-Z0-9.-]+         # domain name    
    (\.[a-zA-Z]{2,4})      # dot-something    
    )''', re.VERBOSE)

# TODO: Find matches in clipboard text.
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# TODO: Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')

# Copy the below text and run the app.
'''
Skip to main content
Home
Search form

        Catalog
        Blog
        Media
        Write for Us
        About Us
        Contact Us

Topics

    Art & Design
    General Computing
    Hacking & Computer Security
    Hardware / DIY
    Kids
    LEGO®
    Linux & BSD
    Manga
    Programming
    Python
    Science & Math
    Scratch
    System Administration
    Early Access

Free ebook edition with every print book purchased from nostarch.com!
Shopping cart
0 Items	Total: $0.00
User login

    Log in
    Create account

Contact Us

No Starch Press, Inc.
245 8th Street
San Francisco, CA 94103 USA
Phone: 800.420.7240 or +1 415.863.9900 (9 a.m. to 5 p.m., M-F, PST)
Fax: +1 415.863.9950

Reach Us by Email

    General inquiries: info@nostarch.com
    Media requests: media@nostarch.com
    Academic requests: academic@nostarch.com (Please see this page for academic review requests)
    Help with your order: info@nostarch.com

Reach Us on Social Media
Twitter
Facebook
Instagram
Pinterest
Navigation

    My account

Want sweet deals?
Sign up for our newsletter.

About Us  |  Jobs!  |  Sales and Distribution  |  Rights  |  Media  |  Academic Requests  |  Conferences  |  Order FAQ  |  Contact Us  |  Write for Us  |  Privacy

Copyright 2019. No Starch Press, Inc
'''
