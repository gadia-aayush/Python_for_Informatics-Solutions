#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 12:16:13 2017

@author: aayushgadia
"""

import re
filename=input('Enter the Filename: ')
f_o=open(filename,'r')
regx_in=input('Enter the Regular Expression: ')
pattern=re.compile(regx_in)

count=0
for line in f_o:
    line.strip()
    if re.search(pattern,line):
#if you write 'line_list'...then it will become string        
        count+=1
        
print (count)      


'''....very very important....
re.search(r'regular expression','data jisme seacrh')
humlog regular expression ko regx_in mein daale...and this
cannot be directly put in re.search().....expression....
as ' ' inverted commas bhi we are not using....
so regx_in ko we will do compile by re.compile.....and then
uska output ko we will keep in re.search......and similarly since
data jisme search must be a string......so humlog line ko strip karenge
usse ek string output mein milega......and then uss output ko put
in re.search expression....'''

'''r'regular expression'....this is the format...agar regular expression ko compile
kar lega.....den r'regular expression' ke jagah...simply woh compiled ka output likhne 
se ho jayega..... re.findall(compile_output,data)'''

