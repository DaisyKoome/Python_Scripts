
# coding: utf-8

# In[17]:

import numpy
L=[1,2]
#Creating a function called area
def area(l,w):
    answ=l*w
    print(answ)
    
area(2,3)
area(34,56)


# In[3]:

#Adding lists
L1=[2,3]
print(L+L1)


# In[4]:

L2=[]
#Using in and zip functions to sum values separately in x and y
for e,f in zip(L,L1):
    print(e+f)


# In[19]:

#Making lists into numpy arrays
a1=numpy.array(L)
a2=numpy.array(L1)

#Multiplying numpy arrays
a1*a2


# In[9]:

#Printing numpy arrays
print(a1)
print(a2)


# In[16]:

#Addition of numpy arrays and python lists
print(a1+a2)
print(L1+L)


# In[18]:

#Dot product
a=numpy.array([1,3])
b=numpy.array([2,4])
dot=0
for x,y in zip(a,b):
    dot+=x*y
print(dot)


# In[20]:

#Using Function dot from numpy
numpy.dot(a,b)


# In[3]:

#Appending a list using append
L=[1,2,3]
L.append(9)
print(L)


# In[17]:

#Appending a list using + []
L=L+[5]
print(L)
print(2*L)


# In[8]:

#Appending an empty list using a loop
L2=[]
for e in L:
    L2.append(e+e)
print(L2)


# In[16]:

#Performing simple arithmetic on numpy arrays
import numpy
t=numpy.array([1,2,3,4])
t+t
print(t+t)
print(2*t)


# In[24]:

#Appending squares of a previous list (L) in an empty list L2
L2=[]
for e in L:
    L2.append(e*e)
print(L2)


# In[25]:

#Using numpy arrays to calculate squares of numbers
print(t**2)


# In[27]:

#Getting square roots using numpy
numpy.sqrt(A)


# In[28]:

#Getting logs using numpy
numpy.log(A)


# In[29]:

#Getting exponentials using numpy
numpy.exp(A)


# In[2]:

#Making a list into a numpy array
import numpy
a=numpy.array([1,2])
b=numpy.array([2,1])
print(a,b)


# In[7]:

#Dot product ((ax*ay)+(bx*by))
dot=0
for x,y in zip(a,b):
    dot+=x*y
print(dot)


# In[8]:

#Multiplying numpy arrays
a*b


# In[9]:

#Summing numpy arrays
numpy.sum(a*b)


# In[10]:

#(a*b).sum why doesnt this work?


# In[11]:

#Using the numpy dot function
numpy.dot(a,b)


# In[12]:

#Alternative way of using the dot function
a.dot(b)


# In[13]:

b.dot(a)


# In[15]:

#Calculating the magnitude of a
amag=numpy.sqrt((a*a).sum())
amag


# In[16]:

#Calculating the norm of a using numpy's linalg function
amag=numpy.linalg.norm(a)
amag


# In[18]:

#Calculating the cosangle
cosangle=a.dot(b)/(numpy.linalg.norm(a)*numpy.linalg.norm(b))
cosangle


# In[20]:

#Calculating the actual angle in radians
angle=numpy.arccos(cosangle)
angle


# In[24]:

#Caculate how much faster the dot function of numpy is than the for loop when calculating dot product
import numpy
from datetime import datetime
#What do the following lines of code mean?
a=numpy.random.randn(100)
b=numpy.random.randn(100)
T=100000

def slow_dot_product(a,b):
    result=0 
    for e,f in zip(a,b):
        result+=e*f
        return result
    
t0=datetime.now()
for t in xrange (T):
    slow_dot_product(a,b)
dt1=datetime.now()-t0

t0=datetime.now()
for t in xrange (T):
    a.dot(b)
dt2=datetime.now()-t0

print("dt1/dt2:",dt1.totalseconds()/dt2.totalseconds())
    