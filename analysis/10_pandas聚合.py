# coding=utf-8
import numpy as np
import pandas as pd

"""
聚合运算
"""

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
    # 0 -0.534900 -0.929757    a    One
    # 1 -0.707960 -0.560224    b    Two
    # 2 -1.249239  0.502429    a    Two
    # 3 -1.021843  2.579728    a  Three
    # 4 -1.044193 -1.034804    b  Three
    # 5  1.183414  0.966418    b    Two
    # 6 -1.147157 -1.144850    b    One
    # 7  0.813827 -0.586484    a  Three

    # 1、内置聚合函数
    group = df.groupby("key1")
    print(type(group))  # <class 'pandas.core.groupby.DataFrameGroupBy'>

    print(group.sum())
    #          data1     data2
    # key1
    # a    -1.992156  1.565916
    # b    -1.715896 -1.773460

    print(group.mean())
    #          data1     data2
    # key1
    # a    -0.498039  0.391479
    # b    -0.428974 -0.443365

    print(group.max())
    #          data1     data2 key2
    # key1
    # a     0.813827  2.579728  Two
    # b     1.183414  0.966418  Two

    # group.size(): 统计元素个数
    print(group.size())
    # key1
    # a    4
    # b    4
    # dtype: int64

    # group.count(): 统计非NaN值个数
    print(df.groupby("key2").count())
    #        data1  data2  key1
    # key2
    # One        2      2     2
    # Three      3      3     3
    # Two        3      3     3

    print(group.describe())
    #      data1                                                              \
    #      count      mean       std       min       25%       50%       75%
    # key1
    # a      4.0 -0.498039  0.923945 -1.249239 -1.078692 -0.778372 -0.197719
    # b      4.0 -0.428974  1.091163 -1.147157 -1.069934 -0.876076 -0.235116
    #
    #                data2                                                    \
    #            max count      mean       std       min       25%       50%
    # key1
    # a     0.813827   4.0  0.391479  1.581436 -0.929757 -0.672302 -0.042028
    # b     1.183414   4.0 -0.443365  0.973486 -1.144850 -1.062315 -0.797514
    #
    #
    #            75%       max
    # key1
    # a     1.021754  2.579728
    # b    -0.178563  0.966418

    # 2、自定义聚合函数group.agg(func): 实现一些内置函数不具备的功能
    def func(obj):
        return obj.max() - obj.min()
    # Groupby对象通过agg调用自定义的函数
    print(group.agg(func))
    #          data1     data2
    # key1
    # a     2.063066  3.509485
    # b     2.330572  2.111268

    # 3、使用多个聚合函数: agg([...])传入聚合函数列表 --> 内置聚合函数要加"";函数名不能重复;最后按函数名做为列名显示结果
    print(group.agg(["sum", "mean", "count", func]))
    #          data1                               data2
    #            sum      mean count      func       sum      mean count      func
    # key1
    # a    -1.992156 -0.498039     4  2.063066  1.565916  0.391479     4  3.509485
    # b    -1.715896 -0.428974     4  2.330572 -1.773460 -0.443365     4  2.111268

    # 4、对不同数据列使用不同聚合函数: 创建字典对象 --> 键：数据列,值：需要使用的聚合函数(多个聚合函数用list表示)
    dictmap_obj = {
        "data1": "sum",
        "data2": ["mean", "max", func]
    }
    #  agg传入这个字典,即可对不同数据列使用不同聚合函数
    print(group.agg(dictmap_obj))
    #          data1     data2
    #            sum      mean       max      func
    # key1
    # a    -1.992156  0.391479  2.579728  3.509485
    # b    -1.715896 -0.443365  0.966418  2.111268


"""
聚合运算后的多表链接: 将分组后的数据集连接到原数据中
"""

