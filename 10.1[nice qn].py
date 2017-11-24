#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 10:20:01 2017

@author: aayushgadia
"""

filename=input('Enter File Name: ')
f_in=open(filename)

emailadd_dict={}
for line in f_in:
    if line.startswith('From '):
        split_list=line.split()
        email_add=split_list[1]
        if email_add not in emailadd_dict:
            emailadd_dict[email_add]=1
            
        else:
            emailadd_dict[email_add]+=1

i=0        
emailadd_tuplelist=[]
#it is a definite loop....
for k,v in emailadd_dict.items():
    emailadd_tuplelist.append((v,k))
    
emailadd_tuplelist.sort(reverse=True)
print(max(emailadd_tuplelist))

