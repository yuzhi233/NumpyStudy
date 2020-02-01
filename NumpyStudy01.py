# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 10:56:27 2020

@author: zhoubo
"""

#numpy是python中的科学计算基础库





#%%--------------------------使用numpy生成数组，得到ndarray类型--------------------------------------------------
import numpy as np

#方法1
t1 = np.array([1,2,3])
print(t1)
# print (type(t1))  # ndarray (n-dimension)array 

#方法2
t2 = np.array(range(10))

#方法3  这个利用numpy里的arange()方法 比上面方便点 类似于python的range()
t3 =np.arange(0,10,2)
print(t3)
print(t3.dtype)# dtype是属性


#%%-----------------------------------umpy中数据类型-----------------------------------------------------------
import numpy as np

t4= np.array(range(1,4),dtype = np.float32) #t4= np.array(range(1,4),dtype =float)  
print(t4)
print(t4.dtype)
print('*'*50)

t5 =np.array([1,0,0,0,1],dtype = bool)
print(t5)
print(t5.dtype)


#调整已经生成的数据类型 astype()
t6 = t5.astype('i1')
print(t6.dtype)

#numpy中的小数
import random


#生成一个10个小数的列表
float_list =[random.random()for i in range(10)]
print(type(float_list[0]))#list这里默认的数据类型是float

#----------------------问题：python内置函数怎么保存想要位数的小数？------------------------------
#random.random()返回0-1的随机小数

t7 = [round(random.random(),2) for i in range(5)]#保留2位 #t7 = np.array([round(random.random(),2) for i in range(5)])

#numpy有自己的方法 np.round()  
t8 = np.array(float_list)
t8 =np.round(t8,2)



