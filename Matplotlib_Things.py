
# coding: utf-8

# In[8]:

import matplotlib.pyplot as plt

#Plotting a graph
#Defining values of x and y
import numpy as np

#Data points for the x-axis
x=np.linspace(0,10,10)

#Creating a sine wave
y=np.sin(x)

#Plotting the sine wave
plt.plot(x,y)

#To show the graph
plt.show()

#Improving the outlook of the plot
plt.plot(x,y)

#Adding an x-label indicating time
plt.xlabel("Time") 

#Plotting a y-label indicating some function of time
plt.ylabel("Some function of time")

#Adding a title to the plotted graph
plt.title("My cool chart")



# In[9]:

#Smoother graph
import matplotlib.pyplot as plt
import numpy as np

#Data points for the x-axis
x=np.linspace(0,10,100)

#Creating a sine wave
y=np.sin(x)

#Plotting the sine wave
plt.plot(x,y)

#Showing the graph
plt.show()


# In[16]:

import pandas as pd
#Loading data and making it into a matrix
A=pd.read_csv(r"C:\Users\USER\Documents\PythonScripts\Data.csv",header=None).as_matrix()

#The x-axis is the first column in the data
x=A[:,0]

#The y-axis is the second column in the data
y=A[:,1]

#Making a scatter-plot
plt.scatter(x,y)

#Showing the plot
plt.show()




# In[21]:

#Plotting an actual line graph side by side with the scatter plot graph
#Creating the x-axis points
x_line=np.linspace(0,100,100)

#Creating the y-axis points
y_line=2*x_line+1

#Creating the scatter plot
plt.scatter(x,y)

#Plotting the actual line graph
plt.plot(x_line,y_line)

#Showing the 2 graphs
plt.show()





# In[22]:

#Making a histogram out of data
plt.hist(x)

#Showing the histogram
plt.show()


# In[24]:

#Showing that the random function brings out data that is uniformly distributed by making a histogram out of it
#Creating random data values
R=np.random.random(10000)

#Plotting the histogram
plt.hist(R)

#Showing the actual histogram
plt.show()


# In[26]:

#Manipulating the number of buckets in a histogram
#In this case,instead of 10 buckets,increasing them to 20
plt.hist(R,bins=20)

#Showing the histogram,now with 20 buckets
plt.show()




# In[27]:

#Proving that in linear regression, the error is normally distributed by creating a scatter plot
y_actual=2*x+1
residuals=y-y_actual

#Plotting a histogram of the residuals
plt.hist(residuals)

#Showing the plot
plt.show()


# In[ ]:



