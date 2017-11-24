#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 20:43:03 2017

@author: aayushgadia
"""

filename=input('Enter Mailbox Data Filename: ')
f_in=open(filename)
i=0
for line in f_in:
    if line.startswith('From '):
        i+=1
        sent_names=line.split()
        print(sent_names[1])
            
print('There were',i,'lines in the file with From as the first word')        
          

