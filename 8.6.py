#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 21:04:26 2017

@author: aayushgadia
"""

import sys
num_list=[]
while True:
    num_inp=input('Enter a number: ')   
    
    try: 
        convert=float(num_inp)
        num_list.append(convert)
        
        
    except:    
        if num_inp=='done' or num_inp=='DONE' or num_inp=='Done':
            print('Max of list is: ',max(num_list))
            print('Min of list is: ',min(num_list)) 
            sys.exit()
        
        else:
            print('BAD DATA')
            continue
            