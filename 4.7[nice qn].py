#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 10:24:08 2017

@author: aayushgadia
"""
#we first define the function...then we call the function...    
def computegrade(score):
    if (score>0 and score<1):
    #in Python, we use the letter 'and', not the symbolic '&&'.        
        if (score>0.9):
            print('GRADE A')
            
        elif(score>0.8):    
            print('GRADE B')
                
        elif(score>0.7):    
            print('GRADE C')
            
        elif(score>0.6):    
            print('GRADE D')
                    
        else:    
            print('GRADE F')
                
                
    else:
        print("BAD SCORE, re-enter")
    

score_input=input("Enter the score, the Maximum Marks is 1: ")
try:
    score=float(score_input)
    print(score)
    computegrade(score)
#here we are now calling the defined function........
#for calling the defined function.....simply write function name with arguments in bracket.    

 
except:
    print("BAD SCORE,re-enter")    
    
    
#always remember, that after defining a function you have to call that function....
#if you have defined a function and if you don't call it.....then nothing will happen...very IMPORTANT
    



        
 
    
    