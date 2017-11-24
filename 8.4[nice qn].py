#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 20:28:42 2017

@author: aayushgadia
"""

f_in=open('dictionary_qn.txt')
word_list=[]
for line in f_in:
    for word in line.split():
        if word not in word_list:
            word_list.append(word)
            

word_list.sort()
print(word_list)   

#this is very important....that if..
''' t=word_list.sort()....print(t) then none will come as output....
if print(word_list.sort()) then also none will come as output...'''        
    
'''so first you have to apply the sort method on the word_list data...and then
you have to print the word_list data.....'''

#REMEMBER THIS FORM...its very important......    
 
'''same applies to .append() too........like it was applied on .sort()....'''
'''if print(word_list.append()) then nothing will be printed..so first you have to
apply the method on the data...and then print the data....this is specially for lists'''

'''sort.....will arrange all alphabetically.....with numbers at the first....
then by alphabets..observe the output......'''




