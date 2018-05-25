# -*- coding: utf-8 -*-
"""
Created on Sat May 19 10:51:52 2018

@author: Daisy
"""

password="orlando"
for i in range(3):
    pwd=input("Please enter the password: ")
    j=2
    if (pwd==password):
        print("Welcome")
        break
    else:
        print("Chances left are: ",j-i)
        continue
    

print("Please try next time")
        