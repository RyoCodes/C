# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 16:20:48 2022

@author: VARUN
"""

quiz = {
        "question1":{
            "question": "What is the capital of France?", 
            "answer": "Paris"
            },
        "question2":{
            "question": "What is the capital of India ?", 
            "answer": "New Delhi"
            },
        "question3":{
            "question": "What is the capital of Pakistan?", 
            "answer": "Islamabad"
            },
        "question4":{
            "question": "What is the capital of Italy?", 
            "answer": "Rome"
            },
        "question5":{
            "question": "What is the capital of Prtugal?", 
            "answer": "Lisbon"
            },
        "question6":{
            "question": "What is the capital of Germany?", 
            "answer": "Berlin"
            },
        "question7":{
            "question": "What is the capital of Russia?", 
            "answer": "Moscow"
            },
        "question8":{
            "question": "What is the capital of Australia?", 
            "answer": "Canberra"
            },
    }

score = 0
for key, value in quiz.items():
        print(value['question'])
        answer = input("Answer: ")
        
        
        if answer.lower()== value['answer'].lower():
            print('Correct')
            score = score+1
            print("Your score is: " + str(score))
            
        else:
            print("Wrong!")
            print("The answer is: " + value['answer'])
            print("Your score is: " + str(score))
            