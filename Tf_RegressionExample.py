
# coding: utf-8

# In[1]:


#Regression example
#Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[2]:


import tensorflow as tf


# In[3]:


#data
x_data=np.linspace(0.0,10.0,1000000)


# In[4]:


#Random points
noise=np.random.randn(len(x_data))


# In[5]:


#Finding out the shape
noise.shape


# #The function that models the line
# y=mx+b
# b=5

# In[6]:


#Adding noise to make an imperfect line
y_true=(0.5*x_data)+5 + noise
#m=0.5,b=+5


# In[7]:


#Creating dataframes and concatenating them using pandas
x_df=pd.DataFrame(data=x_data,columns=['X data'])
y_df=pd.DataFrame(data=y_true,columns=['Y'])


# In[8]:


x_df.head()


# In[9]:


#Concatenating x and y data frames
my_data=pd.concat([x_df,y_df],axis=1)


# In[10]:


my_data.head()#The head part of the code samples out a few data points so as to make it easier to plot the values instead of actually plotting all the million values


# In[11]:


#Plotting out random sample values from the data created earlier
my_data.sample(n=250).plot(kind='scatter',x='X data',y='Y')


# In[12]:


#Using tensorflow to now try to make a perfect line that has a slope of 0.5 and intercepts at 5
#A million data points is too large to plot but necessary to train my neural network sufficiently so a solution is to divide the data points into batches of data
#Create a variable that holds batches of data
batch_size=8 #This holds 8 data points at a time but you can adjust it to any amount you want


# In[13]:


#Creating the m variable which is the slope and the b variable which is the intercept out of random values
np.random.randn(2)


# In[14]:


#The Variables
m=tf.Variable(0.85)
b=tf.Variable(1.50)


# In[15]:


#The Placeholders for x and y axis
xph=tf.placeholder(tf.float32,[batch_size])
yph=tf.placeholder(tf.float32,[batch_size])


# In[16]:


#Defining the graph - actual operations that are taking place
#Now, its creating a y_model that actual models out a perfect y=mx+b line
y_model=m*xph+b


# In[17]:


#Making a loss function
error=tf.reduce_sum(tf.square(yph-y_model))


# In[18]:


#Adding in the optimizer-Gradient Descent Optimizer
optimizer=tf.train.GradientDescentOptimizer(learning_rate=0.001)
train=optimizer.minimize(error)


# In[19]:


#Initializing the variables
init=tf.global_variables_initializer()


# In[20]:


#Creating and running the session
with tf.Session() as sess:
    sess.run(init)
    batches=1000
    for i in range(batches):
        
        #Random index- chooses 8 random index points to be part of each random batch being run
        rand_ind=np.random.randint(len(x_data),size=batch_size)
        
        #Adding in the feed dictionary that feeds data into the x and y placeholders
        feed={xph:x_data[rand_ind],yph:y_true[rand_ind]}
        
        #Running the session
        sess.run(train,feed_dict=feed)
        
        #Grabbing the slope m and intercept b placeholders
        model_m,model_b=sess.run([m,b])


# In[21]:


#new m
model_m


# In[22]:


#new b
model_b


# In[23]:


y_hat=x_data*model_m + model_b


# In[24]:


#Plotting
my_data.sample(250).plot(kind='scatter',x='X data',y="Y")
plt.plot(x_data,y_hat,'r')


# # Tf Estimator API

# In[25]:


import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[26]:


#Creating the feature columns list for the estimator
feat_cols=[tf.feature_column.numeric_column('x',shape=[1])]
estimator=tf.estimator.LinearRegressor(feature_columns=feat_cols)


# In[27]:


from sklearn.model_selection import train_test_split


# In[28]:


x_train,x_eval,y_train,y_eval=train_test_split(x_data,y_true,test_size=0.3,random_state=101)


# In[29]:


#Checking the shape of the training data (should be 70% of the total data)
x_train.shape


# In[30]:


#Checking the shape of the evaluation data (should be 30% of the total data)
x_eval.shape


# In[31]:


#Setting up the estimator inputs-input function that acts as the feed dictionary and batch size indicator all at once
input_func=tf.estimator.inputs.numpy_input_fn({'x':x_train},y_train,batch_size=8,num_epochs=None,shuffle=True)


# In[32]:


#Input function 2-for training
train_input_func=tf.estimator.inputs.numpy_input_fn({'x':x_train},y_train,batch_size=8,num_epochs=1000,shuffle=False)


# In[33]:


#Evaluation/test input function
eval_input_func=tf.estimator.inputs.numpy_input_fn({'x':x_eval},y_eval,batch_size=8,num_epochs=None,shuffle=True)


# In[34]:


#Training the estimator
estimator.train(input_fn=input_func,steps=1000)


# In[35]:


#Getting metrics on training data
train_metrics=estimator.evaluate(input_fn=train_input_func,steps=1000)


# In[36]:


#Evaluation_metrics
eval_metrics=estimator.evaluate(input_fn=eval_input_func,steps=1000)


# In[37]:


import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

#Training set metrics
print('TRAINING DATA METRICS')
print(train_metrics)


# In[38]:


#Comparing to the evaluation set metrics
print('EVAL METRICS')
print(eval_metrics)


# # How do I predict new values?

# In[39]:


#Use of new data that the model has never come across before
#New data
brand_new_data=np.linspace(0,10,10)
input_fn_predict=tf.estimator.inputs.numpy_input_fn({'x':brand_new_data},shuffle=False)


# In[40]:


#Using the predict method
estimator.predict(input_fn=input_fn_predict)
#To see the predicted values,its made into a list
list(estimator.predict(input_fn=input_fn_predict))


# In[41]:


#The predictions are currently dictionaries so to make them a list,create an empty list and append each to it
predictions=[]
for pred in estimator.predict(input_fn=input_fn_predict):
    predictions.append(pred['predictions'])


# In[42]:


#The list of predictions
predictions


# In[46]:


#Data samples on a graph in comparison to the predicted values
my_data.sample(n=250).plot(kind='scatter',x='X data',y='Y')
plt.plot(brand_new_data,predictions,'r*')


# In[ ]:




