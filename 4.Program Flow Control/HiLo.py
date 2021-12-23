# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 23:14:37 2021

@author: admin
"""


# Hi lo game in 10 guess becoz 2^10=1024
low=1
high=1000

print(f"Please think any number between {low} and {high}")

input("press ENTER to start")
num=1
guess=1
while True:
    guess=low+(high-low)//2
    print(f"computer's guess no {num} is {guess}" )
    h_l=input(f"computer's guess number {num} is {guess} Should i guess higher or lower ? Enter h or l   or c :").casefold()
    if h_l=="h":
        low=guess
        num+=1
    elif h_l=="l":
        high=guess
        num+=1
    else:
        print(f"hurraay guessed correctly on guess number {num} ")
        break
        