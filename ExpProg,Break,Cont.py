# -*- coding: utf-8 -*-
"""
Created on Fri May 18 04:58:43 2018

@author: Daisy
"""
#Calculating powers of numbers
print(2**3)
print(3**2)
print(pow(2,3))
print(pow(3,2))

num=int(input("Enter the number: "))
exp=int(input("Enter the exponential: "))
result=1
for i in range (1,(exp+1)):
    result=result*num
print("The result is: ",result)

i=1
while(i<=100):
    print(i)
    if(i==50):
        break
    i=i+1

while 1:
    name=input("Enter the name: ")
    if(name=='quit'):
        break
    
    #OR
    
i=1
while (i==1):
    name=input("Enter the name: ")
    if(name=='exit'):
        break
    
i=1
while(i<=100):
    i=i+1
    if (i<=50):
        continue
    print(i)

        
