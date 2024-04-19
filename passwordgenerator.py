# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 20:41:15 2024

@author: Krista
"""
# =============================================================================
# #modules
# Python allows imports to be on the same line and be seperated by a comma.
# =============================================================================
import string, random

characters = list(string.ascii_letters + string.digits + string.punctuation)

def generate_password():
    #asking the user how long they want their password to be.
    password_length = int(input('Length of password?: '))
    #Shuffling the data from the characters variable.
    random.shuffle(characters)
    
    password = []
    
    for x in range(password_length):
        password.append(random.choice(characters))
        
    random.shuffle(password)
    
    password =''.join(password)
    print(password)
    
generate_password()

    
#Asking the user if they want to generate a password. 
# =============================================================================
# option = input("Do you want to generate a password?: ")
# 
# #Added casefold method to if statement, so case-sensitivity won't be an issue. 
# 
# if option == 'Yes' or'Y'.casefold():
#     generate_password()
# elif option == 'No' or 'N'.casefold():
#     print('No password generated.')
# else:
#     print('Invalid input. Please restart the program and type "Yes" or "No". Thank you.')
# =============================================================================
