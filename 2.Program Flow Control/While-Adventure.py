# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 08:01:19 2021

@author: admin
# """


# exits=["north","south","east","west"]

# way=""

# while way not in exits:
#     way=input("please choose direction to exit    :")
#     if way.casefold()=="quit":
#         print("game over")
#         break
# print("you got out")    
# Range(0,100,7) print upto divisible by 11 comes
# ist method
# n=1

# while n//12==0:
#     print(n)
#     n+=1
#  #Solution   
# for i in range(0,100,7):
#     print(i)
#     if i>0 and i%11==0:
#         break

# print all numbers from 0 to 20 that arent divisible by either 3 or 5(excluding zero)

# for num in range (0,20):
#    if (num %3==0 or num %5==0):
#       continue
#    print(num)
        


# without continue
for i in range(21):
    if i%3!=0 and i%5!=0:
        print(i)