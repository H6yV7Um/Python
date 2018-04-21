# coding=utf-8
"""
pandas里最强大的功能就是分组和聚合

分组: groupby()有很多种分组方式,GroupBy对象没有进行实际运算,只是包含分组的中间数据
分组运算过程: split --> apply --> combine
      拆分: 进行分组的根据
      应用: 每个分组运行的计算规则
      合并: 把每个分组的计算结果合并起来

聚合: 对分组后的数据计算
"""

import numpy as np
import pandas as pd

def test01():
    # 创建DataFrame对象
    dict_obj = {
        "key1": ['a', 'b', 'a', 'a', 'b', 'b', 'b', 'a'],
        "key2": ['One', 'Two', 'Two', 'Three', 'Three', 'Two', 'One', 'Three'],
        "data1": np.random.randn(8),
        "data2": np.random.randn(8)
    }
    df = pd.DataFrame(dict_obj)
    print(df)
    #       data1     data2 key1   key2
    # 0 -0.409179  1.523943    a    One
    # 1  1.479765 -1.054014    b    Two
    # 2 -0.368391 -1.140189    a    Two
    # 3 -0.427695  2.227563    a  Three
    # 4  0.365053 -0.680219    b  Three
    # 5  0.606713  1.012532    b    Two
    # 6 -1.077176 -0.081993    b    One
    # 7  1.712611  0.391927    a  Three

    print(type(df))  # <class 'pandas.core.frame.DataFrame'>

    # 创建groupby对象
    group = df.groupby("key1")
    print(group)  # <pandas.core.groupby.DataFrameGroupBy object at 0x000001D880153CF8>
    print(type(group))  # <class 'pandas.core.groupby.DataFrameGroupBy'>

    # 1、对所有数据分组: 不需要指定分组依据
    group1 = df.groupby("key1")
    print(group1.sum())
    #          data1     data2
    # key1
    # a     0.507347  3.003244
    # b     1.374356 -0.803693

    # 2、对指定列数据分组: 需要指定分组依据的对象
    group2 = df["data1"].groupby(df["key1"])
    print(group2.sum())
    # key1
    # a    0.507347
    # b    1.374356
    # Name: data1, dtype: float64

    # 3、自定义分组
    self_key = [10, 20, 30, 40, 40, 30, 20, 10]
    group3 = df.groupby(self_key)
    print(group3.sum())
    #        data1     data2
    # 10  1.303433  1.915870
    # 20  0.402590 -1.136007
    # 30  0.238322 -0.127657
    # 40 -0.062642  1.547344

    # 4、多层分组: 先按key1分组再按key2分组
    group4 = df.groupby(["key1", "key2"])
    print(group4.sum())
    #                data1     data2
    # key1 key2
    # a    One   -0.409179  1.523943
    #      Three  1.284917  2.619489
    #      Two   -0.368391 -1.140189
    # b    One   -1.077176 -0.081993
    #      Three  0.365053 -0.680219
    #      Two    2.086478 -0.041482

    # 单层分组组名是一个字符串
    for group_name, group_data in group1:
        print(group_name)
        print(group_data)
    # a
    #       data1     data2 key1   key2
    # 0 -0.409179  1.523943    a    One
    # 2 -0.368391 -1.140189    a    Two
    # 3 -0.427695  2.227563    a  Three
    # 7  1.712611  0.391927    a  Three
    # b
    #       data1     data2 key1   key2
    # 1  1.479765 -1.054014    b    Two
    # 4  0.365053 -0.680219    b  Three
    # 5  0.606713  1.012532    b    Two
    # 6 -1.077176 -0.081993    b    One

    # 多层分组组名是包含多个字符串的元组
    for group_name, group_data in group4:
        print(group_name)
        print(group_data)
    # ('a', 'One')
    #       data1     data2 key1 key2
    # 0 -0.409179  1.523943    a  One
    # ('a', 'Three')
    #       data1     data2 key1   key2
    # 3 -0.427695  2.227563    a  Three
    # 7  1.712611  0.391927    a  Three
    # ('a', 'Two')
    #       data1     data2 key1 key2
    # 2 -0.368391 -1.140189    a  Two
    # ('b', 'One')
    #       data1     data2 key1 key2
    # 6 -1.077176 -0.081993    b  One
    # ('b', 'Three')
    #       data1     data2 key1   key2
    # 4  0.365053 -0.680219    b  Three
    # ('b', 'Two')
    #       data1     data2 key1 key2
    # 1  1.479765 -1.054014    b  Two
    # 5  0.606713  1.012532    b  Two

    print("-" * 50)

    # 将groupby对象转换成list/dict_obj
    print(list(group4))
    # [(('a', 'One'),       data1     data2 key1 key2
    #                 0 -0.409179  1.523943    a  One),
    #  (('a', 'Three'),       data1     data2 key1   key2
    #                 3 -0.427695  2.227563    a  Three
    #                 7  1.712611  0.391927    a  Three),
    #  (('a', 'Two'),       data1     data2 key1 key2
    #                 2 -0.368391 -1.140189    a  Two),
    #  (('b', 'One'),       data1     data2 key1 key2
    #                 6 -1.077176 -0.081993    b  One),
    #  (('b', 'Three'),       data1     data2 key1   key2
    #                 4  0.365053 -0.680219    b  Three),
    #  (('b', 'Two'),       data1     data2 key1 key2
    #                 1  1.479765 -1.054014    b  Two
    #                 5  0.606713  1.012532    b  Two)]

    print("-" * 50)

    print(dict(list(group1)))
    # {'a':       data1     data2 key1   key2
    #     0   -0.409179  1.523943    a    One
    #     2   -0.368391 -1.140189    a    Two
    #     3   -0.427695  2.227563    a  Three
    #     7    1.712611  0.391927    a  Three,
    #  'b':       data1     data2 key1   key2
    #     1    1.479765 -1.054014    b    Two
    #     4    0.365053 -0.680219    b  Three
    #     5    0.606713  1.012532    b    Two
    #     6   -1.077176 -0.081993    b    One}

    print("-" * 50)

    print(dict(list(group1))["b"])
    #       data1     data2 key1   key2
    # 1  1.479765 -1.054014    b    Two
    # 4  0.365053 -0.680219    b  Three
    # 5  0.606713  1.012532    b    Two
    # 6 -1.077176 -0.081993    b    One

