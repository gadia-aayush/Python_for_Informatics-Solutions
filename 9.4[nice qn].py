#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 21:40:40 2017

@author: aayushgadia
"""


i=0
sender_list=[]
filename=input('Enter a file name: ')
f_in=open(filename)
for line in f_in:
    if line.startswith('From '):
        word_list=line.split()
        sender=word_list[1]
        sender_list.append(sender)

print(sender_list,'\n')        
d=dict()       
for sent in sender_list:
    if sent not in d:
        d[sent]=1
        
    else:
        d[sent]+=1
       
print(d)     

new_d={}
for k,v in d.items():
    new_d[v]=k
    if v>i:
        i=v
        continue
    else:
        continue
    
print(new_d)          
print('\nMaximum messages is by',new_d[i],'with',i,'messages')        

