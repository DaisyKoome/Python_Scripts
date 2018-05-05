# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 21:21:46 2018

@author: Daisy
"""

#A simple dog class
class Dog():
    """A simple attempt to model a dog"""
    def __init__(self,name,age):
        """Initialize name and age attributes"""
        self.name=name
        self.age=age
        
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title()+"is now sitting.")
        
    def roll_over(self):
        """Simulate a dog rolling over in response to a command."""
        print(self.name.title()+"rolled over.")

#Making an instance from a class
#Making an instance representing a specific dog
my_dog=Dog('willie',6)
print("My dog's name is "+my_dog.name.title()+".")
print("My dog is "+str(my_dog.age)+" years old.")  

#Creating a class
class student:
    
    def details(self,name,age):
        print("the name is {} and the age is {}".format(name,age))
        
#Creating an object
s1=student()
s1.details("collin",35)
    
    