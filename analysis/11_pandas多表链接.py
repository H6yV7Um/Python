# coding=utf-8
"""
pd.merge(): 根据单个或多个键将不同DataFrame的行连接起来,类似数据库的连接操作
pd.concat(): 沿轴方向将多个对象合并到一起
duplicated(): 判断是否是重复行    drop_duplicates(): 过滤重复行
replace(): 根据值的内容进行替换
"""

import numpy as np
import pandas as pd

def merge01():
    # 创建DataFrame对象
    df1 = pd.DataFrame({
            "key": ["a", "b", "c", "b", "a", "b", "c"],
            "data1": np.random.rand(7)
        })
    df2 = pd.DataFrame({
            "key": ["a", "b", "c", "d"],
            "data2": np.random.randint(10, 20, 4)
        })
    print(df1)
    #       data1 key
    # 0  0.605224   a
    # 1  0.875598   b
    # 2  0.259573   c
    # 3  0.418260   b
    # 4  0.744634   a
    # 5  0.712319   b
    # 6  0.076110   c
    print(df2)
    #    data2 key
    # 0     14   a
    # 1     13   b
    # 2     12   c
    # 3     17   d

    # 1、默认使用相同列名作为外键,且是内连接
    print(pd.merge(df1, df2))
    #       data1 key  data2
    # 0  0.605224   a     14
    # 1  0.744634   a     14
    # 2  0.875598   b     13
    # 3  0.418260   b     13
    # 4  0.712319   b     13
    # 5  0.259573   c     12
    # 6  0.076110   c     12

    # 2、指定外键: on=""
    print(pd.merge(df1, df2, on="key"))
    #       data1 key  data2
    # 0  0.605224   a     14
    # 1  0.744634   a     14
    # 2  0.875598   b     13
    # 3  0.418260   b     13
    # 4  0.712319   b     13
    # 5  0.259573   c     12
    # 6  0.076110   c     12

    # 更改列名返回新的df
    df1 = df1.rename(columns={"key": "key1"})
    df2 = df2.rename(columns={"key": "key2"})
    print(df1)
    #       data1 key1
    # 0  0.605224    a
    # 1  0.875598    b
    # 2  0.259573    c
    # 3  0.418260    b
    # 4  0.744634    a
    # 5  0.712319    b
    # 6  0.076110    c
    print(df2)
    #    data2 key2
    # 0     14    a
    # 1     13    b
    # 2     12    c
    # 3     17    d

    # 3、如果两张表没有相同列名,可以手动指定左右两个表的外键: left_on=""  right_on=""
    print(pd.merge(df1, df2, left_on="key1", right_on="key2"))
    #       data1 key1  data2 key2
    # 0  0.605224    a     14    a
    # 1  0.744634    a     14    a
    # 2  0.875598    b     13    b
    # 3  0.418260    b     13    b
    # 4  0.712319    b     13    b
    # 5  0.259573    c     12    c
    # 6  0.076110    c     12    c

    # 4、可以用how指定是(内/外/左/右)连接,默认内连接取交集
    print(pd.merge(df1, df2, left_on="key1", right_on="key2", how="outer"))
    #       data1 key1  data2 key2
    # 0  0.605224    a     14    a
    # 1  0.744634    a     14    a
    # 2  0.875598    b     13    b
    # 3  0.418260    b     13    b
    # 4  0.712319    b     13    b
    # 5  0.259573    c     12    c
    # 6  0.076110    c     12    c
    # 7       NaN  NaN     17    d

    print(pd.merge(df1, df2, left_on="key1", right_on="key2", how="left"))
    #       data1 key1  data2 key2
    # 0  0.605224    a     14    a
    # 1  0.875598    b     13    b
    # 2  0.259573    c     12    c
    # 3  0.418260    b     13    b
    # 4  0.744634    a     14    a
    # 5  0.712319    b     13    b
    # 6  0.076110    c     12    c

    print(pd.merge(df1, df2, left_on="key1", right_on="key2", how="right"))
    #       data1 key1  data2 key2
    # 0  0.605224    a     14    a
    # 1  0.744634    a     14    a
    # 2  0.875598    b     13    b
    # 3  0.418260    b     13    b
    # 4  0.712319    b     13    b
    # 5  0.259573    c     12    c
    # 6  0.076110    c     12    c
    # 7       NaN  NaN     17    d

