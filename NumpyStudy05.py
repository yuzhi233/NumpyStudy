# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 14:20:58 2020

@author: zhoubo
"""

#%% -------------------Numpy中数值的修改--------------
import numpy as np

t =np.arange(24).reshape((4,6))
print(t<10)#t中大于10  bool类型的数组

print(t[t<10])#打印索引符合t>10的数组

print(type(t[t<10]))#type是ndarray
t[t<10] = 0 #将t中t<10的数值改为0
print(t)
t[t>10] =10#将t中t>10的数值改为10
print(t)

print('-'*40)

#还可以用np.where()  类比与python中三元运算符 a =3 if 3>2 else 4

t2 =np.arange(24).reshape((4,6))
print('t2\n',t2)
 
print('t2替换后:\n',np.where(t2<10,0,1))#把t2<10的数替换成0，否则替换成1



#如果想把t2中小于10的数替换成10大于20的数替换成20 怎么做？
#Numpy中的clip()操作 裁剪操作
print(t2.clip(10,20))#clip()就是小于10的替换成10，大于20的替换成20

print(t2.dtype)#t2是int32

t2 = t2.astype(float)
t2[3,3] =np.nan#nan是浮点类型
print(t2)


#%%------------------------------Numpy数组的拼接---------------------

import numpy as np
#np.vstack()竖直拼接和np.hstack()水平拼接   以后的水平拼接和竖直分割跟这个类似

t1 =np.array([[1,2,3,4,5],
              [6,7,8,9,10]])
t2 =np.array([[1,1,1,1,1],
             [2,2,2,2,2]])

print('t1:\n',t1)
print('t2:\n',t2)
print('竖直拼接:\n',np.vstack( t1,t2 ))
print('水平拼接:\n',np.hstack((t1,t2)))

#交换数据的行列

#行交换&列交换

t3 =np.arange(24).reshape((6,4))
print('t3:\n',t3)

#行交换 交换1和3行
t3[[0,2],:]= t3[[2,0],:]
print('1行和3行进行交换:\n',t3)

#列交换 同理
t3[:,[0,2]] = t3[:,[2,0]]
print('第1列跟第3列交换:\n',t3)