def test02():
    # 创建DataFrame对象
    df = pd.DataFrame(
        {
            "key1": ["a", "b", "b", "a", "a", "b"],
            "key2": ["one", "two", "two", "three"," three", "three"],
            "data1": np.random.randint(1, 20, (6)),
            "data2": np.random.randint(1, 20, (6))
        }
    )
    print(df)
    #    data1  data2 key1    key2
    # 0     11     13    a     one
    # 1      2      2    b     two
    # 2     13     14    b     two
    # 3     16     13    a   three
    # 4     16     13    a   three
    # 5      9      7    b   three

    print(df.dtypes)
    # data1     int32
    # data2     int32
    # key1     object
    # key2     object
    # dtype: object

    print(type(df))  # <class 'pandas.core.frame.DataFrame'>

    # 分组聚合之后给操作的数据列添加前缀
    key1_sum = df.groupby("key1").sum().add_prefix("sum_")
    print(key1_sum)
    #       sum_data1  sum_data2
    # key1
    # a            43         39
    # b            24         23

    print(type(key1_sum))  # <class 'pandas.core.frame.DataFrame'>

    # 1、merge()
    df_new = pd.merge(df, key1_sum, left_on="key1", right_index=True)
    print(df_new)
    #    data1  data2 key1    key2  sum_data1  sum_data2
    # 0     11     13    a     one         43         39
    # 3     16     13    a   three         43         39
    # 4     16     13    a   three         43         39
    # 1      2      2    b     two         24         23
    # 2     13     14    b     two         24         23
    # 5      9      7    b   three         24         23

    # 2、transform(func): 默认是将所有列都参与运算,func可以是内置函数也可以是自定义函数
    key1_sum_tf = df.groupby("key1").transform("sum").add_prefix("sum_")
    print(key1_sum_tf)
    #   sum_data1 sum_data2        sum_key2
    # 0        43        39  onethree three
    # 1        24        23     twotwothree
    # 2        24        23     twotwothree
    # 3        43        39  onethree three
    # 4        43        39  onethree three
    # 5        24        23     twotwothree

    print(type(key1_sum_tf))  # <class 'pandas.core.frame.DataFrame'>
    # 查看聚合生成的df的列索引
    print(key1_sum_tf.columns)  # Index(['sum_data1', 'sum_data2', 'sum_key2'], dtype='object')

    # 将聚合运算生成的结果集添加到原先的df中
    df[key1_sum_tf.columns] = key1_sum_tf
    print(df)
    #    data1  data2 key1    key2 sum_data1 sum_data2        sum_key2
    # 0     11     13    a     one        43        39  onethree three
    # 1      2      2    b     two        24        23     twotwothree
    # 2     13     14    b     two        24        23     twotwothree
    # 3     16     13    a   three        43        39  onethree three
    # 4     16     13    a   three        43        39  onethree three
    # 5      9      7    b   three        24        23     twotwothree

def test03():
    # 3、transform(func)可以指定某些数据列参与运算
    df2 = pd.DataFrame(
        {
            "key1": ["a", "b", "b", "a", "a", "b"],
            "key2": ["one", "two", "two", "three", " three", "three"],
            "data1": np.random.randint(1, 20, (6)),
            "data2": np.random.randint(1, 20, (6))
        }
    )
    print(df2)
    #    data1  data2 key1    key2
    # 0     14      7    a     one
    # 1      4     15    b     two
    # 2      4      6    b     two
    # 3     11      4    a   three
    # 4     11     13    a   three
    # 5     11     11    b   three

    # 按指定列进行分组聚合
    key1_sum_tf2 = df2[["data1", "data2"]].groupby(df2["key1"]).transform("sum").add_prefix("sum_")
    # 等价于: key1_sum_tf2 = df2.iloc[:, 0:2].groupby(df2["key1"]).transform("sum").add_prefix("sum_")
    print(key1_sum_tf2)
    #    sum_data1  sum_data2
    # 0         36         24
    # 1         19         32
    # 2         19         32
    # 3         36         24
    # 4         36         24
    # 5         19         32

    # 将聚合运算生成的结果集添加到原先的df中
    df2[key1_sum_tf2.columns] = key1_sum_tf2
    print(df2)
    #    data1  data2 key1    key2  sum_data1  sum_data2
    # 0     14      7    a     one         36         24
    # 1      4     15    b     two         19         32
    # 2      4      6    b     two         19         32
    # 3     11      4    a   three         36         24
    # 4     11     13    a   three         36         24
    # 5     11     11    b   three         19         32


"""
groupby.apply(func): 分组后的函数应用,func可以是内置函数也可以是自定义函数
"""

