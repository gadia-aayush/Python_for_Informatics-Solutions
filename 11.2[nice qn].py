#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 12:50:07 2017

@author: aayushgadia
"""

import re
filename=input('Enter the file name: ')
f_o=open(filename,'r')

count=0
total=0
for line in f_o:
    line.strip()
    if re.search(r'New Revision: [\d]+',line):
       val=re.search(r'New Revision: [\d]+',line)
       val_g=val.group()
       val2=re.search(r'[\d]+',val_g)
       val2_g=float(val2.group())
       
       total+=val2_g
       count+=1
       
print(total/count)       


#important.......that it is backslash d.....
#i did the mistake of not putting...backslash \...i had put forward slash..../       
     
