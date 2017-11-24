#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 10:11:30 2017

@author: aayushgadia
"""

#Program in which Input is Celsius Temperature & Output is Fahrenheit Temperature.

temp_input=input("Enter the Temperature in Celsius: ")
try:
    ctemp=float(temp_input)
    ftemp= (9.0/5.0)*ctemp + 32
    print(ftemp)
    
except:
    print("\nPlease Enter Temperature in Numbers")

     



