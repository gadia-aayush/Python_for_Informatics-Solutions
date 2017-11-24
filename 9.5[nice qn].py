#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 21:59:30 2017

@author: aayushgadia
"""


filename=input('Enter a file name: ')
domain_list=[]
f_in=open(filename)
for line in f_in:
    if line.startswith('From '):
        line_split=line.split()
        email_add=line_split[1]
        pos=email_add.find('@')
        domain=email_add[pos+1:]
        domain_list.append(domain)
        
      
domain_dict={}
    
for domain in domain_list:
    if domain not in domain_dict:
        domain_dict[domain]=1
        
    else:
        domain_dict[domain]+=1
        
print(domain_dict)        
        
        
     
