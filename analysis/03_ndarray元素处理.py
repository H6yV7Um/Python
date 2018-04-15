# coding=utf-8
import numpy as np

"""
元素计算函数: 
np.ceil(): 向上取整,参数是 number 或 array
np.floor(): 向下取整,参数是 number 或 array
np.abs(): 元素的绝对值,参数是 number 或 array
np.rint(): 四舍五入,参数是 number 或 array
np.isnan(): 判断元素是否为 NaN(Not a Number),参数是 number 或 array
np.multiply(): 元素相乘,参数是 number 或 array
np.divide(): 元素相除,参数是 number 或 array
np.where(condition, x, y): 三元运算符,if condition x else y
"""

def test01(): 
    # 创建一个指定区间的浮点型二维数组
    arr = np.random.uniform(-10, 10, (2, 3))
    print(arr)
    # 元素向上取整
    print(np.ceil(arr))
    # 元素向下取整
    print(np.floor(arr))
    # 元素取绝对值
    print(np.abs(arr))
    # 元素取四舍五入值
    print(np.rint(arr))
    # 创建一个nan值
    num = np.nan
    print(num)  # nan
    print(np.isnan(num))  # True
    # 判断是否是nan值
    print(np.isnan(arr))  # [[False False False][False False False]]
    # 元素相乘
    print(np.multiply(10, arr))  # 等价于print(10 * arr)
    # 元素相除
    print(np.divide(arr, 10))  # 等价于print(arr / 10)
    # 三元表达式
    print(np.where(arr > 1, 100, 200))


"""
元素统计函数: 
np.mean(), np.sum(): 所有元素的平均值/和,参数是 number 或 array
np.max(), np.min(): 所有元素的最大值/最小值,参数是 number 或 array
np.std(), np.var(): 所有元素的标准差/方差,参数是 number 或 array;  用来衡量数据和期望值的偏移量
np.argmax(), np.argmin(): 最大/小值的索引值,参数是 number 或 array
np.cumsum(), np.cumprod(): 返回一个一维数组,每个元素都是之前所有元素的累加和/累乘积,参数是 number 或 array
注意: 统计多维数组时默认统计全部维度,默认是axis=0(按列),axis=1(按行)
"""

def test02():
    # 创建一个指定区间的整形二维数组
    arr = np.random.randint(1, 10, (3, 4))
    print(arr)
    # 默认求全部元素平均值
    print(np.mean(arr))
    # 也可以求指定区间平均值
    print(np.mean(arr[1][1:3]))
    # 默认求所有元素的和
    print(np.sum(arr))
    print("=" * 30)
    # 按列/行求和
    print(np.sum(arr, axis=0))
    print(np.sum(arr, axis=1))
    # 默认求所有元素的最大值
    print(np.max(arr))
    #  默认求所有元素的最小值
    print(np.min(arr))
    # 标准差: 所有数据分别和平均数的差的和的平均数
    print(np.std(arr))
    # 方差: 所有数据分别和平均数的差的平方的和的平均数
    print(np.var(arr))
    # 数组里最大值的下标值(如果有多个重复数据取第一个)
    print(np.argmax(arr))
    # 数组里最小值的下标值
    print(np.argmin(arr))
    # 返回一个一维数组,每个元素都是当前元素和前面所有元素的累加和
    print(np.cumsum(arr))
    print(np.cumsum(arr).reshape(4, 3))
    # 返回一个一维数组,每个元素都是当前元素和前面所有元素的累乘积
    print(np.cumprod(arr))
    # 按列计算
    print(np.cumprod(arr, axis=0))


"""
元素判断函数: 
np.any(): 至少有一个元素满足指定条件,返回True
np.all(): 所有的元素满足指定条件,返回True
"""

def test03():
    # 创建一个正态分布随机抽样数组
    arr = np.random.randn(10000)
    print(arr)
    print(np.any(arr > 0))  # True
    print(np.all(arr > 0))  # False


"""
元素去重排序函数: 
np.unique(): 去除重复值并返回排序后的结果,类似Python的set
"""

def test04():
    arr = np.array([[1, 2, 3, 4], [2, 3, 4, 5]])
    print(arr)  # [[1 2 3 4][2 3 4 5]]
    print(np.unique(arr))  # [1 2 3 4 5]


if __name__ == "__main__": 
    # test01()
    # test02()
    # test03()
    test04()