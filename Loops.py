# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 06:45:25 2018

@author: Daisy
"""
for i in range (6):
    print("Hello world!")
    
for i in range (6):
    print(i)
    
for i in range(1,7):
    print(i)
    
for i in range(0,12,2):
    print(i)
    
name="Daisy"
for i in range (6):
    print(name)
    
num=0
for i in range (1,6):
    num=num+i
    print(num)
    
num=0
for i in range(5):
    num=num+i
    print(num)
    
i=0
while (i<5):
    i=i+1
    print("Hi there!")
    
i=0
while (i<=5):
    i=i+1
    print("God is good! :-)")

#A program to calculate and display the factorial of a number    
fact=1
num=int(input("Please enter any number: "))
for i in range(1,(num+1)):
    fact=fact*i
    print(fact)
print("The factorial of",num,"is",fact)
    