def test04():
    filename = "D://starcraft.csv"
    # 加载文件
    df = pd.read_csv(filename, usecols=["LeagueIndex", "Age", "HoursPerWeek", "TotalHours", "APM"])
    print(df.head(10))
    #    LeagueIndex   Age  HoursPerWeek  TotalHours       APM
    # 0            5  27.0          10.0      3000.0  143.7180
    # 1            5  23.0          10.0      5000.0  129.2322
    # 2            4  30.0          10.0       200.0   69.9612
    # 3            3  19.0          20.0       400.0  107.6016
    # 4            3  32.0          10.0       500.0  122.8908
    # 5            2  27.0           6.0        70.0   44.4570
    # 6            1  21.0           8.0       240.0   46.9962
    # 7            7  17.0          42.0     10000.0  212.6022
    # 8            4  20.0          14.0      2708.0  117.4884
    # 9            4  18.0          24.0       800.0  155.9856

    # 需求：按照LeagueIndex列分组，求其他列的topk

    # 自定义topk函数
    def topk(obj, column="APM", n=3):
        # obj是分组后的对象,by是指定排序的列,然后降序排序取前n个值
        return obj.sort_values(by=column, ascending=False)[:n]

    # 按leagueIndex分组,每组数据都会应用apply()的函数
    group = df.groupby("LeagueIndex").apply(topk)
    print(group)
    #                   LeagueIndex   Age  HoursPerWeek  TotalHours       APM
    # LeagueIndex
    # 1           2214            1  20.0          12.0       730.0  172.9530
    #             2246            1  27.0           8.0       250.0  141.6282
    #             1753            1  20.0          28.0       100.0  139.6362
    # 2           3062            2  20.0           6.0       100.0  179.6250
    #             3229            2  16.0          24.0       110.0  156.7380
    #             1520            2  29.0           6.0       250.0  151.6470
    # 3           1557            3  22.0           6.0       200.0  226.6554
    #             484             3  19.0          42.0       450.0  220.0692
    #             2883            3  16.0           8.0       800.0  208.9500
    # 4           2688            4  26.0          24.0       990.0  249.0210
    #             1759            4  16.0           6.0        75.0  229.9122
    #             2637            4  23.0          24.0       650.0  227.2272
    # 5           3277            5  18.0          16.0       950.0  372.6426
    #             93              5  17.0          36.0       720.0  335.4990
    #             202             5  37.0          14.0       800.0  327.7218
    # 6           734             6  16.0          28.0       730.0  389.8314
    #             2746            6  16.0          28.0      4000.0  350.4114
    #             1810            6  21.0          14.0       730.0  323.2506
    # 7           3127            7  23.0          42.0      2000.0  298.7952
    #             104             7  21.0          24.0      1000.0  286.4538
    #             1654            7  18.0          98.0       700.0  236.0316
    # 8           3393            8   NaN           NaN         NaN  375.8664
    #             3373            8   NaN           NaN         NaN  364.8504
    #             3372            8   NaN           NaN         NaN  355.3518

    # 也可以给自定义函数指定参数
    group1 = df.groupby("LeagueIndex").apply(topk, column="TotalHours", n=2)
    print(group1)
    #                  LeagueIndex   Age  HoursPerWeek  TotalHours       APM
    # LeagueIndex
    # 1           2676            1  20.0          24.0      1870.0   67.9392
    #             2751            1  29.0           8.0      1000.0   54.4284
    # 2           2452            2  34.0          24.0      2000.0   69.3036
    #             3162            2  23.0          18.0      1800.0   61.6998
    # 3           2216            3  24.0          20.0     10260.0   76.5852
    #             10              3  16.0          16.0      6000.0  153.8010
    # 4           1978            4  22.0          10.0     18000.0  152.2374
    #             289             4  19.0          28.0      4000.0  194.1858
    # 5           1793            5  18.0          24.0   1000000.0  281.4246
    #             770             5  22.0          16.0     20000.0  248.0490
    # 6           2324            6  20.0           8.0     25000.0  247.0164
    #             1352            6  21.0          20.0      5000.0  141.6486
    # 7           7               7  17.0          42.0     10000.0  212.6022
    #             2271            7  22.0          56.0      3000.0  169.6974
    # 8           3340            8   NaN           NaN         NaN  189.7404
    #             3341            8   NaN           NaN         NaN  287.8128

    # group_keys = False 表示禁用层级索引
    group2 = df.groupby("LeagueIndex", group_keys=False).apply(topk)
    print(group2)
    #       LeagueIndex   Age  HoursPerWeek  TotalHours       APM
    # 2214            1  20.0          12.0       730.0  172.9530
    # 2246            1  27.0           8.0       250.0  141.6282
    # 1753            1  20.0          28.0       100.0  139.6362
    # 3062            2  20.0           6.0       100.0  179.6250
    # 3229            2  16.0          24.0       110.0  156.7380
    # 1520            2  29.0           6.0       250.0  151.6470
    # 1557            3  22.0           6.0       200.0  226.6554
    # 484             3  19.0          42.0       450.0  220.0692
    # 2883            3  16.0           8.0       800.0  208.9500
    # 2688            4  26.0          24.0       990.0  249.0210
    # 1759            4  16.0           6.0        75.0  229.9122
    # 2637            4  23.0          24.0       650.0  227.2272
    # 3277            5  18.0          16.0       950.0  372.6426
    # 93              5  17.0          36.0       720.0  335.4990
    # 202             5  37.0          14.0       800.0  327.7218
    # 734             6  16.0          28.0       730.0  389.8314
    # 2746            6  16.0          28.0      4000.0  350.4114
    # 1810            6  21.0          14.0       730.0  323.2506
    # 3127            7  23.0          42.0      2000.0  298.7952
    # 104             7  21.0          24.0      1000.0  286.4538
    # 1654            7  18.0          98.0       700.0  236.0316
    # 3393            8   NaN           NaN         NaN  375.8664
    # 3373            8   NaN           NaN         NaN  364.8504
    # 3372            8   NaN           NaN         NaN  355.3518


if __name__ == "__main__":
    # test01()
    # test02()
    # test03()
    test04()