# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 12:50:36 2020

@author: zhoubo
"""

#%% Numpy数组中nan替换成均值

import numpy as np

t1 =np.arange(12).reshape(3,4).astype('float')#nan的type是float
t1[1,2:] =np.nan#将第2行第2-最后 列
print(t1)

for i in range(t1.shape[1]):#按列来循环 t1 是4列循环4次
    temp_col =t1[:,i]  #拿出t1第i列 赋值给temp_col
    nan_num = np.count_nonzero(np.isnan(temp_col))#计算nan的个数 存到nan_num里
    if nan_num != 0:#如果nan个数不为0 下面要将nan替换成列均值↓
        temp_notnan_col = temp_col[temp_col == temp_col]#将这一列非nan的数字拿出来存到temp_nonan_col里  temp_col == temp_col是bool数组 索引找到非nan数组
        temp_col[np.isnan(temp_col)] =temp_notnan_col.mean()#   temp_col[np.isnan(temp_col)] 是索引到nan的位置 并替换成列均值
    
print(t1)