# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 11:03:08 2022

@author: VARUN
"""

import PyPDF3
import pyttsx3
import pdfplumber

file = 'C:\\Users\VARUN\OneDrive\Documents\lorem.pdf'

book = open(file, 'rb')
pdfReader = PyPDF3.PdfFileReader(book)

pages = pdfReader.numPages
finalText = ""
 
with pdfplumber.open(file) as pdf:
     for i in range(0,pages):
         page = pdf.pages[i]
         text = page.extract_text()
         text = page.extract_text()
         finalText += text
         
engine = pyttsx3.init()
engine.say(finalText, 'Lorem.mp3')
engine.runAndWait()         