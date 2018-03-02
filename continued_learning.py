# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 10:01:24 2018

@author: Daisy
"""
#Tuples code
dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])

#Trying to change a tuple
#dimensions[0]=250

#Looping items in a tuple
dimensions=(200,50)
#for dimension in dimensions:
    #print("Value="+str=(dimension)) #Why is this not working?
    
#Redefining a tuple
dimensions=(200,50)
for dimension in dimensions:
    print("Original dimension:")
    print(dimension)
dimensions=(400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension) 
    
    
#If statements
#Changing case for specific items in a list
sports=['tennis','chess','monopoly','scrabble']
for sport in sports:
    if sport=='chess':
        print(sport.upper())
    else:
        print(sport.title())
        
#Checking for equality
requested_topping='mushrooms'
if requested_topping !='anchovies':
    print("Hold the anchovies!")
    
#Numerical comparisons
answer=17
if answer!=42:
    print("That is not the correct answer. Please try again!")
    
#Logical comparisons
#Checking multiple conditions
#Using and to check multiple conditions
age_0=22
age_1=18
condition=age_0>=21 and age_1>=21
print(condition)
#if condition==true:
    #print("True") How do I rephrase this so that it returns true or false?
#age_1=22
#age_0>=21 and age_1>=21 How do I make this return true or false?

#Using or to check multiple conditions
#age_0=22
#age_1=18
#age_0>=21 or age_1>=21 How do I code this to return true or false?
#age_0=18
#age_0>=21 or age_1>=21 How do I make this return true or false?

#Checking whether a value is in a list using keyword in
requested_toppings=['mushrooms','onions','pineapples']
#'mushrooms' in requested_toppings How do I rephrase this to return true or false?
'pepperoni' in requested_toppings

#Checking whether a value is not in a list
banned_users=['andrew','carolina','david']
user='marie'
if user not in banned_users:
    print(user.title()+",you can post a response if you wish.")
    
#Boolean Expressions
   




        

    