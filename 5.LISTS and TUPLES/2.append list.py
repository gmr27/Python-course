# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 19:20:23 2021

@author: admin
"""


# even=[2,4,6,8]
# odd=[1,3,5,7,9]
# print(min(odd))
# print(len(even))

# print("mississippi".count("s"))


current_choice="-"
parts=[]
while current_choice!="0":
    if current_choice in "12345":
        print(f"Adding {current_choice}")
        if current_choice==1:
            parts.append("computer")
        elif current_choice==2:
            parts.append("monitor")
        elif current_choice==3:
            parts.append("keyboard")
        elif current_choice==4:
            parts.append("mouse")
        else:
            parts.append("mat")
    else:
        print("please add options from the list below    :")
        print("1.Computer")
        print("2.monitor")
        print("3.keyboard")
        print("4.mouse")
        print("5.mat")
        print("0. to finish")
    current_choice=input(" enter ")    
    
print(parts)    