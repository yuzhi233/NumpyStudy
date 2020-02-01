# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 18:03:38 2020

@author: zhoubo
"""

import numpy as np 

#数组计算

#加减乘除是对应元素操作
t1 =np.arange(12).reshape(3,4)
print('t1=:\n',t1)
print('t1*2 =:\n',t1*2)

#尤其注意除法

#t1/0
# print('t1/0=:\n',t1/0)#竟然能计算 返回值有 nan（not a number) 和 inf无穷  (infinite)

t2 =np.arange(3).reshape(3,1)
print('t2=\n',t2)
print('t1-t2=:\n',t1-t2)#因为在列维度上是一致的所以可以操作 分别对每列操作  （看形状跟哪种相似就对那个维度操作)

t3 =np.arange(9).reshape(3,3)
print('t3=:\n',t3)

print(t3-t2)

#总结:要想行列进行计算 你至少得有形状相似的地方啊，不然算个毛啊
#能不能计算判断比较麻烦，，碰到了复杂的再说吧。。3d以下比较好判断