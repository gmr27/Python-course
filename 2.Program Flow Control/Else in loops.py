# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 00:45:46 2021

@author: admin
"""


numbers=[1,45,31,12,60]
for num in numbers:
    if num %8==0:
        print("the numbers are unacceptable")
        break
else:
    print("all those numbers are fine")