# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 13:23:53 2020

@author: zhoubo
"""
import numpy as np
a =np.array([[3,2,1],
             [3,1,2],
             [2,3,1]])
print(a.shape)
max_index =np.argmax(a,axis =0)
print(max_index) #预计按axis =0结果是 [0,2,1]  按axis =1 的话结果是[0,0,1]

#猜测正确 为了跟前面不记混 [行,列]  这样记：
#二维度数组 axis =0 意思是沿着行元素的列方向进行操作  axis =1 沿着列元素的行方向进行操作




#下面是百度的，方便理解

#如果axis=0，则沿着纵轴进行操作，若axis=1则沿着横轴进行操作。但是这只是仅仅对于二维数组而言。
#但是可以总结为一句话：设axis=i ,则numpy沿着第i个下标变化的方向进行操作
#axis=0,首先来看一下，arr的0轴在哪里，a的shape为（3,3），a的shape下标为(0,1),
#则axis=0对应于数组shape下标的的第一个位置。 