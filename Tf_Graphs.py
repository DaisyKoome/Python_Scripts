
# coding: utf-8

# In[2]:


import tensorflow as tf


# In[3]:


#Creating constants which are integers and adding them
n1=tf.constant(1)


# In[4]:


n2=tf.constant(2)


# In[5]:


n3=n1+n2


# In[6]:


with tf.Session() as sess:
    result=sess.run(n3)


# In[7]:


print(result)


# In[8]:


#Creating a default graph
print(tf.get_default_graph)


# In[10]:


#Creating another graph
g=tf.Graph()


# In[13]:


#Setting the new graph to be the default graph
graph_one=tf.get_default_graph
print(graph_one)
graph_two=tf.Graph()
print(graph_two)


# In[17]:


with graph_two.as_default():
    print(graph_two is tf.get_default_graph())


# In[ ]:




