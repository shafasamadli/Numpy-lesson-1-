#!/usr/bin/env python
# coding: utf-8

# # Numpy practicing 

# In[22]:


list1=[x*2 for x in range(2,27)]
print(list1)


# In[23]:


get_ipython().system('pip install names')
import names 
list3=[names.get_full_name() for x in range(10)]
print(list3)


# In[25]:


list4=[x for x in enumerate(list3,1)]  # enumerate requires iterable data type 
print(list4)


# In[29]:


import numpy as np 
np_array_1=np.array(list4)
print(np_array_1)
print(type(np_array_1)) # nd array it means that this type of list is numpy array


# In[35]:


np_array=np.array([1,2,3,4])
np_array_test=np.array(["Smith","Charles",2,True]) 
# Numpy contain just one type of data it means that if our list consists of int,string and bool type of elements numpy will convert all of them to string
print(np_array)
print(type(np_array))
print(np_array_test)


# In[45]:


np_array_2=np.arange(10) # create numpy array which the elements of array begin from 0 to 9. 
#The code block says that create a numpy array and it must be 10 elements 
print(np_array_2)


# In[46]:


np_array_3=np.arange(21)
print(np_array_3)


# In[50]:


a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(f"It is numpy array,\n {a} and type of it {type(a)}")
print(f"The elements which index is 2 {a[2]}")


# In[52]:


# A vector is an array with a single dimension (there’s no difference between row and column vectors)
# A matrix refers to an array with two dimensions. For 3-D or higher dimensional arrays, the term tensor is also commonly used.
# Dimensions are called axes


# In[53]:


# Create numpy array which all elements of this array will be zero and it is called zeros nd array
print(np.zeros(5)) # output shown as float


# In[54]:


print(np.zeros(10))


# In[55]:


# We also have ones numpy array or ndarray and all elements of this array is one
print(np.ones(7)) # again output will be float


# In[56]:


print(np.ones(12))


# In[57]:


# Sometimes we create empty ndarray  instead of zeros ndarray due to the speed factor
# This array consists of randomly numbers
print(np.empty(8))


# In[59]:


print(np.arange(20))


# In[60]:


print(np.arange(100,130))


# In[61]:


print(np.arange(125,180,5))


# In[64]:


print(np.linspace(5,30,4)) # bu function verilen araliqda neçə interval olmasina gore bolur ededleri
# yani burada 5 ve 12 arasinda 4 beraber yere bolunmesini isteyir. Ilk ve son yani serhed olmasi ucun yazdigimiz araliqdaki ededler (5,30) eyni qalir


# In[65]:


print(np.linspace(100,200,12))


# In[70]:


print(np.ones(5,dtype=np.int64)) # normally it must return float64 type of data however when we want to convert the type of it we can use this code part
print(np.zeros(12,dtype=np.int64))


# In[73]:


list_random=[19,24,3,10,15,30,43]
np_array_random=np.array(list_random)
print(np_array_random)
print(np.sort(np_array_random))


# In[74]:


np_array_5=np.array([19,24,3,10,15,30,43])
print(np.sort(np_array_5))


# In[80]:


b = np.array([[10,4],[3,1]]) # sort along the last axis, her setirdeki matricin ve ya vectorun icini sort edir 
np.sort(b)  


# In[81]:


np.sort(b, axis=None)  # sort the flattened array


# In[84]:


np.sort(b, axis=0)  # sort along the first axis


# In[87]:


nd_array_1=np.array([x for x in range(0,15)])
nd_array_2=np.array([y for y in range(20,35)])
print(nd_array_1)
print(nd_array_2)
# to execute this operation we must pay attention the shape of numpy arrays if they aren't equal we will face error
print(nd_array_1+nd_array_2) 


# In[92]:


nd_array_1=np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])
nd_array_2=np.array([20,21,22,23,24,25,26,27,28,29,30,31,32,33,34])
print(nd_array_1)
print(nd_array_2)
print(np.concatenate((nd_array_1,nd_array_2))) # pay attention the number of bracelets


# In[95]:


x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
print(np.concatenate((x,y)))
print(np.shape(np.concatenate((x,y))))


# In[97]:


np.concatenate((x, y), axis=0)
print(np.concatenate((x, y), axis=0))
print(np.shape(np.concatenate((x, y), axis=0)))


# In[107]:


# ndarray.ndim will tell you the number of axes, or dimensions, of the array
# sondaki moterizelerin sayina gore bilmek olar
array_example = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0 ,1 ,2, 3],
                           [4, 5, 6, 7]]])
print(array_example)
print(f"Dimension of array is: {array_example.ndim}")


# In[109]:


# ndarray.size will tell you the total number of elements of the array. This is the product of the elements of the array’s shape
array_example_1 = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0 ,1 ,2, 3],
                           [4, 5, 6, 7]]])
print(array_example_1)
print(f"Size of array is: {array_example_1.size}") # 6*4=24


# In[111]:


# ndarray.shape will display a tuple of integers that indicate the number of elements stored along each dimension of the array. If, for example, you have a 2-D array with 2 rows and 3 columns, the shape of your array is (2, 3)
array_example_2 = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0 ,1 ,2, 3],
                           [4, 5, 6, 7]]])
# print(array_example_2)
# shape of ndarray is also called as attribute of ndarray
print(f"Shape of array is: {array_example_2.shape}") # 3- dimension, 2-rows, 4-columns  row*column


# In[ ]:


# Note: The value before the comma specifies the row, the value after the comma specifies the column


# In[ ]:


# np.mean(ndarray)
# np.std(ndarray)
# np.median(ndarray)
# np.corrcoef(ndarray)
# gk_heights=np_heights[np_positions=='GK']
# other_heights=np_heights[np_positions!='GK']


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




