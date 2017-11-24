#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 09:31:39 2017

@author: aayushgadia
"""
score_input=input("Enter a score b/w 0 and 1\n")

try:
    score=float(score_input)
    if (score<1 and score>0):
        if (score>=0.9):
            print("GRADE A")

        elif(score>=0.8):
            print("GRADE B")
#implies that score<0.9 and score>=0.8, 
#similarly coorelate for rest..

        elif(score>=0.7):
            print("GRADE C")
    
        elif(score>=0.6):
            print("GRADE D")

        else:
            print("GRADE F")    

#ek 'if' ke corresponding ek hi 'else' aata hai....  
    else:
        print("BAD SCORE\nKindly Re-enter the Score..")
    
    
    
except:
    print("BAD SCORE\nKindly Re-enter the Score..")
    
#first try block is tried....
#if try block is not executed then except is executed....
#if try block is executed then program goes out of try except block
