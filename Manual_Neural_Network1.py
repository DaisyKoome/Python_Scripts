
# coding: utf-8

# In[54]:

#Manually making a neural network
#Creating a function that says hello
class SimpleClass():
    def __init__(self,name):
        print("hello "+name)


# In[55]:

#Checking the datatype
s="world"
type (s)


# In[70]:

#Caliing the function
x= SimpleClass('name')


# In[67]:

#Creating another funtion that prints 'yelling'
class SimpleClass():
    def __init__(self,name):
        print("hello "+name)

    def yell(self):
        print("YELLING")


# In[71]:

#Trying out both functions:
#Trying out the hello function
x=SimpleClass('name')


# In[72]:

#Trying out the yell function
x.yell()


# In[73]:

#Creating another class called ExtendedClass that incorporates the SimpleClass
class ExtendedClass(SimpleClass):
    
    def __init__(Self):
        print("EXTEND!")

#Testing the new class
y=ExtendedClass()    


# In[74]:

#Testing the attachment of the new class to the functions in the initial class
y.yell()


# In[75]:

#How to make this special init method in the SimpleCLS also execute within the ExtendedClass class using the super keyword
class ExtendedClass(SimpleClass):
    
    def __init__(Self):
        
        super().__init__('Jose')
        print("EXTEND!")
        
#Testing whether it works:
y=ExtendedClass()


# In[23]:

#Operation class code
class Operation():
    
    def __init__(self,input_nodes=[]):
        
        self.input_nodes=input_nodes
        self.output_nodes=[]
        
        for node in input_nodes:
            node.output_nodes.append(self)
        
        #The following code creates a connection between the operations,variables,placeholders and the graph objects
        _default_graph.operations.append(self)
            
    def compute(self):
        pass


# In[72]:

#Creating example operations
#For addition
class add(Operation):
    
    def __init__(self,x,y):
        
        super().__init__([x,y])
        
    def compute(self,x,y):
        self.inputs=[x,y]
        return x + y


# In[73]:

#For multiplication
class multiply(Operation):
    
    def __init__(self,x,y):
        
        super().__init__([x,y])
        
    def compute(self,x,y):
        self.inputs=[x,y]
        return x * y


# In[85]:

#For matrix multiplication
class add(Operation):
    
    def __init__(self,x,y):
        
        super().__init__([x,y])
        
    def compute(self,x,y):
        self.inputs=[x,y]
        return x + y


# In[86]:

#Placeholders,graphs and variables
#Placeholder-an 'empty' node that needs a value to be provided as input so as to compute output.
#Variables-changeable parameters of the graph
#Graph-global variable connecting variables and placeholders to operations

#Placeholder class code
class Placeholder:
    def __init__(self):
        
        self.output_nodes=[]
        
        #The following code creates a connection between the operations,variables,placeholders and the graph objects
        _default_graph.placeholders.append(self)


# In[87]:

#Variables class code
class Variable():
    
    def __init__(self,initial_value=None):
        
        self.value=initial_value
        self.output_nodes=[]
        
        #The following code creates a connection between the operations,variables,placeholders and the graph objects
        _default_graph.placeholders.append(self)


# In[88]:

#Graph class code
class Graph():
    
    def __init__(self):
        
        self.operations=[]
        self.placeholders=[]
        self.variables=[]
        
    def set_as_default(self):
        
        #The following code makes the graph class global so that there is a link between the graph,placeholders,varaiables and operations objects
        global _default_graph
        _default_graph=self


# #How can I make this cell a textbox?
# #Example variables and placeholders for the graph
# z=Ax+b
# 
# A=10
# 
# b=1
# 
# z=10x+1

# In[89]:

g=Graph()


# In[90]:

g.set_as_default()


# In[91]:

A=Variable(10)


# In[92]:

b=Variable(1)


# In[93]:

x=Placeholder() #To be defined by the user


# In[94]:

y=multiply(A,x)


# In[95]:

z=add(y,b)


# In[96]:

#Create a traverse post order function-does a PostOrder tree traversal of nodes which makes sure that computation is done in the correct order
#Create a Session class that actually creates the graph

def traverse_postorder(self):

#PostOrder taversal of nodes-This makes sure computations are done in the correct order (Ax first, then Ax+b)

    nodes_postorder=[]
    
    def recurse(node):
        if isinstance(node, Operation):
            for input_node in node.input_nodes:
                recurse(input_node)
            nodes_postorder.append(node)
            
    recurse(operation)
    return nodes_postorder


# In[97]:

class Session():
    
    def run(self,operation,feed_dict={}):
        
        nodes_postorder=traverse_postorder(operation)
        for node in nodes_postorder:
            if type(node)==Placeholder:
                node.output=feed_dict[node]
            elif type(node)==Variable:
                    node.output=node.value
            else:
                #its an operation if not a placeholder or varaiable so
                node.inputs=[input_node.output for input_node in nodes.input_nodes]
                node.output=node.compute(*node.inputs)
            
            if node.output==list:
                node.output=np.array(node.output)
        
        return operation.output            
                


# In[98]:

sess= Session()


# In[102]:

result=sess.run(Operation=z,feed_dict=({x:10})


# In[ ]:

#Trying out matrix multiplication 
g=Graph()
g.set_as_default()
A=Variable([[[10,20],[30,40]])
b=Variable([1,2])
            
x=Placeholder()
y=matmul(A,x)
z=add(y,b)       


# In[1]:

sess= Session()


# In[2]:

sess.run(operation=z,feed_dict={x:10})


# In[5]:

#Classification #How can I make this bold or larger font or a textbox?
#Activation function
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

def sigmoid(z):
    return 1/(1+np.exp(-z))      


# In[6]:

sample_z=np.linspace(-10,10,100)
sample_a=sigmoid(sample_z)


# In[7]:

plt.plot(sample_z,sample_a)
plt.show()
#How comes the graph works while the code isnt working?


# In[9]:

class Sigmoid(Operation):
    def __init__(self,z):
        
        super().__init__([z])
        
    def compute(self,z_val):
       return 1/(1+np.exp(-z_val)) 
        


# In[10]:

from sklearn.datasets import make_blobs


# In[11]:

data=make_blobs(n_samples=50,n_features=2,centers=2,random_state=75)


# In[12]:

data


# In[14]:

type(data)


# In[16]:

data[1]


# In[21]:

features=data[0]
labels=[1]
plt.scatter(features[:,0],features[:,1],cmap='coolwarm') #Why doesnt the code for color work? c=labels


# In[23]:

x=np.linspace(0,11,10)
y=-x+5
plt.scatter(features[:,0],features[:,1],cmap='coolwarm')
plt.plot(x,y)


# In[24]:

#(1,1)*f-5=0
np.array([1,1]).dot(np.array([[8],[10]]))-5


# In[25]:

np.array([1,1]).dot(np.array([[2],[-10]]))-5


# In[28]:

g=Graph()
g.set_as_default()
x=Placeholder()
w=Variable([1,1])
b=Variable(-5)
z=add(matmul(w,x),b)
a=Sigmoid(z)

sess=Session()
sess.run(operation=a,feed_dict={x:[8,10]})


# In[ ]:



