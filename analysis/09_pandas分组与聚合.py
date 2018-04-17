# coding=utf-8
"""
分组: groupby有很多种分组方式
对数据集进行分组,然后对每组进行统计分析;SQL能够对数据进行过滤和分组聚合;pandas能利用groupby进行更加复杂的分组运算
分组运算过程: split --> apply --> combine
      拆分: 进行分组的根据
      应用: 每个分组运行的计算规则
      合并: 把每个分组的计算结果合并起来
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
    print(type(df))  # <class 'pandas.core.frame.DataFrame'>

    # 创建groupby对象
    group = df.groupby("key1")
    print(group)  # <pandas.core.groupby.DataFrameGroupBy object at 0x000001D880153CF8>
    print(type(group))  # <class 'pandas.core.groupby.DataFrameGroupBy'>

    # 对所有数据分组: 不需要指定分组依据
    group1 = df.groupby("key1")
    print(group1.sum())

    # 对某一列数据分组: 需要指定分组依据的对象
    group2 = df["data1"].groupby(df["key1"])
    print(group2.sum())

    # 自定义分组
    self_key = [10, 20, 30, 40, 40, 30, 20, 10]
    group3 = df.groupby(self_key)
    print(group3.sum())

    # 多层分组
    group4 = df.groupby(["key1", "key2"])
    print(group4.sum())

    # 单层分组组名是一个字符串
    for group_name, group_data in group1:
        print(group_name)
        print(group_data)
        print("=======")

    # 多层分组组名是包含多个字符串的元组
    for group_name, group_data in group4:
        print(group_name)
        print(group_data)
        print("=======")

    print("-" * 50)

    # 将groupby对象转换成list/dict_obj
    print(list(group4))
    print("-" * 50)
    print(dict(list(group1)))
    print("-" * 50)
    print(dict(list(group1))["b"])

    # 按数据类型分组
    print(df.dtypes)
    group5 = df.groupby(df.dtypes)
    print(group5.sum())

def test02():
    # 创建DataFrame对象
    df2 = pd.DataFrame(
        np.random.randint(10, 20, (3, 4)),
        index=["Python", "C++", "C"],
        columns=['a', 'b', 'c', 'd']
    )
    print(df2)
    # 利用高级索引的位置索引iloc将第二行的2~3列值替换成NaN; 注意: NaN所在的列数据都会变成float类型
    df2.iloc[1, 1:3] = np.NaN
    print(df2)

    # 1、按数据类型分组: 如果表格中有NaN值,需要指定轴方向为行,因为每一列的数据类型是相同的
    group = df2.groupby(df2.dtypes, axis=1)
    print(group.sum())

    # 2、按字典(别名)分组: 需要指定轴方向为行
    # 创建一个字典,对应每一列的别名，则分组运算时，按字典的值（别名）来进行分组
    dict_obj2 = {"a": "tony", "b": "robin", "c": "jack", 'd': "robin"}
    group1 = df2.groupby(dict_obj2, axis=1)
    print(group1.sum())

    # 3、按函数分组
    group2 = df2.groupby(lambda index: len(index), axis=1)
    print(group2.sum())

def test03():
    # 根据嵌套列表创建层级索引,name指定索引名称
    columns = pd.MultiIndex.from_arrays([['Python', 'Java', 'Python', 'Java', 'Python'],
                                         ['A', 'A', 'B', 'C', 'B']], names=['language', 'index'])

    # 创建5 * 5的DataFrame对象,并指定列索引为层级索引
    df = pd.DataFrame(np.random.randint(1, 10, (5, 5)), columns=columns)
    print(df)

    # level指定索引级别,axis指定索引方向(行索引/列索引)
    print(df.groupby(level=0, axis=1).sum())

    # level也可以直接指定索引名来做分组
    print(df.groupby(level="language", axis=1).sum())



if __name__ == "__main__":
    # test01()
    # test02()
    test03()