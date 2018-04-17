# coding=utf-8
"""
np.genfromtxt(): 从外部加载.csv文件
注意: fname参数最好是已经加载到项目中的文件,np.genfromtxt()可能读不到外部路径
"""

import numpy as np

# 加载文件
filename = "presidential_polls.csv"
with open(filename, "r") as f:
    # 读取第一行表头数据(最后一列是换行符)
    columns = f.readline()[:-1]
    print(columns)

# 将表头字段切割成列表
names = columns.split(",")
print(names)

# 待统计字段
col_list = "matchup,adjpoll_clinton,adjpoll_trump,adjpoll_johnson".split(",")
print(col_list)

# 获取指定列的索引
col_index = [names.index(col) for col in col_list]
print(col_index)

# 将字段和对应的数据加载到程序中
arr = np.genfromtxt(
    fname=filename,  # 文件名
    dtype=str,  # 数据类型(原始数据包含字母和数字,先给str)
    delimiter=",",  # 字段分隔符
    usecols=col_index  # 指定列的索引值
)
print(arr)

# 取出表格的数据部分
arr1 = arr[1:, 1:]

# 数据清洗,将空字符串替换成0.
arr1 = np.where(arr1 == "", "0.", arr1)
print(arr1)

# 转换str数据类型为float
arr1 = arr1.astype(float)
print(arr1.dtype)

# 统计三个候选人的票数
print("%s: %.2f" % (arr[0][1], np.sum(arr1[:, 0:1], axis=0)))
print("%s: %.2f" % (arr[0][2], np.sum(arr1[:, 1:2], axis=0)))
print("%s: %.2f" % (arr[0][3], np.sum(arr1[:, 2:3], axis=0)))
