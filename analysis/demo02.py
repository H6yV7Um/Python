# coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt
import zipfile
import os

# 手动实现分组功能
def test01():
    filename = "D://FoodFacts.csv"
    # 加载文件并删除nan值
    df = pd.read_csv(filename, usecols=["countries_en", "additives_n"], encoding="gbk").dropna()
    print(type(df))  # <class 'pandas.core.frame.DataFrame'>
    # print(df.head(10))

    # 分别取出国家和添加剂列的值
    country_list = df["countries_en"].values
    add_list = df["additives_n"].values
    print(country_list)
    print(add_list)
    # 以国家列表为索引组成新的Series对象
    ser = pd.Series(add_list, index=country_list)
    print(ser.head(10))

    # 对国家做去重
    country_set = set(country_list)
    print(country_set)

    # 字典生成器
    dict = {country: ser[country].mean() for country in country_set}
    print(dict)
    print(dict["France"])

    # 再对每个国家的数据做统计
    ser1 = pd.Series(dict).sort_values(ascending=False)
    print(ser1.head(10))

    # 取前10做图
    ser1[:10].plot.bar()
    plt.show()


# groupby实现
def test02():
    # zip压缩文件所在目录
    data_path = "D://"
    zipfile_path = "open-food-facts.zip"
    fullzipfile = os.path.join(data_path, zipfile_path)
    print(fullzipfile)  # D://open-food-facts.zip

    # 打开zip压缩文件,读取文件信息
    with zipfile.ZipFile(fullzipfile) as f:
        # f.namelist()返回的是zip压缩文件里所有文件名的列表
        csvfile = f.namelist()[0]
        print(csvfile)  # FoodFacts.csv

    # 获取csv文件全路径
    csvfile_path = os.path.join(data_path, csvfile)
    print(csvfile_path)  # D://FoodFacts.csv

    # 解压zip压缩文件到指定path下
    with zipfile.ZipFile(fullzipfile) as f:
        f.extractall(path=data_path)

    # 加载csv文件并删除nan值
    df = pd.read_csv(csvfile_path, usecols=["countries_en", "additives_n"], encoding="gbk").dropna()
    print(type(df))  # <class 'pandas.core.frame.DataFrame'>
    print(df.head(10))

    # 取出添加剂列的数据并按国家列分组,返回groupby对象
    group = df["additives_n"].groupby(df["countries_en"])
    print(group)  # <pandas.core.groupby.SeriesGroupBy object at 0x00000176E3A2FE48>
    print(type(group))  # <class 'pandas.core.groupby.SeriesGroupBy'>

    # 对groupby对象做统计处理
    data = group.mean().sort_values(ascending=False)[:10]
    data.index.name = "country"
    print(type(data))  # <class 'pandas.core.series.Series'>
    print(data)

    # 画图
    data.plot.bar()

    # 显示绘图结果
    plt.show()

if __name__ == "__main__":
    # test01()
    test02()