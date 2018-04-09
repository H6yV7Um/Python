# coding=utf-8
"""
Numpy: Python科学计算的基础库,重在数值计算,主要用于多维数组(矩阵)处理的库;用来存储和处理大型矩阵,比Python自身的嵌套列表结构要高效的多;本身是由C语言开发,是个很基础的扩展,Python其余的科学计算扩展大部分都是以此为基础;
高性能科学计算和数据分析的基础包
ndarray,多维数组(矩阵),具有矢量运算能力,快速、节省空间
矩阵运算,无需循环,可完成类似Matlab中的矢量运算
线性代数、随机数生成

Scipy: 基于Numpy提供了一个在Python中做科学计算的工具集,专为科学和工程设计的Python工具包;主要应用于统计、优化、整合、线性代数模块、傅里叶变换、信号和图像处理、常微分方程求解、稀疏矩阵等,在数学系或者工程系相对用的多一些,和数据处理的关系不大, 我们知道即可,这里不做讲解;
在NumPy库的基础上增加了众多的数学、科学及工程常用的库函数
线性代数、常微分方程求解、信号处理、图像处理
一般的数据处理numpy已经够用

ndarray(N Dimension Array)多维数组
NumPy数组是一个多维的数组对象(矩阵)，称为ndarray，具有矢量算术运算能力和复杂的广播能力，速度快且节省空间
ndarray的下标从0开始，且数组里的所有元素必须是相同类型
常用属性
ndim属性: 数组维度个数
shape属性: 数组维度大小
dtype属性: 数组中的数据类型

"""

import numpy as np
import matplotlib.pyplot as plt


"""
ndarray随机创建: 通过随机抽样numpy.random生成随机数据
"""

# 创建一个3*4(3行4列)的随机浮点型二维数组(二维数组里有3个一维数组,每个一维数组有4个元素),rand固定区间0.0~1.0
def rand():
    arr = np.random.rand(3, 4)
    print(arr)
    print(type(arr))  # <class 'numpy.ndarray'>
    print(arr.ndim)  # 2
    print(arr.shape)  # (3, 4)
    print(arr.dtype)  # float64

# 创建一个3*4(3行4列)的随机浮点型二维数组,uniform指定区间1.0~5.0
def uniform():
    arr = np.random.uniform(1, 5, (3, 4))
    print(arr)
    print(type(arr))  # <class 'numpy.ndarray'>
    print(arr.ndim)  # 2
    print(arr.shape)  # (3, 4)
    print(arr.dtype)  # float64

# 创建一个3*4*5(3个4行5列)的随机整型三维数组,randint指定区间1~10
def randint():
    arr = np.random.randint(1, 10, (3, 4, 5))
    print(arr)
    print(type(arr))  # <class 'numpy.ndarray'>
    print(arr.ndim)  # 3
    print(arr.shape)  # (3, 4, 5)
    print(arr.dtype)  # int32

# 创建一个符合正态分布的随机数抽样数组,数据个数是10000
def randn():
    arr = np.random.randn(10000)
    print(arr)
    print(type(arr))  # <class 'numpy.ndarray'>
    print(arr.ndim)  # 1
    print(arr.shape)  # (10000,)
    print(arr.dtype)  # float64
    plt.hist(arr, bins=100)  # bins参数表示正态分布图中柱子的个数
    plt.show()

"""
ndarray序列创建: 
"""

# 将list序列转换成数组
def array():
    l1 = range(10)
    l2 = list(range(10))
    print(l1)  # range(0, 10)
    print(l2)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # np.array(collection)可以将序列化的数据转换成数组;collection包含序列型对象(list)和嵌套序列对象(list of list)
    print(np.array(l1))  # [0 1 2 3 4 5 6 7 8 9]
    print(np.array(l2))  # [0 1 2 3 4 5 6 7 8 9]
    arr = np.array([l1, l2])
    print(arr)
    print(arr.ndim)  # 2
    print(arr.shape)  # (2, 10)
    print(arr.dtype)  # int32

# 创建一个3*4的二维数组,每个元素都是float64类型的0
def zeros():
    arr = np.zeros((3, 4))
    print(arr)


"""
ndarray数据类型: 
"""

if __name__ == "__main__":
    # rand()
    # uniform()
    # randint()
    # randn()
    # array()
    zeros()