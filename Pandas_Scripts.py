
# coding: utf-8

# In[31]:

#Panda code
#Converting a csv file into a matrix
import pandas
x=[]
for row in open(r"C:\Users\USER\Documents\PythonScripts\Data.csv"):
    row=row.split(",")
    x.append(row)
print(x)

#Finding out the data type
type(x)#Why is my type a list whereas in the tutorial its a dataframe?

#Finding out the structure of the list by making it into a numpy array
import numpy as np
x=np.array(x)
x.shape

#Finding out info about the list
import pandas 
x.info()#Why is this not working?

#Finding out what is in the head of the csv file
get_ipython().set_next_input('x.head() Why is this not displaying Maths,Eng, Swa as the head');get_ipython().magic('pinfo head')

#Why is this reading the first row instead of the first column?
x[0]


# In[12]:

#The following are various ways that I tried to use in loading data from a CSV file made in excel


# In[9]:

data = np.genfromtxt(r"C:\Users\USER\Documents\PythonScripts\Data.csv", dtype=float, delimiter=',', names=True)


# In[46]:

import pandas
def readcsv(r"C:\Users\USER\Documents\PythonScripts\Data.csv"):
      with open Data.csv as csvfile
      file=csv.reader(csvfile, delimiter=",")


# In[30]:

import pandas as pd
X=pd.read_csv(r"C:\Users\USER\Documents\PythonScripts\Data.csv",header=None)
X

#Finding out the data type
type(x)#Why is my type a list whereas in the tutorial its a dataframe?

#Finding out the structure of the list by making it into a numpy array
import numpy as np
x=np.array(x)
x.shape

#Finding out info about the list
import pandas 
x.info()#Why is this not working?

#Finding out what is in the head of the csv file
x.head() #Why is this not displaying Maths,Eng, Swa as the head?

#Why is this reading the first row instead of the first column?
x[0]


# In[38]:

import pandas as pd
DSI_data=open(r'C:\Users\USER\Documents\PythonScripts\Data.csv')
DSI_reader=pd.read_csv(DSI_data)
print(DSI_reader)

#Finding out the data type
type(x)#Why is my type a list or numpy.ndarray whereas in the tutorial its a dataframe?

#Finding out the structure of the list by making it into a numpy array
import numpy as np
x=np.array(x)
x.shape

#Finding out info about the list
import pandas 
x.info()#Why is this not working?

#Finding out what is in the head of the csv file
x.head() #Why is this not displaying Maths,Eng, Swa as the head?

M=x.as_matrix() Not woriking coz its already a matrix/numpy array

#Why is this reading the first row instead of the first column? Because the data type is a numpy array.
#Numpy(array):x[0]-returns the 0th row
#Pandas(dataframe):x[0]-returns column that has name 0
#The datatype should be a dataframe for all the code that has errors so far to work
#Why is it not a dataframe?
x[0]

#Determining the data type of x[0]
type([0]) #Should be a series not a list or numpy array

#Pandas dataframes are for 2D objects.
#Pandas series are for 1D objects.

#How to get a pandas row
x.iloc[0]#I think it doesnt work coz its a numpy array or list not a pandas data frame

#Finding out the data type of a pandas row
type(x.iloc[0])#Doesnt work coz its a list

#Getting more than 1 column in pandas
x[[0,2]]#List indices must be integers or slices,not list

#Selecting specific roe based on some criteria eg filtering out all the row which have data in the 0th column being less than 5 
x[x[0]<5] #< is not supported between instances of 'list' and 'int'

#This code outputs the value of all the rows in the 0th column in form of boolean values 
x[0]<5 #Doesn't work here coz its a list





# In[ ]:




# In[ ]:



