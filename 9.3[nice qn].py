#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 21:19:47 2017

@author: aayushgadia
"""

days_list=[]
filename=input('Enter a file name: ')
f_in=open(filename)
for line in f_in:
    if line.startswith('From '):
        word_list=line.split()
        day=word_list[2]
        days_list.append(day)

   
d=dict()       
for day in days_list:
    if day not in d:
        d[day]=1
        
    else:
        d[day]+=1
       
print(d)        


#it will be line.startswith('From ')....it is From then space........
#earlier i just wrote....'From' & did not put any space...after From.....