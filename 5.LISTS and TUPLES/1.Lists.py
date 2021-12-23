# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 10:10:13 2021

@author: admin
"""


parts=["computer",
       "monitor",
       "keyboard",
       "mouse",
       "mat"
       ]
for part in parts:
    print(part)
parts2=parts
print(id(parts))
print(id(parts2))    

parts+=["pen drive"]
print(parts)
print(id(parts))
print(id(parts2))    
# they have same id
