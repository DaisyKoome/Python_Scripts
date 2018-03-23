# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 15:27:54 2018

@author: Daisy
"""

#Simple if statements
age=19
if age>=18:
    print("You're old enough to vote")

#If....else    
age=17
if age>=18:
    print("You're old enough to vote")
else:    
    print("Sorry,you're too young to vote")
    
#If...elif...else chain
age=12
if age<4:
    print("Your entry fee is $0")
elif age<18:
    print("Your entry fee is $5")
else:
    print("Your entry fee is $10")
    
age=12
if age<4:
    price=0
elif age<18:
    price=5
else:
    price=10
print("Your cost price is $"+str(price)+".")

#Using multiple elif blocks
age=20
if age<4:
    price=0
elif age<18:
    price=5
elif age<65:
    price=10
else:
    price=5
print("Your cost price is $"+str(price)+".")

#Testing multiple conditions using independent if statements
requested_toppings=['mushrooms','extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")
print("\nFinished making your pizza!")

#Testing multiple conditions using if-elif-else #It only returns the first true test
requested_toppings=['mushrooms','extra cheese','green peppers']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese")
print("\nFinished making your pizza!")

#Using if statements with lists
requested_toppings=['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    print("Adding "+requested_topping+".")
    
requested_toppings=['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping=='green peppers':
        print("Sorry,we are out of green peppers right now")
    else:
        print("Adding "+requested_topping+".")
print("\nFinished making your pizza!")

#Checking that a list is not empty
requested_toppings=[]
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding"+requested_topping+".")
    print("\nFinished making your pizza!") #Why is it printing this line yet its part of the false conditional test coz there are no requested toppings yet?
else:
        print("Are you sure you want a plain pizza?")
        
#Using multiple lists
available_toppings=['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings=['mushrooms','french fries','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding  "+requested_topping+".")
    else:
        print("Sorry,we do not have "+requested_topping+".")
print("\nWe've finished making your pizza!")


#DICTIONARIES
#A simple dictionary displaying properties of an alien in a game
alien_0={'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])

#Accessing values in a dictionary
new_points=alien_0['points']
print("You have just earned "+str(new_points)+" points!")

#Adding new key-value pairs
print(alien_0)
alien_0['x-position']=0
alien_0['y-position']=25
print(alien_0)

#Starting with an empty dictionary
alien_0={}
alien_0['color']='green'
alien_0['points']=5
print(alien_0)

#Modifying values in a dictionary
alien_0={'color':'green'}
print("The alien now "+alien_0['color']+".")
alien_0['color']='yellow'
print("The alien is now "+alien_0['color']+".")


