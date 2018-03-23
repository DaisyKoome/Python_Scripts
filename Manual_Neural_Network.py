
# coding: utf-8

# In[54]:

#Manually making a neural network
#Creating a function that says hello
class SimpleClass():
    def __init__(self,name):
        print("hello "+name)


# In[55]:

#Checking the datatype
s="world"
type (s)


# In[70]:

#Caliing the function
x= SimpleClass('name')


# In[67]:

#Creating another funtion that prints 'yelling'
class SimpleClass():
    def __init__(self,name):
        print("hello "+name)

    def yell(self):
        print("YELLING")


# In[71]:

#Trying out both functions:
#Trying out the hello function
x=SimpleClass('name')


# In[72]:

#Trying out the yell function
x.yell()


# In[73]:

#Creating another class called ExtendedClass that incorporates the SimpleClass
class ExtendedClass(SimpleClass):
    
    def __init__(Self):
        print("EXTEND!")

#Testing the new class
y=ExtendedClass()    


# In[74]:

#Testing the attachment of the new class to the functions in the initial class
y.yell()


# In[75]:

#How to make this special init method in the SimpleCLS also execute within the ExtendedClass class using the super keyword
class ExtendedClass(SimpleClass):
    
    def __init__(Self):
        
        super().__init__('Jose')
        print("EXTEND!")
        
#Testing whether it works:
y=ExtendedClass()


# In[ ]:




# In[ ]:



