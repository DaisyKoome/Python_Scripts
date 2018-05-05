
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


#Creating a data frame called diabetes to contain a csv data file
diabetes=pd.read_csv('pima-indians-diabetes.csv')


# In[3]:


diabetes.head()


# In[4]:


#Cleaning (Normalising) the data
#List of columns
diabetes.columns


# In[5]:


#Creating a list of columns to normalise
cols_to_norm=['Number_pregnant', 'Glucose_concentration', 'Blood_pressure', 'Triceps',
       'Insulin', 'BMI', 'Pedigree']


# In[6]:


#Normalising using pandas
#Using a custom function
diabetes[cols_to_norm]=diabetes[cols_to_norm].apply(lambda x:(x-x.min())/(x.max()-x.min()))


# In[7]:


diabetes.head()


# In[8]:


#Creating feature columns
import tensorflow as tf


# In[9]:


diabetes.columns


# In[10]:


#Split the columns into numeric columns and feature columns by creating a new variable for each column
#Creating a for loop for that
columns=['Number_pregnant', 'Glucose_concentration', 'Blood_pressure', 'Triceps',
       'Insulin', 'BMI', 'Pedigree', 'Age']
for column in columns:
    print("tf.feature_column.numeric_column "+ ('')+(column))
    


# In[11]:


num_preg=tf.feature_column.numeric_column('Number_pregnant')
plasma_gluc=tf.feature_column.numeric_column('Glucose_concentration')
dias_press=tf.feature_column.numeric_column('Blood_pressure')
tricep=tf.feature_column.numeric_column('Triceps')
insulin=tf.feature_column.numeric_column('Insulin')
bmi=tf.feature_column.numeric_column('BMI')
diabetes_pedigree=tf.feature_column.numeric_column('Pedigree')
age=tf.feature_column.numeric_column('Age')


# In[12]:


#Categorical features(non-continuous values)
#Using a vocabulary list-preferable for a category with few options
assigned_group=tf.feature_column.categorical_column_with_vocabulary_list('Group',['A','B','C','D'])


# In[13]:


#Using a hash-bucket-when the categorical column has many options
#assigned_group=tf.feature_column.categorical_column_with_hash_bucket('Group',hash_bucket_size=10)


# In[14]:


#Converting a continuous column into a categorical column (feature engineering)
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[15]:


#A histogram showing the ages in the data
diabetes['Age'].hist(bins=20)


# In[16]:


#Taking the continuous ages and bucketing them into categories for example decade-wise
age_bucket=tf.feature_column.bucketized_column(age,boundaries=[20,30,40,50,60,70,80])


# In[17]:


#A list of the feature columns
feat_cols=[num_preg,plasma_gluc,dias_press,tricep,insulin,bmi,diabetes_pedigree,assigned_group,age_bucket]


# In[18]:


#Performing a train test split
x_data=diabetes.drop('Class',axis=1)
x_data.head()


# In[19]:


labels=diabetes['Class']


# In[20]:


labels


# In[21]:


#Train-test split
from sklearn.model_selection import train_test_split


# In[22]:


X_train,X_test,y_train,y_test=train_test_split(x_data,labels,test_size=0.3,random_state=101)


# In[23]:


#Creating an input function
import tensorflow as tf
import pandas as pd
input_func=tf.estimator.inputs.pandas_input_fn(x=X_train,y=y_train,batch_size=10,num_epochs=1000,shuffle= True)


# In[24]:


#Creating the model
model=tf.estimator.LinearClassifier(feature_columns=feat_cols,n_classes=2)


# In[25]:


#Training the model
model.train(input_fn=input_func,steps=1000)


# In[26]:


#Evaluating the model
#Creating the input function for evaluation
eval_input_func=tf.estimator.inputs.pandas_input_fn(x=X_test,y=y_test,batch_size=10,num_epochs=1,shuffle=False)


# In[27]:


#Calling the evaluate function
results=model.evaluate(eval_input_func)


# In[28]:


#The results of the evaluation
results


# In[29]:


#Getting predictions
pred_input_func=tf.estimator.inputs.pandas_input_fn(x=X_test,batch_size=10,num_epochs=1,shuffle=False)


# In[30]:


#Calling the predict function
predictions=model.predict(pred_input_func)


# In[31]:


#Storing the predictions as a list
my_pred=list(predictions)


# In[32]:


#Output of the predictions
my_pred


# In[33]:


#How to do a dense neural network classification (using DNN classifier)
#In the hidden units part,feed in how many neurons you want in how many layers
dnn_model=tf.estimator.DNNClassifier(hidden_units=[10,10,10],feature_columns=feat_cols,n_classes=2)


# In[34]:


#Trying to use the input function created earlier with the dense neural network created gives errors because the feature columns need to be made into embedded columns
dnn_model.train(input_fn=input_func,steps=1000)


# In[35]:


#Creating an embedded column from a categorical column
embedded_group_col=tf.feature_column.embedding_column(assigned_group,dimension=4)


# In[36]:


#Reset the feature columns by replacing the categorical column 'assigned group' with the embedded column just created from it
feat_cols=[num_preg,plasma_gluc,dias_press,tricep,insulin,bmi,diabetes_pedigree,embedded_group_col,age_bucket]


# In[37]:


#Creating the input function again
input_func=tf.estimator.inputs.pandas_input_fn(X_train,y_train,batch_size=10,num_epochs=1000,shuffle=True)


# In[43]:


#Creating the DNN model again
dnn_model=tf.estimator.DNNClassifier(hidden_units=[10,20,20,20,10],feature_columns=feat_cols,n_classes=2)


# In[44]:


#Training the DNN model
dnn_model.train(input_fn=input_func,steps=1000)


# In[45]:


#After training,now the model is evaluated
#Creating the evaluation input function
eval_input_func=tf.estimator.inputs.pandas_input_fn(x=X_test,y=y_test,batch_size=10,num_epochs=1,shuffle=False)


# In[46]:


#Calling the evaluate function
dnn_model.evaluate(eval_input_func)


# In[ ]:





# In[ ]:




