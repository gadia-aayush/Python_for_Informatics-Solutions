#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 10:59:49 2017

@author: aayushgadia
"""


import sys  #sys is a module
sum=0
i=0


#for Infinite Loop in Python use While Loop use....
#always loop mein 3 things hota hai....Initialisation, Test, Increment....
while(i>=0):
    num_input=input("Enter the Number: ")
#here compare operator use as we are comparing whether LHS is equal to RHS or not...
#here assignment operator use nahi karenge....           
    try:
        num=float(num_input)
        print(num)
        i+=1
        sum+=num
        continue
        
                      
    except:
        if(num_input=='done' or num_input=='DONE' or num_input=='Done'):           
           if(i>0):
               average=sum/i 
               print("Total: ",sum,"Average: ",average,"Count: ",i)                             
           else:
               print("Total: ",sum,"Average is Not Defined as Denominator is Zero"," Count: ",i)                
 # and exit is a function with argument in brackets              
           sys.exit()           
        else:
            print("BAD DATA, re-enter")
            continue
        
'''even if there are no arguments in exit function, 
keep the argument brackets empty.....but do use the arguments bracket'''

#always see kaha program start & kaha terminate...        
        
       
       
    
    
        
        
        
    