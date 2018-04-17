# coding=utf-8
import numpy as np
import pandas as pd

"""
使用Numpy内置函数
"""

def func():
    # 创建Series对象
    ser = pd.Series(range(10, 15))
    print(ser)
    # 0    10
    # 1    11
    # 2    12
    # 3    13
    # 4    14
    # dtype: int64
    print(np.sum(ser))  # 60
    print(np.mean(ser))  # 12.0

    # 创建DataFrame对象
    df = pd.DataFrame(np.random.rand(3, 4))
    print(df)
    #          0         1         2         3
    # 0  0.812014  0.450101  0.530228  0.886650
    # 1  0.137895  0.585542  0.653094  0.903724
    # 2  0.351485  0.575038  0.389685  0.871155
    print(np.sum(df))  # 默认按列计算
    # 0    1.301394
    # 1    1.610681
    # 2    1.573008
    # 3    2.661528
    # dtype: float64
    print(np.sum(df, axis=1))  # 可以指定按行计算
    # 0    2.678993
    # 1    2.280255
    # 2    2.187362
    # dtype: float64

"""
统计函数
"""

def statistics():
    # 创建DataFrame对象
    df = pd.DataFrame(np.random.rand(3, 4), index=["A", "B", "C"], columns=["a", "b", "c", "d"])
    print(df)
    #           a         b         c         d
    # A  0.662115  0.561382  0.868828  0.035643
    # B  0.245825  0.518846  0.465999  0.427616
    # C  0.729571  0.003776  0.531873  0.042876

    # 求和,默认axis=0按列
    print(df.sum())
    # a    1.637511
    # b    1.084003
    # c    1.866699
    # d    0.506136
    # dtype: float64

    # 按行求和: skipna表示是否排除缺失值,默认为True
    print(df.sum(axis=1, skipna=False))
    # A    2.127968
    # B    1.658286
    # C    1.308095
    # dtype: float64

    # 统计描述
    print(df.describe())
    #               a         b         c         d
    # count  3.000000  3.000000  3.000000  3.000000
    # mean   0.545837  0.361334  0.622233  0.168712
    # std    0.261998  0.310385  0.216082  0.224247
    # min    0.245825  0.003776  0.465999  0.035643
    # 25%    0.453970  0.261311  0.498936  0.039260
    # 50%    0.662115  0.518846  0.531873  0.042876
    # 75%    0.695843  0.540114  0.700350  0.235246
    # max    0.729571  0.561382  0.868828  0.427616


"""
df.apply(func): 作用于行/列
df.applymap(func): 作用于每一个元素
注意: Series对象只有apply() --> AttributeError: 'Series' object has no attribute 'applymap'
"""

def apply():
    # 创建DataFrame对象
    df = pd.DataFrame(np.random.rand(3, 4))
    print(df)
    #           0         1         2         3
    # 0  0.576049  0.953486  0.590568  0.733479
    # 1  0.659062  0.407894  0.673379  0.055446
    # 2  0.108279  0.174220  0.333750  0.138823
    print(np.max(df))
    # 0    0.659062
    # 1    0.953486
    # 2    0.673379
    # 3    0.733479
    # dtype: float64

    # 求每一列最大值(默认axis=0按列)
    print(df.apply(lambda x: x.max()))  # 等价于np.max(df)
    # 0    0.659062
    # 1    0.953486
    # 2    0.673379
    # 3    0.733479
    # dtype: float64

    # 求每一行最大值(按行)
    print(df.apply(lambda x: x.max(), axis=1))
    # 0    0.953486
    # 1    0.673379
    # 2    0.333750
    # dtype: float64

    # 将每个元素保留两位小数
    print(df.applymap(lambda x: "%.2f" % x))
    #           0         1         2         3
    # 0      0.58      0.96      0.60      0.74
    # 1      0.66      0.41      0.67      0.06
    # 2      0.11      0.17      0.33      0.14


"""
排序函数: 按索引排序 --> df.sort_index() 默认axis=0, ascending=True
         按值排序 --> df.sort_values(by='column name')
"""

