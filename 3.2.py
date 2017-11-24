#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 09:31:39 2017

@author: aayushgadia
"""
#try except ke liye if else hona not necessary.
#both work independent
hours_input=input("Enter Hours Worked\n")
rph_input=input("Enter Rate per Hours\n")
try:
    hours=float(hours_input)
    rph=float(rph_input)
    pay=hours*rph
    print("%f"%pay)
    
except:
    print("Please enter NUMERICS only")