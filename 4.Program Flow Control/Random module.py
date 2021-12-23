# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 22:39:19 2021

@author: admin
"""


# Random module

import random
highest=10
ans=random.randint(1,highest)
print(ans)  # Remove after testing
guess=200
attempt=0
while ans!=guess:
    print("Guess any number below {}".format(highest))
    guess= int(input(f"ENter your Guess no {attempt+1} below   :"))
    attempt+=1
    
    
    if guess==ans:
        print(f"you got it at attempt no {attempt}")
    else:
        if guess>ans:
            print(f"guess lower in attempt no {attempt+1}")
        else:
            print(f"guess highin attempt no {attempt+1}")
    
    if attempt>=5:
        print("sorry you exhausted all 5 attempts")
        break
    if guess==0:
        print("you exted the game")
        break
