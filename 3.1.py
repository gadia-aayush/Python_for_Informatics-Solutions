#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 02:36:53 2017

@author: aayushgadia
"""

hours_input=float(input("Hours worked\n"))
rph_input=float(input("Rate per hours\n"))
if (hours_input>40):
    pay=40*rph_input + (hours_input-40)*1.5*rph_input
    print("Pay %f"%pay)
    
    
else:
    pay=hours_input*rph_input    
    print("Pay %f"%pay)