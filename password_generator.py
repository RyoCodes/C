# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 20:57:08 2022

@author: VARUN
"""

import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    password_length = int(input("How long would you like your password to be? "))
    
    random.shuffle(characters)
    
    password = []
    
    for x in range(password_length):
        password.append(random.choice(characters))
        
        
    random.shuffle(password)
    
    password = "".join(password)
    
    print(password)
    
    
option = input("Do you want yo generate a password? (Yes/No) : ")


if option == "Yes" or option == "yes":
    generate_password()
elif option == "No" or option == "no":
    print("program ended")
    quit()
else:
    print("invalid input, please enter yes or no")
    quit()