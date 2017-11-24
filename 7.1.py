#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 08:57:58 2017

@author: aayushgadia
"""

file_name=input('Enter file name: ')
f_in=open(file_name)
for line in f_in:
    print(line.upper())
