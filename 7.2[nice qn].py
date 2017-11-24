#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 19:50:05 2017

@author: aayushgadia
"""
filename=input('Enter File Name: ')
f_o=open(filename)
val=0
count=0
for line in f_o:
    if line.startswith('X-DSPAM-Confidence-'):
        pos=line.find('.')
        i=float(line[pos-1:])
        val+=i
        count+=1
        print(i,'\t',val,'\n')

print('Total Spam Confidence= ',val,'\n','Total no. of lines in which spam confidence appeared= ',count)        
print('Average Spam Confidence= ',val/count)        


#use dictionary_qn.txt as the file......and bring it in the folder in which 7.2.py file is