# coding=utf-8
"""
NLTK是Python自然语言处理的一个工具包
分类: 根据词性来分(词性标注);名词、形容词、动词等...
分词: 根据语义来分
"""

import nltk
# 调用nltk的包管理工具,可以下载语料库和模型等数据;其中Brown语料库、Punkt分词模型是必装的
# nltk.download()


"""
语料库的使用
"""
def test01():
    # 导入布朗大学
    from nltk.corpus import brown

    # 查看brown语料库
    print(brown.readme())
    # 查看语料库所有句子个数
    print(len(brown.sents()))  # 57340
    # 查看语料库所有单词个数
    print(len(brown.words()))  # 1161192

"""
分词: 英文分词
"""
def test02():
    # 文本样例
    text = "Python is a high-level programming language, and i like it!"
    # 分词处理(需实现安装好punkt分词模型): 返回所有词的列表
    seg_list = nltk.word_tokenize(text)
    print(seg_list)
    # ['Python', 'is', 'a', 'high-level', 'programming', 'language', ',', 'and', 'i', 'like', 'it', '!']

"""
分词: 中文分词
"""
def test03():
    # 可以处理中文分词的工具：jieba分词
    import jieba

    # 原文本
    text = "欢迎来到召唤师峡谷"
    # 1、全模式: 将所有可能出现的词汇全部列出来,返回一个可迭代对象
    res1 = jieba.cut(text, cut_all=True)
    print(type(res1))  # <class 'generator'>
    # 转换成list格式
    print(list(res1))
    # Building prefix dict from the default dictionary ...
    # Dumping model to file cache C:\Users\独行侠CQ\AppData\Local\Temp\jieba.cache
    # Loading model cost 1.371 seconds.
    # ['欢迎', '迎来', '来到', '召唤', '召唤师', '峡谷']
    # Prefix dict has been built succesfully.

    # 2、精确模式: 尽可能按语义进行分词处理
    res2 = jieba.cut(text, cut_all=False)
    print(type(res2))  # <class 'generator'>
    print(list(res2))  # ['欢迎', '来到', '召唤师', '峡谷']

    # 3、搜索引擎模式
    res3 = jieba.cut_for_search(text)
    print(type(res3))  # <class 'generator'>
    print(res3)  # <generator object Tokenizer.cut_for_search at 0x0000026ADDD0C0F8>
    print("|".join(res3))  # 欢迎|来到|召唤|召唤师|峡谷

"""
词形处理: 词干提取
"""
def test04():
    # 1、PorterStemmer
    from nltk.stem.porter import PorterStemmer

    # 创建PorterStemmer对象
    ps = PorterStemmer()
    print(type(ps))  # <class 'nltk.stem.porter.PorterStemmer'>
    print(ps)  # <PorterStemmer>

    # 词干提取
    print(ps.stem("looked"))  # look
    print(ps.stem("looking"))  # look

    # 2、SnowballStemmer
    from nltk.stem.snowball import SnowballStemmer

    # 查看SnowballStemmer支持的语系
    print(SnowballStemmer.languages)  # ('arabic', 'danish', 'dutch', 'english', 'finnish', 'french', 'german', 'hungarian', 'italian', 'norwegian', 'porter', 'portuguese', 'romanian', 'russian', 'spanish', 'swedish')

    # 创建SnowballStemmer对象: 必须先指定语系
    ss = SnowballStemmer("english")
    print(type(ss))  # <class 'nltk.stem.snowball.SnowballStemmer'>
    print(ss)  # <nltk.stem.snowball.SnowballStemmer object at 0x00000272DA64AC50>

    # 词干提取
    print(ss.stem("looked"))  # look
    print(ss.stem("looking"))  # look

    # 3、LancasterStemme
    from nltk.stem.lancaster import LancasterStemmer

    # 创建LancasterStemmer对象
    ls = LancasterStemmer()
    print(type(ls))  # <class 'nltk.stem.lancaster.LancasterStemmer'>
    print(ls)  # <LancasterStemmer>

    # 词干提取
    print(ls.stem("looked"))  # look
    print(ls.stem("looking"))  # look

"""
词形处理: 词形归并
"""
def test05():
    pass


if __name__ == "__main__":
    # test01()
    # test02()
    # test03()
    test04()