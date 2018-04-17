# coding=utf-8
"""
Pandas是一个强大的分析结构化数据的工具集,基于NumPy构建,提供了高级数据结构和数据操作工具
一个强大的分析和操作大型结构化数据集所需的工具集
基础是NumPy,提供了高性能矩阵的运算
提供了大量能够快速便捷地处理数据的函数和方法
应用于数据挖掘,数据分析
提供数据清洗功能

Pandas两大数据结构:
Series: 类似一维数组的对象,由数据和索引组成,索引是自动创建的
DataFrame: 表格型数据结构(如excel),每列数据可以是不同类型,索引包括列索引和行索引
"""

import numpy as np
import pandas as pd

"""
创建Series对象: ser = pd.Series(list/dict)
"""

def series01():
    # 通过list创建series,不指定行索引,默认是自增长的int类型
    ser = pd.Series(range(10, 20))
    print(ser)
    # 0    10
    # 1    11
    # 2    12
    # 3    13
    # 4    14
    # 5    15
    # 6    16
    # 7    17
    # 8    18
    # 9    19
    # dtype: int64

    # 查看索引
    print(ser.index)  # RangeIndex(start=0, stop=10, step=1)

    # 查看数据
    print(ser.values)  # [10 11 12 13 14 15 16 17 18 19]

    # 查看Series对象的元素的数据类型
    print(ser.dtype)  # int64
    print(ser.dtypes)  # int64

    # 查看Series对象的数据类型
    print(type(ser))  # <class 'pandas.core.series.Series'>

    # 根据索引获取值
    print(ser[2])  # 12

    # 默认查看series对象的前/后5条数据
    print(ser.head())
    print(ser.tail())
    # 指定查看series对象的前3条数据
    print(ser.head(3))

def series02():
    # 通过dict创建series
    ser = pd.Series({"a": 11.1, "b": 22.2, "c": 33.3})
    print(ser)
    # a    11.1
    # b    22.2
    # c    33.3
    # dtype: float64
    print(ser.head(2))
    # a    11.1
    # b    22.2
    # dtype: float64

    # name属性: 对象名-->ser.name 对象索引名-->ser.index.name
    print(ser.name)  # None
    ser.name = "haha"
    print(ser.name)  # haha
    print(ser.index.name)
    ser.index.name = "xixi"  # None
    print(ser.index.name)  # xixi

"""
创建DataFrame对象: df = pd.DataFrame(ndarray/dict)
"""

def dataframe01():
    # 通过ndarray创建dataframe,不指定行/列索引,默认是自增长的int类型
    df = pd.DataFrame(np.random.rand(3, 4))
    print(df)
    #           0         1         2         3
    # 0  0.714400  0.028173  0.796146  0.246265
    # 1  0.655501  0.667714  0.201332  0.674610
    # 2  0.409520  0.800446  0.881828  0.512586

    # 查看索引
    print(df.index)  # RangeIndex(start=0, stop=3, step=1)
    print(df.columns)  # RangeIndex(start=0, stop=4, step=1)

    # 查看数据
    print(df.values)
    # [[0.714400  0.028173  0.796146  0.246265]
    #  [0.655501  0.667714  0.201332  0.674610]
    #  [0.409520  0.800446  0.881828  0.512586]]

    # 查看DataFrame对象的元素的数据类型
    print(df.dtypes)
    # 0    float64
    # 1    float64
    # 2    float64
    # 3    float64
    # dtype: object

    # 查看DataFrame对象的数据类型
    print(type(df))  # <class 'pandas.core.frame.DataFrame'>

    print(df.head(2))
    #           0         1         2         3
    # 0  0.714400  0.028173  0.796146  0.246265
    # 1  0.655501  0.667714  0.201332  0.674610

def dataframe02():
    # 通过dict创建dataframe
    df = pd.DataFrame({
        "A": 1.0,  # float类型
        "B": pd.Timestamp("20170625"),  # timestramp类型
        "C": pd.Series(range(10, 14)),  # Series 类型
        "D": ["Python", "C", "C++", "Java"],  # Python列表类型
        "E": np.array([10] * 4),  # ndarray类型
        "F": "orc"  # str 类型
    })
    print(df)
    #      A          B   C       D   E    F
    # 0  1.0 2017-06-25  10  Python  10  orc
    # 1  1.0 2017-06-25  11       C  10  orc
    # 2  1.0 2017-06-25  12     C++  10  orc
    # 3  1.0 2017-06-25  13    Java  10  orc

    # 查找指定列数据
    print(df["D"])
    # 0    Python
    # 1         C
    # 2       C++
    # 3      Java
    # Name: D, dtype: object

    # 查找指定列数据的指定行
    print(df["D"][2])  # C++

    # 添加列
    df["G"] = df["C"] * 2
    print(df)
    #      A          B   C       D   E    F   G
    # 0  1.0 2017-06-25  10  Python  10  orc  20
    # 1  1.0 2017-06-25  11       C  10  orc  22
    # 2  1.0 2017-06-25  12     C++  10  orc  24
    # 3  1.0 2017-06-25  13    Java  10  orc  26

    # 删除列
    del(df["F"])
    print(df)
    #      A          B   C       D   E   G
    # 0  1.0 2017-06-25  10  Python  10  20
    # 1  1.0 2017-06-25  11       C  10  22
    # 2  1.0 2017-06-25  12     C++  10  24
    # 3  1.0 2017-06-25  13    Java  10  26


if __name__ == "__main__":
    # series01()
    # series02()
    dataframe01()
    # dataframe02()