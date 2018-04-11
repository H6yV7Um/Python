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
rand(): 创建一个3*4的随机浮点型二维数组(二维数组里有3个一维数组,每个一维数组有4个元素),rand固定区间0.0~1.0
uniform(): 创建一个3*4的随机浮点型二维数组,uniform指定区间1.0~5.0
randint(): 创建一个3*4*5的随机整型三维数组,randint指定区间1~10
randn(): 创建一个符合正态分布的随机数抽样数组,数据个数是10000
"""

def rand():
    arr = np.random.rand(3, 4)
    print(arr)
    print(type(arr))  # <class 'numpy.ndarray'>
    print(arr.ndim)  # 2
    print(arr.shape)  # (3, 4)
    print(arr.dtype)  # float64

def uniform():
    arr = np.random.uniform(1, 5, (3, 4))
    print(arr)
    print(type(arr))  # <class 'numpy.ndarray'>
    print(arr.ndim)  # 2
    print(arr.shape)  # (3, 4)
    print(arr.dtype)  # float64

def randint():
    arr = np.random.randint(1, 10, (3, 4, 5))
    print(arr)
    print(type(arr))  # <class 'numpy.ndarray'>
    print(arr.ndim)  # 3
    print(arr.shape)  # (3, 4, 5)
    print(arr.dtype)  # int32

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
np.array(): 将list转换成数组
np.zeros(): 创建一个3*4的二维数组,每个元素都是float64类型的0
np.ones(): 创建一个3*4的二维数组,每个元素都是float64类型的1
np.empty(): 创建一个3*4的二维数组,每个元素都是内存里的随机值
np.arange(): 创建一个区间为0~n的一维数组,类似python的range()
reshape(): 重组原数组并调整形状(维度)
shuffle(): 打乱数组(洗牌)
"""

def array():
    l1 = range(10)
    l2 = list(range(10))
    print(l1)  # range(0, 10)
    print(l2)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # np.array(collection)可以list转换成数组;collection包含序列型对象(list)和嵌套序列对象(list of list)
    print(np.array(l1))  # [0 1 2 3 4 5 6 7 8 9]
    print(np.array(l2))  # [0 1 2 3 4 5 6 7 8 9]
    arr = np.array([l1, l2])
    print(arr)
    print(arr.ndim)  # 2
    print(arr.shape)  # (2, 10)
    print(arr.dtype)  # int32

def zeros():
    arr = np.zeros((3, 4))
    print(arr)

def ones():
    arr = np.ones((3, 4))
    print(arr)

def empty():
    arr = np.empty((3, 4))
    print(arr)

def arange():
    arr = np.arange(15)
    print(arr)  # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]

def reshape():
    arr = np.arange(15)
    # 将15个元素的一维数组重组成二维数组,二维数组有3个一维数组,每个一维数组5个元素
    arr1 = arr.reshape(3, 5)
    # 将15个元素的一维数组重组成三维数组,三维数组有1个二维数组,每个二维数组有3个一维数组,每个一维数组5个元素
    arr2 = arr.reshape(1, 3, 5)
    print(arr1)
    print(arr2)

def shuffle():
    arr = np.arange(15)
    print(arr)  # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]
    # 注意: 是给原数组洗牌,并没有return新数组
    np.random.shuffle(arr)
    print(arr)  # [ 7  2  0  9 10 14  8  5 12 11 13  3  1  6  4]
    arr1 = arr.reshape(3, 5)
    print(arr1)

"""
ndarray的数据类型: 
dtype: 指定/查看数组的数据类型,类型名+位数: float64, int32
astype: 转换数组的数据类型
"""

def dtype():
    arr = np.ones((3, 4))
    print(arr)
    print(arr.dtype)  # float64
    arr1 = np.ones((3, 4), dtype=int)
    print(arr1)
    print(arr1.dtype)  # int32

def astype():
    arr = np.ones((3, 4))
    print(arr)
    print(arr.dtype)  # float64
    arr1 = arr.astype(int)
    print(arr1)
    print(arr1.dtype)  # int32

    # 转换float64为int32时,是取整不是四舍五入,比如5.69063769-->5  -3.80322353-->-3
    arr2 = np.random.uniform(-10, 10, (3, 4))
    print(arr2)
    print(arr2.dtype)
    arr3 = arr2.astype(int)
    print(arr3)
    print(arr3.dtype)

if __name__ == "__main__":
    # rand()
    # uniform()
    # randint()
    # randn()
    # array()
    # zeros()
    # ones()
    # empty()
    # arange()
    # reshape()
    # shuffle()
    # dtype()
    astype()