#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 12:00:29 2017

@author: aayushgadia
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 10:59:49 2017

@author: aayushgadia
"""


import sys  
i=0
list_num=[]


while(i>=0):
    num_input=input("Enter the Number: ")
    try:
        num=float(num_input)
        print(num)
        list_num.append(num)
        i+=1
        continue       
    
                      
    except:
        if(num_input=='done' or num_input=='DONE' or num_input=='Done'):  
            if (i>0):
                print(list_num) 
                print("Maximum Value is: ",max(list_num),"\nMinimum Value is: ",min(list_num))
            else:
                print("Maximum & Minimum value is NOT DEFINED as List is empty")
            sys.exit()    
                
        else:
            print("BAD DATA, re-enter")
            continue

        
              
        
       
       
    
    
        
        
        
    