# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 20:41:15 2024

@author: Krista
"""
#modules
import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

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
    
#Asking the user if they want to generate a password. 
option = input("Do you want to generate a password?: ")

if option == 'Yes':
    generate_password()
elif option == 'No':
    print('No password generated.')
else:
    print('Invalid input. Please restart the program and type "Yes" or "No". Thank you.')