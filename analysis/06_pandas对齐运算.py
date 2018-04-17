# coding=utf-8
"""
对齐运算：是数据清洗的重要过程,可以按索引对齐进行运算,如果没对齐的位置则补NaN,最后也可以填充NaN
"""

import numpy as np
import pandas as pd

"""
Series对齐运算
"""

def test01():
    # 创建两个Series对象
    s1 = pd.Series(range(10, 20))
    s2 = pd.Series(range(20, 25))
    print(s1)
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
    print(s2)
    # 0    20
    # 1    21
    # 2    22
    # 3    23
    # 4    24
    # dtype: int64

    # 两个Series对象合并,缺失值以NAN代替
    print(s1.add(s2))  # 等同于print(s1 + s2)
    # 0    30.0
    # 1    32.0
    # 2    34.0
    # 3    36.0
    # 4    38.0
    # 5     NaN
    # 6     NaN
    # 7     NaN
    # 8     NaN
    # 9     NaN
    # dtype: float64

    # 两个Series对象合并,先将缺失值以0.填充再参与运算
    print(s1.add(s2, fill_value=0.))
    # 0    30.0
    # 1    32.0
    # 2    34.0
    # 3    36.0
    # 4    38.0
    # 5    15.0
    # 6    16.0
    # 7    17.0
    # 8    18.0
    # 9    19.0
    # dtype: float64


"""
DataFrame对齐运算
"""

def test02():
    # 创建两个DataFrame对象
    df1 = pd.DataFrame(np.random.rand(2, 3))
    df2 = pd.DataFrame(np.random.rand(3, 4))
    print(df1)
    #           0         1         2
    # 0  0.562746  0.936670  0.960589
    # 1  0.436045  0.647018  0.217559
    print(df2)
    #           0         1         2         3
    # 0  0.574791  0.378391  0.686065  0.028149
    # 1  0.267706  0.593127  0.561548  0.346504
    # 2  0.768704  0.416898  0.907734  0.030335

    # 两个DataFrame对象合并,缺失值以NAN代替
    print(df1.add(df2))
    #           0         1         2   3
    # 0  1.137536  1.315061  1.646654 NaN
    # 1  0.703751  1.240145  0.779107 NaN
    # 2       NaN       NaN       NaN NaN

    # 两个DataFrame对象合并,先将缺失值以0.填充再参与运算
    print(df1.add(df2, fill_value=0.))
    #           0         1         2         3
    # 0  1.137536  1.315061  1.646654  0.028149
    # 1  0.703751  1.240145  0.779107  0.346504
    # 2  0.768704  0.416898  0.907734  0.030335



if __name__ == "__main__":
    # test01()
    test02()