def sort01():
    # 创建Series对象
    ser = pd.Series(range(10, 15), index=[np.random.randint(1, 20, (5))])
    print(ser)
    # 9     10
    # 17    11
    # 13    12
    # 1     13
    # 2     14
    # dtype: int64

    # 按索引大小排序,默认升序
    print(ser.sort_index())
    # 1     13
    # 2     14
    # 9     10
    # 13    12
    # 17    11
    # dtype: int64

    # 按索引大小降序排序
    print(ser.sort_index(ascending=False))
    # 17    11
    # 13    12
    # 9     10
    # 2     14
    # 1     13
    # dtype: int64

    # 创建DataFrame对象
    df = pd.DataFrame(
        np.random.rand(3, 4),
        index=[np.random.randint(1, 50, (3))],
        columns=[np.random.randint(1, 50, (4))]
    )
    print(df)
    #           4         9         3         6
    # 8  0.239748  0.809207  0.188228  0.303757
    # 5  0.952137  0.785475  0.092088  0.439625
    # 1  0.704169  0.591714  0.787556  0.666112

    # 默认是按行索引升序排列(注意：此处axis=0是按行,与别处不一样)
    print(df.sort_index())
    #           4         9         3         6
    # 1  0.704169  0.591714  0.787556  0.666112
    # 5  0.952137  0.785475  0.092088  0.439625
    # 8  0.239748  0.809207  0.188228  0.303757

    # 指定按列索引降序排列
    print(df.sort_index(axis=1, ascending=False))
    #           9         6         4         3
    # 8  0.809207  0.303757  0.239748  0.188228
    # 5  0.785475  0.439625  0.952137  0.092088
    # 1  0.591714  0.666112  0.704169  0.787556

def sort02():
    # 创建Series对象
    ser = pd.Series(range(10, 15), index=[np.random.randint(1, 20, (5))])
    print(ser)
    # 12    10
    # 14    11
    # 5     12
    # 4     13
    # 12    14
    # dtype: int64

    # 按值大小排序,默认升序
    print(ser.sort_values())
    # 12    10
    # 14    11
    # 5     12
    # 4     13
    # 12    14
    # dtype: int64

    # 按值大小降序排序
    print(ser.sort_values(ascending=False))
    # 12    14
    # 4     13
    # 5     12
    # 14    11
    # 12    10
    # dtype: int64

    # 创建DataFrame对象
    df = pd.DataFrame(
        np.random.rand(3, 4),
        index=["A", "B", "C"],
        columns=["a", "b", "c", "d"]
    )
    print(df)
    #           a         b         c         d
    # A  0.937402  0.286003  0.283498  0.341866
    # B  0.420777  0.129560  0.168913  0.421132
    # C  0.663444  0.847107  0.417213  0.151916

    # 注意：by后面跟的是字段名称,所以只能是列索引,默认升序
    print(df.sort_values(by="c"))
    #           a         b         c         d
    # B  0.420777  0.129560  0.168913  0.421132
    # A  0.937402  0.286003  0.283498  0.341866
    # C  0.663444  0.847107  0.417213  0.151916

    print(df.sort_values(by="c", ascending=False))
    #           a         b         c         d
    # C  0.663444  0.847107  0.417213  0.151916
    # A  0.937402  0.286003  0.283498  0.341866
    # B  0.420777  0.129560  0.168913  0.421132


"""
处理缺失值
"""

def nan():
    # 创建DataFrame对象
    df = pd.DataFrame(
        [
            np.random.randn(4),
            [10., np.nan, 20., np.nan],
            [30., np.nan, np.nan, 40.]
        ]
    )
    print(df)
    #            0          1          2          3
    # 0   1.213876   0.634034  -0.518584   0.312328
    # 1  10.000000        NaN  20.000000        NaN
    # 2  30.000000        NaN        NaN  40.000000

    # 1、判断是否存在缺失值
    print(df.isnull())
    #        0      1      2      3
    # 0  False  False  False  False
    # 1  False   True  False   True
    # 2   True  False   True  False

    # 2、丢弃缺失数据的行/列,默认axis=0(按行处理)
    print(df.dropna())
    #           0         1         2         3
    # 0  1.213876  0.634034 -0.518584  0.312328

    print(df.dropna(axis=1))
    #            0
    # 0   1.213876
    # 1  10.000000
    # 2  30.000000

    # 3、填充缺失数据
    print(df.fillna(50.))
    #            0          1          2          3
    # 0   1.213876   0.634034  -0.518584   0.312328
    # 1  10.000000  50.000000  20.000000  50.000000
    # 2  50.000000  30.000000  50.000000  40.000000


if __name__ == "__main__":
    # func()
    statistics()
    # apply()
    # sort01()
    # sort02()
    # nan()