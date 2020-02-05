# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 11:07:49 2020

@author: zhoubo
"""
import numpy as np

#-----------------------Numpy更多好用的方法--------------------------------------------

# np.ones(),np.zeros(),np.eye()

t1 =np.ones((2,3))#创建都是1的
t2 =np.zeros((2,3))#创建都是0的数组
t3 =np.eye(10)#单位矩阵10*10

print('t3',t3)
#np.argmax()返回参数最大值位置的索引值
max_index =np.argmax(t3,axis=0)
print('t3,max index:\n',max_index)

#Numpy生成随机数

#np.random 下的方法 rand()，randn()，randint()，seed()
t4 =np.random.randn(2,3,4)#标准正态分布
print(t4)



t5 =np.random.uniform(0,11,(2,3))#产生从0-10，2行3列均匀分布的随机数的数组
print('均匀分布t5：\n',t5)


t6 = np.random.seed(10)#添加随机种子后以后随机产生的都说固定的了，每次运行结果不会变的产生一次的
t6 =np.random.randint(0,11,(2,3))
print(t6)


#%%Numpy的copy() 
import numpy as np


#例子 b=a 和b=a[:]区别
a=[1,2,3]
b=a

a.append(4)
print(a,id(a))
print(b,id(b))
print(a is b)
#id()函数用于获取对象的内存地址
c=[1,1,1]
d =c[:]
c.append(0)
print(c,id(c))
print(d,id(d))
print(c is d)

#你品 你细品
#python中的copy()
e =[2,2,2]
f=e.copy()
print(e,id(e))
print(f,id(f))

g = np.array([1,3,4])
h =g.copy()
print(h is g)