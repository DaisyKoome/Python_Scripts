
# coding: utf-8

# In[3]:

from scipy.stats import norm
#Gaussian PDF and CDF
#Finding the probability of 0 from standard normal distribution
norm.pdf(0)


# In[5]:

#For a gaussian that has a mean other than 0 and a variant other than 1
norm.pdf(0,loc=5,scale=10) #Mean=5 and standard deviation=10 which corresponds to variants of 100 resulting to  a smaller probability density

#Calculating the probability density of many different values contained within an array simultaneously
#Getting a random array
import numpy as np
r=np.random.randn(10)

#Instead of using a for loop to calculate the probability density of each individual value,scipy has a function that enables calculation of the pdf of all values at the same time
#Using logarithms to calculate PDF (Probability Density Function) in this case makes it easier
norm.logpdf(r)


# In[8]:

#The Cumulative Distribution Function (CDF)
#Computing CDF of r(from th preceding code above) numerically using a scipy function
norm.cdf(r)

#Calculating the log of cdf
norm.logcdf(r)


# In[10]:

#Sampling form the standard normal distribution
#10000 samples
r=np.random.randn(10000)

#Plotting a histogram of the 10000 random samples in order to verify that it is indeed the standard normal
import matplotlib.pyplot as plt
plt.hist(r,bins=100)

#Showing the histogram
plt.show()


# In[17]:

#Sampling from a gaussian distribution that has an arbitrary mean and a standard deviation
#Scaling the function and adding the mean
import numpy as np
r=10*np.random.randn(10000) + 5 #5 is the mean in this case #This gives samples from a gaussian distribution with standard deviation 10 and mean 5

#Creating a histogram to verify that the distribution is standard
plt.hist(r,bins=100)

#Showing the histogram
plt.show()




# In[18]:

#Working with data that is multi-dimensional
#Sampling from a 2D Gaussian with a mean of 0 and variants 1 #This is a spherical gaussian because each dimension is unco-related and independent of the other and they all have the same variants
#The data should be spread out in a circle when plotted
#Adding more dimensions to the function that has been used
r=np.random.randn(10000,2)

#Verifying that these points have neen spread out in a circular cloud using a scatter plot
plt.scatter(r[:,0],r[:,1])

#Showing the scatter plot
plt.show()



# In[21]:

#Sampling from an elliptical gaussian where the variants are different for each function
#For example, a gaussian where the standard deviation of the 2nd dimension is 5 and the mean is 2 #To do this,just scale the data
r[:,1]=5*r[:,1]+2

#Creating a scatter plot to prove that the above code works
plt.scatter(r[:,0],r[:,1])

#To make each axis equal size
plt.axis('equal')

#Showing the scatter plot
plt.show()




# In[ ]:



