# -*- coding: utf-8 -*-
"""
Created on Sun May 13 04:45:02 2018

@author: Daisy
"""
fact=1
i=1
num=int(input("Enter any number:"))
while (i<=num):
    fact=fact*i
    print(fact)
    i=i+1
print("The factorial of",num,"is",fact)

num=int(input("Enter any number:"))
for i in range(1,11):
    print(num,"X",i,"=",num*i)
    
i=0
num=int(input("Please enter any number:"))
while (i<=10):
    print(num,"X",i,"=",num*i)
    i=i+1
    
"""For a multi multiplication table"""
num=int(input("Please enter any number: "))
for i in range(1,(num+1)):
    print("\n")
    for j in range(1,11):
        print(i,"X",j,"=",i*j)
    
    