def merge02():
    # 创建DataFrame对象
    df1 = pd.DataFrame({
        "key1": ["a", "b", "c", "b", "a", "b", "c"],
        "data": np.random.randint(1, 10, 7)
    })
    df2 = pd.DataFrame({
        "key2": ["a", "b", "c", "d"],
        "data": np.random.randint(10, 20, 4)
    })
    print(df1)
    #    data key1
    # 0     4    a
    # 1     5    b
    # 2     5    c
    # 3     7    b
    # 4     9    a
    # 5     1    b
    # 6     3    c
    print(df2)
    #    data key2
    # 0    10    a
    # 1    14    b
    # 2    19    c
    # 3    17    d

    # 处理两个表的重复列名: suffixes接收一个可迭代对象(tuple,list,set等),分别给左右表的数据列名加后缀
    print(pd.merge(df1, df2, left_on="key1", right_on="key2", suffixes=("_left", "_right")))
    #    data_left key1  data_right key2
    # 0          4    a          10    a
    # 1          9    a          10    a
    # 2          5    b          14    b
    # 3          7    b          14    b
    # 4          1    b          14    b
    # 5          5    c          19    c
    # 6          3    c          19    c

def merge03():
    # 创建DataFrame对象
    df1 = pd.DataFrame({
        "key": ["a", "b", "c", "d", "a", "b"],
        "data1": np.random.randn(6)
    })
    df2 = pd.DataFrame({"data2": np.random.randint(10, 20, 3)}, index=["a", "b", "c"])
    print(df1)
    #       data1 key
    # 0  0.027250   a
    # 1 -1.069506   b
    # 2  0.471796   c
    # 3 -0.457012   d
    # 4 -0.361524   a
    # 5 -1.074912   b
    print(df2)
    #    data2
    # a     14
    # b     10
    # c     16

    # 按行索引进行连接: right_index=True表示将右边表的行索引做为外键连接
    print(pd.merge(df1, df2, left_on="key", right_index=True, how="outer"))
    #       data1 key  data2
    # 0  0.027250   a   14.0
    # 4 -0.361524   a   14.0
    # 1 -1.069506   b   10.0
    # 5 -1.074912   b   10.0
    # 2  0.471796   c   16.0
    # 3 -0.457012   d    NaN

    print(pd.merge(df2, df1, left_index=True, right_on="key", how="outer"))
    #    data2     data1 key
    # 0   14.0  0.027250   a
    # 4   14.0 -0.361524   a
    # 1   10.0 -1.069506   b
    # 5   10.0 -1.074912   b
    # 2   16.0  0.471796   c
    # 3    NaN -0.457012   d

