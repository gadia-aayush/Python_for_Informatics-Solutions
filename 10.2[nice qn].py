#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 10:51:04 2017

@author: aayushgadia
"""


#we have a file viz of all the email lists of a particular day.....
#assume day is same throughout....

filename=input('Enter the File Name: ')
f_in=open(filename)    
hour_dict={}   
for line in f_in:
    if line.startswith('From '):
        list_new=line.split()
        time=list_new[5]
        hour=time.split(':')[0]
        if hour not in hour_dict:
            hour_dict[hour]=1
        else:
            hour_dict[hour]+=1

new_list=[]        
for h,c in hour_dict.items():
    new_list.append((h,c))
    
new_list.sort()

for h,c in new_list:    
    print(h,c)

            
            
            
#in & not in.......2 methods only operate.........
#is not in....& all....these methods do not exist.......            
    
        
       
    
        
    
    
