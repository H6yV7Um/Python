# coding=utf-8
"""
Series和DataFrame中的索引都是Index对象
Series: <class 'pandas.core.series.Series'>
DataFrame: <class 'pandas.core.frame.DataFrame'>
常见Index种类:
Index,索引
Int64Index,整数索引
MultiIndex,层级索引
DatetimeIndex,时间戳类型
高级索引: 包括标签索引loc和位置索引iloc
"""

import numpy as np
import pandas as pd

"""
Series索引
"""

def index01():
    # 创建Series对象,并指定行索引
    ser = pd.Series(range(10, 15), index=["a", "b", "c", "d", "e"])
    print(ser)
    # a    10
    # b    11
    # c    12
    # d    13
    # e    14
    # dtype: int64

    # 查看索引
    print(ser.index)  # Index(['a', 'b', 'c', 'd', 'e'], dtype='object')
    print(type(ser.index))  # <class 'pandas.core.indexes.base.Index'>

    # 查看数据
    print(ser.values)  # [10 11 12 13 14]

    # 查看数据类型
    print(ser.dtype)  # int64
    print(type(ser))  # <class 'pandas.core.series.Series'>

    # 1、行索引: ser[pos],ser['label'],
    print(ser[2])  # 12
    print(ser["c"])  # 12

    # 2、切片索引(连续索引): ser['label1': 'label3'],ser[2:4],
    print(ser["b": "d"])  # 注意: 标签索引是会包含末尾位置的
    # b    11
    # c    12
    # d    13
    # dtype: int64
    print(ser.loc["b": "d"])
    # b    11
    # c    12
    # d    13
    # dtype: int64
    print(ser[1:3])
    # b    11
    # c    12
    # dtype: int64
    print(ser.iloc[1:3])
    # b    11
    # c    12
    # dtype: int64

    # 3、不连续索引: ser[['label1', 'label2', 'label3']],ser[[pos1, pos2, pos3]]
    print(ser[["a", "c"]])
    # a    10
    # c    12
    # dtype: int64
    print(ser[[0, 2, 4]])
    # a    10
    # c    12
    # e    14
    # dtype: int64

    # 4、布尔索引:
    ser1 = (ser % 2) == 0
    print(ser1)
    # a     True
    # b    False
    # c     True
    # d    False
    # e     True
    # dtype: bool

    # 返回符合bool条件的对象: True值保留,False值舍弃
    print(ser[ser1])
    # a    10
    # c    12
    # e    14
    # dtype: int64
    print(ser[ser > 12])
    # d    13
    # e    14
    # dtype: int64


"""
DataFrame索引: 类似ndarray的索引操作
"""

def index02():
    # 创建DataFrame对象,并指定行索引和列索引
    df = pd.DataFrame(np.random.rand(3, 4), index=["A", "B", "C"], columns=["a", "b", "c", "d"])
    print(df)
    #           a         b         c         d
    # A  0.839326  0.029922  0.436647  0.452534
    # B  0.511720  0.745351  0.401869  0.952479
    # C  0.043536  0.411603  0.863108  0.350684

    # 查看索引
    print(df.index)  # Index(['A', 'B', 'C'], dtype='object')
    print(df.columns)  # Index(['a', 'b', 'c', 'd'], dtype='object')

    # 查看数据
    print(df.values)
    # [[0.839326  0.029922  0.436647  0.452534]
    #  [0.511720  0.745351  0.401869  0.952479]
    #  [0.043536  0.411603  0.863108  0.350684]]

    # 查看df列的数据类型
    print(df.dtypes)
    # a    float64
    # b    float64
    # c    float64
    # d    float64
    # dtype: object

    # 查看df对象数据类型
    print(type(df))  # <class 'pandas.core.frame.DataFrame'>

    # 1、列索引: DataFrame的列索引只能是label不能是pos --> KeyError: '[1] not in index'
    print(df["c"])
    # A    0.436647
    # B    0.401869
    # C    0.863108
    # Name: c, dtype: float64

    print(df["c"].values)  # [0.436647 0.401869 0.863108]

    # 2、切片索引(连续索引): DataFrame不能直接切片,可通过高级索引的loc(标签索引)/iloc(位置索引)来做切片
    print(df.loc["A": "B", "c": "d"])  # loc两个参数: 行索引和列索引
    #           c         d
    # A  0.436647  0.452534
    # B  0.401869  0.952479
    print(df.iloc[0:2, 2:4])  # iloc两个参数: 行索引和列索引
    #           c         d
    # A  0.436647  0.452534
    # B  0.401869  0.952479

    # 3、不连续索引
    print(df[["a", "c"]])
    #           a         c
    # A  0.839326  0.436647
    # B  0.511720  0.401869
    # C  0.043536  0.863108


if __name__ == "__main__":
    # index01()
    index02()