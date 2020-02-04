# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 13:45:13 2020

@author: zhoubo
"""



#%% Numpy中怎么找到数据中的nan的个数思路

import numpy as np
from numpy import nan

#需要先知道的先决知识

#2个nan是不相等的，可以进行布尔操作 np.nan ==np.nan  : False np.nan != np.nan  True nan和任何数操作还是nan



#找到nan的个数
#第一种方法：

#np.count_nonzero()这个函数可以计算数组中  非0  的个数

t1 =np.array([[3,3,3,3],
              [4,nan,6,7],
              [9,10,nan,11]])

print(t1)

print('非0个数：\n',np.count_nonzero(t1))

print(t1!=t1)#只有nan的位置   t1才!= t1 得到的是个bool数组

print('非0个数（恰好找到了nan的个数）:\n',np.count_nonzero(t1!=t1))#因为bool值 True为1 False为0，这样计算非0个数应该是1
#print(t1[t1!=t1])#访问true位置的索引可以取到nan位置
#--------------------------------------------------------------------------------------------------------

#第二种方法：
#np.isnan()    相当于上面t1！=t2

print(np.isnan(t1))
#同样的思路计算 bool矩阵中非0个数，恰好就反应了nan的个数
print(np.count_nonzero(np.isnan(t1)))


#%% Numpy统计方法
import numpy as np
from numpy import nan

t1 =np.array([[3,3,3,3],
              [4,nan,6,7],
              [9,10,nan,11]])

t2 =np.arange(12).reshape(3,4)

#直接替换成0不合适！
#把Nan替换成/均值中值，或者删除含nan的一行/列(不是非常推荐不是完美选择)
print(t1.dtype) 

#求和
print(np.sum(t1,axis =0))#行元素的列方向求sum


#求均值
print(np.mean(t1,axis =0))

#求中值/中位数
print('中位数：\n',np.median(t1))#要是有nan会没法计算出中位数#汇报warning

#最大/最小值
print('最大值\n',t1.max(axis =0))

#极值
print('极值：\n',np.ptp(t2,axis =0))

#标准差
print('标准差：\n',t2.std(axis =0))#标准差越大越离散，越小越稳定




















