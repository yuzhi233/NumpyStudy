# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 16:51:26 2020

@author: zhoubo
"""
#%%   数组的形状 shape
import numpy as np

t1 = np.arange(12)

#print(t1)
print(t1.shape)#t1是一个元组  如果是1维度  就是数组元素个数

t2 =np.array([[1,2,3],[4,5,6]])
#print(t2)
print(t2.shape)  #2行3列
#%% 3维度数组
import numpy as np

t3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
_t3 =np.array([[[1,2,3],[4,5,6]],[[7,8,8],[10,11,12]],[[1,2,3],[4,5,6]]])

print('t3:\n',t3)
print('-----------------')
print('t3.shape =',t3.shape)
print('*****************************')

print('_t3\n',_t3)
print('_t3.shape =',_t3.shape)#看打印结果注意 区别！  #显然 (3,2,3)分别代表 3块数据 ，每块数据2行3列


#%%----------------------------修改形状reshape()-------------------------------
import numpy as np

t4 = np.arange(12)#生成12个数0-11
print(t4)
t4_reshape = t4.reshape(3,4)# 注意12=3*4
print(t4_reshape)
#拿t4_reshape 为例子 获取行数列数
row,col =(t4_reshape.shape[0],t4_reshape.shape[1])
print(row,col)
print('---------------------------------------------------------------------\n---------------------------------------------------------------------')


t5 =np.arange(24)
print('t5_生成1d:\n',t5)

#将24个数reshape成 3个（2*4）
t5 =t5.reshape((3,2,4))#再体会一下24 =3*2*4 里面也可以不加括号 反正不加括号默认就是元组
print ('t5_变成3，2，4后:\n',t5)


#假设 想让t5再变回1维度
t5 =t5.reshape((24,))  #注意传入的是一个元组
print('t5_变回1d后:\n',t5)

#%%------------------还有个方法flatten()将高维度数组展开成一维------------------------

#先生成个2D数组
t_2d = np.arange(0,12).reshape(3,4)
print('t_2d:\n',t_2d)
#用flatten()方法将其展开成1d
t_2d_to_1d = t_2d.flatten()
print('t_2d_to_1d:\n',t_2d_to_1d)

#生成个3D的
t_3d =np.arange(0,24).reshape(4,3,2)
print('t_3d:\n',t_3d)
t_3d_to_1d = t_3d.flatten()
print('t_3d_to_1d',t_3d_to_1d)










