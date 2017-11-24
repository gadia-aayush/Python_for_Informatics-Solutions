#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 20:02:58 2017

@author: aayushgadia
"""

#EASTER EGGS.........
filename=input('Enter the File Name: ')
if filename=='na na boo boo':
    print("NA NA BOO BOO TO YOU - You have been punk'd! by THE AAYUSH GADIA ")

else:
    f_in=open(filename)
    f_out=f_in.read()
    print(f_out)