def test02():
    # 创建DataFrame对象
    df2 = pd.DataFrame(
        np.random.randint(10, 20, (3, 4)),
        index=["Python", "C++", "C"],
        columns=['a', 'b', 'c', 'd']
    )
    print(df2)
    #          a   b   c   d
    # Python  11  15  11  10
    # C++     16  14  15  19
    # C       14  19  10  18

    # 利用高级索引的位置索引iloc将第二行的2~3列值替换成NaN; 注意: NaN所在的列数据都会变成float类型
    df2.iloc[1, 1:3] = np.NaN
    print(df2)
    #          a     b     c   d
    # Python  11  15.0  11.0  10
    # C++     16   NaN   NaN  19
    # C       14  19.0  10.0  18

    # 1、按数据类型分组: 如果表格中有NaN值,需要指定轴方向为行,因为每一列的数据类型是相同的
    group = df2.groupby(df2.dtypes, axis=1)
    print(group.sum())
    #         int32  float64
    # Python   21.0     26.0
    # C++      35.0      0.0
    # C        32.0     29.0

    # 2、按字典(别名)分组: 需要指定轴方向为行
    # 创建一个字典,对应每一列的别名，则分组运算时，按字典的值（别名）来进行分组
    dict_obj2 = {"a": "tony", "b": "robin", "c": "jack", 'd': "robin"}
    group1 = df2.groupby(dict_obj2, axis=1)
    print(group1.sum())
    #         jack  robin  tony
    # Python  11.0   25.0  11.0
    # C++      0.0   19.0  16.0
    # C       10.0   37.0  14.0

    # 3、按函数分组
    group2 = df2.groupby(lambda index: len(index), axis=1)
    print(group2.sum())
    #            1
    # Python  47.0
    # C++     35.0
    # C       61.0

def test03():
    # 根据嵌套列表创建层级索引,name指定索引名称
    columns = pd.MultiIndex.from_arrays([['Python', 'Java', 'Python', 'Java', 'Python'],
                                         ['A', 'A', 'B', 'C', 'B']], names=['language', 'index'])

    # 创建5 * 5的DataFrame对象,并指定列索引为层级索引
    df = pd.DataFrame(np.random.randint(1, 10, (5, 5)), columns=columns)
    print(df)
    # language Python Java Python Java Python
    # index         A    A      B    C      B
    # 0             9    7      8    9      9
    # 1             9    3      6    7      7
    # 2             3    1      7    6      9
    # 3             9    6      1    5      1
    # 4             8    4      6    8      4

    # 4、按索引级别分组: level指定索引级别,axis指定索引方向(行索引/列索引)
    print(df.groupby(level=0, axis=1).sum())
    # language  Java  Python
    # 0           16      26
    # 1           10      22
    # 2            7      19
    # 3           11      11
    # 4           12      18

    # level也可以直接指定索引名来做分组
    print(df.groupby(level="language", axis=1).sum())
    # language  Java  Python
    # 0           16      26
    # 1           10      22
    # 2            7      19
    # 3           11      11
    # 4           12      18


if __name__ == "__main__":
    # test01()
    # test02()
    test03()