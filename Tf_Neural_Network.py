
# coding: utf-8

# In[1]:


#Building a neural network using tensorflow
#Creating a session graph             
import tensorflow as tf
import numpy as np


# In[2]:


#Setting random seed values
np.random.seed(101)
tf.set_random_seed(101)


# In[3]:


#Creating random data values
rand_a=np.random.uniform(0,100,(5,5))
rand_a


# In[4]:


rand_b=np.random.uniform(0,100,(5,1))
rand_b


# In[7]:


#Creating placeholders for the random uniform objects
a=tf.placeholder(tf.float32)


# In[8]:


b=tf.placeholder(tf.float32)


# In[9]:


#Addition
add_op=a+b


# In[10]:


#Multiplication
mul_op=a*b


# In[15]:


#Creating sessions that use graphs with feed dictionaries to get results off of these operations
with tf.Session() as sess:
    add_result=sess.run(add_op,feed_dict={a:rand_a,b:rand_b})
    print(add_result)
    print('\n')
    
    mul_result=sess.run(mul_op,feed_dict={a:rand_a,b:rand_b})
    print(mul_result)


# # Example neural network

# In[16]:


#Number of features and neurons
n_features=10
n_dense_neurons=3


# In[17]:


#Placeholders
x=tf.placeholder(tf.float32,(None,n_features))


# In[28]:


#Variables
W=tf.Variable(tf.random_normal([n_features,n_dense_neurons]))
b=tf.Variable(tf.ones([n_dense_neurons]))


# In[29]:


#Operation and activation function
#Matrix multiplication
xW=tf.matmul(x,W)


# In[30]:


#Addition
z=tf.add(xW,b)


# In[31]:


#Activation function
a=tf.sigmoid(z)


# In[35]:


#Initializing the variables
init=tf.global_variables_initializer()

#Creating a session
with tf.Session() as sess:
    sess.run(init)
    
    layer_out=sess.run(a,feed_dict={x:np.random.random([1,n_features])})


# In[36]:


print(layer_out)


# # Simple Regression Example

# In[38]:


#data
x_data=np.linspace(0,10,10)+np.random.uniform(-1.5,1.5,10)


# In[39]:


x_data


# In[40]:


#Plotting out
y_label=np.linspace(0,10,10)+np.random.uniform(-1.5,1.5,10)
y_label


# In[42]:


import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
plt.plot(x_data,y_label,'*')


# y=mx+b

# In[43]:


#Initializing random values
np.random.rand(2)


# In[44]:


#Creating 2 random variables
m=tf.Variable(0.81)
b=tf.Variable(0.67)


# In[46]:


#Creating the cost function
error=0
for x,y in zip(x_data,y_label):
    y_hat=m*x+b #predicted value


# In[54]:


#Cost function to fix the randomness of m and b values-the cost function calculates the error
error+=(y-y_hat)**2 #this is the cost function-you square it in order to 'punish' higher errors

#Creating an optimizer to minimize the error
optimizer=tf.train.GradientDescentOptimizer(learning_rate=0.001)
train=optimizer.minimize(error)


# In[58]:


#Initializing variables
init=tf.global_variables_initializer()


# In[59]:


#Create the session and run it
with tf.Session() as sess:
    sess.run(init)
    
    training_steps=100
    
    for i in range(training_steps):
        
        sess.run(train)
        
    final_slope , final_intercept=sess.run([m,b])


# In[60]:


#Evaluating the results
x_test=np.linspace(-1,11,10)

#y=mx+b
y_pred_plot=final_slope*x_test+final_intercept #Explain this please
plt.plot(x_test,y_pred_plot,'r')
plt.plot(x_data,y_label,'*')


# In[ ]:





# In[ ]:




