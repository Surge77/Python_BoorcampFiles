"""
WAP that uses the getpass module to prompt the user for a password, without echoing what they type to the console
"""

import getpass

password = getpass.getpass(prompt='Enter your password: ')

if password == 'tejas':
    print("Welcome to my world")
else:
    print("You don't deserve to be here!")