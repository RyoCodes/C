# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 15:55:05 2022

@author: VARUN
"""

def main():
    print(" Welcome to the email slicer ")
    print("")
    
    email_input = input("Input your email address: ")
    
    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")
    
    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension:", extension)
    
while True:
    main()