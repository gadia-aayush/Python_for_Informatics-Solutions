#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 09:31:39 2017

@author: aayushgadia
"""
str='X-DSPAM-Confidence: 0.8475'
print(str.find(':'))
#argument in inverted commas

print(str[str.find(':')+1:])
print(float(str[str.find(':')+1:]))