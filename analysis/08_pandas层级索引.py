# coding=utf-8
import pandas as pd

"""
MultiIndex索引对象: 多层索引
"""

def test01():
    # 创建有多层索引的Series对象
    ser = pd.Series(
        range(10, 15),
        index=[
            ["a", "a", "b", "c", "c"],
            [10, 20, 30, 10, 20]
        ]
    )
    print(ser)
    # a  10    10
    #    20    11
    # b  30    12
    # c  10    13
    #    20    14
    # dtype: int64

    # 查看索引: levels表示两个层级中分别有那些标签,labels是每个位置分别是什么标签
    print(ser.index)
    # MultiIndex(levels=[['a', 'b', 'c'], [10, 20, 30]],
    #            labels=[[0, 0, 1, 2, 2], [0, 1, 2, 0, 1]])

    # 查看索引类型
    print(type(ser.index))  # <class 'pandas.core.indexes.multi.MultiIndex'>

    # 根据外层索引取值
    print(ser["b"])
    # 30    12
    # dtype: int64

    # 取出所有外层索引的内层索引为20的值
    print(ser[:, 20])
    # a    11
    # c    14
    # dtype: int64

    # 取出外层索引为a内层索引为10的值
    print(ser["a", 10])  # 10

    # 交换分层: ser.swaplevel(level),0是最外层、1是次外层。。。
    print(ser.swaplevel())  # 只有两层就不用写参数,就是最外层与次外层交换
    # 10  a    10
    # 20  a    11
    # 30  b    12
    # 10  c    13
    # 20  c    14
    # dtype: int64

    # 按层索引排序: ser.sort_index(level),默认level=0最外层、level=1次外层。。。
    print(ser.sort_index())
    # a  10    10
    #    20    11
    # b  30    12
    # c  10    13
    #    20    14
    # dtype: int64
    print(ser.sort_index(level=1))
    # a  10    10
    # c  10    13
    # a  20    11
    # c  20    14
    # b  30    12
    # dtype: int64

    # 先交换分层再按层索引排序
    print(ser.swaplevel().sort_index())
    # 10  a    10
    #     c    13
    # 20  a    11
    #     c    14
    # 30  b    12
    # dtype: int64


"""
重构:
unstack(): 将Series对象重构成DataFrame对象
stack(): 将DataFrame对象重构成Series对象
"""

def test02():
    # 创建有多层索引的Series对象
    ser = pd.Series(
        range(10, 15),
        index=[
            ["a", "a", "b", "c", "c"],
            [10, 20, 30, 10, 20]
        ]
    )
    print(ser)
    # a  10    10
    #    20    11
    # b  30    12
    # c  10    13
    #    20    14
    # dtype: int64

    # unstack(level)默认level=-1将最内层的索引变成列索引,匹配不到的就给NaN值
    print(ser.unstack())
    #      10    20    30
    # a  10.0  11.0   NaN
    # b   NaN   NaN  12.0
    # c  13.0  14.0   NaN

    # unstack(level=0)可以将外层索引变成列索引
    df = ser.unstack(level=0)
    print(df)
    #        a     b     c
    # 10  10.0   NaN  13.0
    # 20  11.0   NaN  14.0
    # 30   NaN  12.0   NaN

    # stack()将DataFrame对象重构成Series对象,索引不变,默认会丢弃NaN值
    print(df.stack())
    # 10  a    10.0
    #     c    13.0
    # 20  a    11.0
    #     c    14.0
    # 30  b    12.0
    # dtype: float64


if __name__ == "__main__":
    # test01()
    test02()