#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 09:31:39 2017

@author: aayushgadia
"""

input_hours=float(input("Enter Hours\n"))
input_rateperhours=float(input("Enter Rate per hours\n"))
gross=input_hours*input_rateperhours
print("Pay {0}".format(gross))