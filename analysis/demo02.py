# coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt

filename = "D://FoodFacts.csv"

# 手动实现分组功能
def test01():
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
    # 加载文件并删除nan值
    df = pd.read_csv(filename, usecols=["countries_en", "additives_n"], encoding="gbk").dropna()
    print(type(df))  # <class 'pandas.core.frame.DataFrame'>
    print(df.head(10))

    # 取出添加剂列的数据并按国家分组,返回groupby对象
    groupby_obj = df["additives_n"].groupby(df["countries_en"])
    print(groupby_obj)  # <pandas.core.groupby.SeriesGroupBy object at 0x00000176E3A2FE48>
    print(type(groupby_obj))  # <class 'pandas.core.groupby.SeriesGroupBy'>

    # 对groupby对象做统计处理
    data = groupby_obj.mean().sort_values(ascending=False)[:10]
    data.index.name = "country"
    print(data)

    # 画图
    data.plot.bar()
    plt.show()

if __name__ == "__main__":
    # test01()
    test02()