
# coding: utf-8

# In[1]:


import tensorflow as tf


# In[2]:


sess=tf.InteractiveSession()


# In[3]:


my_tensor=tf.random_uniform((4,4),0,1)


# In[4]:


my_tensor


# In[5]:


my_var=tf.Variable(initial_value=my_tensor)


# In[6]:


print(my_var)


# In[9]:


init=tf.global_variables_initializer()


# In[10]:


sess.run(init)


# In[11]:


sess.run(my_var)


# In[12]:


ph=tf.placeholder(tf.float32)


# In[ ]:




