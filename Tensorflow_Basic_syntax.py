
# coding: utf-8

# In[1]:


import tensorflow as tf
print (tf.__version__)


# In[ ]:


#Basic tensorflow syntax
import tensorflow as tf
hello=tf.constant("Hello ")


# In[4]:


#Creating constants using tensorflow
world=tf.constant("world")


# In[5]:


type(hello)


# In[6]:


print(hello)


# In[8]:


#Creating a session so that we can print a statement
with tf.Session() as sess:
    result=sess.run(hello+world)


# In[10]:


print(result)


# In[11]:


#Creating constants that are integers
a=tf.constant(10)


# In[12]:


b=tf.constant(20)


# In[13]:


#Finding out the data type
type(a)


# In[14]:


#Attempting to add without first creating a session
a+b


# In[16]:


#Creating a session so that we can add
with tf.Session() as sess:
    result=sess.run(a+b)


# In[17]:


#Outputing the result
result


# In[18]:


#Constant operation for a constant number
const=tf.constant(10)


# In[19]:


#A filled out matrix-you give dimensions of the matrix and the values
fill_mat=tf.fill((4,4),10)


# In[20]:


#A 4*4 matrix made up of zeros
myzeros=tf.zeros((4,4))


# In[21]:


#A 4*4 matrix amde up of ones
myones=tf.ones((4,4))


# In[22]:


myrandn=tf.random_normal((4,4),mean=0,stddev=1.0)


# In[24]:


myrandu=tf.random_uniform((4,4),minval=0,maxval=1)


# In[25]:


myzeros


# In[28]:


my_ops=[const,fill_mat,myzeros,myones,myrandn,myrandu]


# In[31]:


#Creating an interactive session which allows you to call it throughout multiple cells
sess=tf.InteractiveSession()
for op in my_ops:
    print(sess.run(op))
    print("\n")


# In[32]:


#Creating an interactive session which allows you to call it throughout multiple cells
sess=tf.InteractiveSession()
for op in my_ops:
    #Using eval instead of sess.run
    print(op.eval())
    print("\n")


# In[34]:


#Creating a 2*2 matrix
a=tf.constant([[1,2],
               [3,4]])


# In[35]:


#Finding out the shape in terms of dimensions
a.get_shape()


# In[37]:


#Creating a 2*1 matrix
b=tf.constant([[10],[100]])


# In[39]:


#Finding out the shape in terms of dimensions
b.get_shape()


# In[40]:


#Doing a matrix multiplication
result=tf.matmul(a,b)
sess.run(result)


# In[41]:


#Using eval instead of sess.run
result.eval()


# In[ ]:




