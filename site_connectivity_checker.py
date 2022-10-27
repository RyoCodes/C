# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 23:25:22 2022

@author: VARUN
"""

import urllib.request as urllib



def main(url):
    print("Checking connectivity ")
    
    response = urllib.urlopen(url)
    print("Connected to ", url, "successfully")
    print("The response code was:", response.getcode())

print("This is a site connectivity checker program")
input_url = input("Input the url of the site you want to check: ")

main(input_url)


