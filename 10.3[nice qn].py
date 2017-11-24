#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 11:32:57 2017

@author: aayushgadia
"""

def most_frequent():
#very necessary to add parenthesis after function name...when defining function...

    str_in=input('Enter a string: ')
    str_new1=str_in.lower()
    str_new2=str_new1.replace(' ','')
    str_new=str_new2.strip()    
    str_dict={}
    for char in str_new:
        if char not in str_dict:
            str_dict[char]=1
            
        else:
            str_dict[char]+=1
    str_list=[]
    for k,v in str_dict.items():
        str_list.append((v,k))
        #(v,k) ko we made it 1 argument.....by making it a tuple......
        str_list.sort(reverse=True)
        
    for v,k in str_list:
        print(v,k)
        
#we have created a list....where we have exchanged the position of keys & values
#now when we have sorted this list........then it was sorted numerically...and we did reverse sort..descending
#and when numbers are same like for 6,4,3,2....then it is sorted alphabetically and that too...reverse sort....in descending order
#thats why....in 1...first u came..then p. then m.. then l   

most_frequent()
  
#.split....returns a list
#.strip....returns a string only......





