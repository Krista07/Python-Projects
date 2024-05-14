# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 20:41:15 2024

@author: Krista
"""
# =============================================================================
# #modules
# Python allows imports to be on the same line and be seperated by a comma.
# =============================================================================
#This is an updated Password generator using the most up to date functions for Python

#Python allows you to use multiple modules within the same line for the import function.

import string, secrets, random

#This is a custom variable to calls letters from the alphabet, numbers, and random keyboard symbols.
characters = list(string.ascii_letters + string.digits + string.punctuation)

def generatePassword():
    #Creates a password based on digital input from the user.
    password = ''.join(secrets.choice(characters) for i in range(int(input('Character length for password?: '))))

    print(password)

generatePassword()