def concat():
    # 1、创建ndarray对象
    arr1 = np.random.randint(10, 20, (3, 4))
    arr2 = np.random.randint(10, 20, (3, 4))

    # 默认axis=0按列合并(列数不变,行数增加)
    print(np.concatenate([arr1, arr2]))
    # [[13 18 12 15]
    #  [13 10 17 13]
    #  [17 10 10 13]
    #  [11 13 11 10]
    #  [17 18 10 17]
    #  [17 12 19 16]]

    # 可以指定axis=1按行合并(行数不变,列数增加)
    print(np.concatenate([arr1, arr2], axis=1))
    # [[13 18 12 15 11 13 11 10]
    #  [13 10 17 13 17 18 10 17]
    #  [17 10 10 13 17 12 19 16]]

    # 2、创建Series对象
    s1 = pd.Series(np.random.randint(10, 20, 2), index=range(0, 2))
    s2 = pd.Series(np.random.randint(10, 20, 3), index=range(2, 5))
    s3 = pd.Series(np.random.randint(10, 20, 4), index=range(5, 9))

    s4 = pd.Series(np.random.randint(10, 20, 2))
    s5 = pd.Series(np.random.randint(10, 20, 3))
    s6 = pd.Series(np.random.randint(10, 20, 4))

    # 索引号不同的Series对象合并
    print(pd.concat([s1, s2, s3]))
    # 0    18
    # 1    11
    # 2    13
    # 3    14
    # 4    13
    # 5    14
    # 6    15
    # 7    16
    # 8    15
    # dtype: int32

    # 索引号相同的Series对象合并
    print(pd.concat([s4, s5, s6]))
    # 0    11
    # 1    12
    # 0    16
    # 1    14
    # 2    19
    # 0    17
    # 1    10
    # 2    15
    # 3    12
    # dtype: int32

    # Series对象默认按列合并,可以指定axis=1按行合并
    print(pd.concat([s4, s5, s6], axis=1))
    #       0     1   2
    # 0  11.0  16.0  17
    # 1  12.0  14.0  10
    # 2   NaN  19.0  15
    # 3   NaN   NaN  12

    # Series对象默认是外连接(数据全部保留,缺失数据用NaN表示),可以指定join="inner"为内连接
    print(pd.concat([s4, s5, s6], axis=1, join="inner"))
    #     0   1   2
    # 0  11  16  17
    # 1  12  14  10

    # 3、创建DataFrame对象
    df1 = pd.DataFrame(np.random.randint(10, 20, (2, 3)), index=["A", "B"], columns=["a", "b", "c"])
    df2 = pd.DataFrame(np.random.randint(10, 20, (3, 4)), index=["A", "B", "C"], columns=["a", "b", "c", "d"])
    print(df1)
    #     a   b   c
    # A  19  12  10
    # B  18  13  12
    print(df2)
    #     a   b   c   d
    # A  18  18  15  16
    # B  13  18  19  19
    # C  15  10  17  15

    # DataFrame对象默认按列合并,外链接
    print(pd.concat([df1, df2]))
    #     a   b   c     d
    # A  19  12  10   NaN
    # B  18  13  12   NaN
    # A  18  18  15  16.0
    # B  13  18  19  19.0
    # C  15  10  17  15.0

    # DataFrame对象可以指定按行合并,内连接
    print(pd.concat([df1, df2], axis=1, join="inner"))
    #     a   b   c   a   b   c   d
    # A  19  12  10  18  18  15  16
    # B  18  13  12  13  18  19  19

def duplicated():
    # 1、创建Series对象
    s1 = pd.Series(np.random.randint(10, 15, 8))
    print(s1)
    # 0    10
    # 1    11
    # 2    12
    # 3    14
    # 4    10
    # 5    13
    # 6    13
    # 7    12
    # dtype: int32

    # 判断Series对象每行数据是否是重复数据,返回bool值
    print(s1.duplicated())
    # 0    False
    # 1    False
    # 2    False
    # 3    False
    # 4     True
    # 5    False
    # 6     True
    # 7     True
    # dtype: bool

    # 可以直接过滤掉重复数据的行,只留数据首次出现的行
    print(s1.drop_duplicates())
    # 0    10
    # 1    11
    # 2    12
    # 3    14
    # 5    13
    # dtype: int32

    # 2、创建DataFrame对象
    df = pd.DataFrame({
        "data1": np.random.randint(10, 15, 8),
        "data2": ["a", "b", "c", "b", "b", "a", "a", "c"]
    })
    print(df)
    #    data1 data2
    # 0     13     a
    # 1     11     b
    # 2     11     c
    # 3     12     b
    # 4     10     b
    # 5     10     a
    # 6     13     a
    # 7     10     c

    # 将data2列数据的b都替换成d
    print(df["data2"].replace("b", "d"))
    # 0    a
    # 1    d
    # 2    c
    # 3    d
    # 4    d
    # 5    a
    # 6    a
    # 7    c
    # Name: data2, dtype: object

    # DataFrame对象需要指定列进行判断和过滤
    print(df.duplicated("data1"))
    # 0    False
    # 1    False
    # 2     True
    # 3    False
    # 4    False
    # 5     True
    # 6     True
    # 7     True
    # dtype: bool

    # 按指定列过滤数据时,其他列的数据也会相应的丢失
    print(df.drop_duplicates("data2"))
    #    data1 data2
    # 0     13     a
    # 1     11     b
    # 2     11     c


if __name__ == "__main__":
    # merge01()
    # merge02()
    # merge03()
    # concat()
    duplicated()