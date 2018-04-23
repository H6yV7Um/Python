# coding=utf-8
"""
注意: 使用etree.HTML()时,如果response.encoding不是utf-8后面response.text可能会乱码,这时可以用response.content代替
content = response.content
html = etree.HTML(content)
res_list = html.xpath("***")

报错: SyntaxError: Non-UTF-8 code starting with '\xe5' on line 67, but no encoding declared;
原因: Python默认编码是ASCII,代码中出现中文字符就会报错,在python文件首行加上# coding=utf-8即可
"""

import requests
from lxml import etree
import jieba
# Counter类用于统计元素个数
from collections import Counter

def crawl():
    """
    数据抓取
    :return:
    """
    # 链接
    url = "http://www.gov.cn/premier/2017-03/16/content_5177940.htm"
    # 请求头
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"}
    # 发送get请求
    response = requests.get(url, headers=headers)
    print(response.encoding)  # ISO-8859-1
    # 获取数据
    content = response.content
    # 解析HTML文档
    html = etree.HTML(content)
    print(type(html))  # <class 'lxml.etree._Element'>
    # 使用xpath表达式
    res_list = html.xpath("//p | //span")

    data = ""
    # 遍历列表
    for res in res_list:
        if res.text is not None:
            data += res.text
    # 返回最终结果
    return data

def statistics(text):
    """
    数据统计
    :return:
    """
    # 1、先做分词
    seg_list = jieba.cut(text, cut_all=True)
    print(type(seg_list))  # <class 'generator'>

    # 读取中文停用词库
    filename = "D://中文停用词库.txt"
    # 将停用词库处理为列表
    stopword_list = [line.strip() for line in open(filename, "r", encoding="utf-8")]
    print(stopword_list)

    # 2、停用词处理
    word_list = [seg for seg in seg_list if seg not in stopword_list and seg != ""]
    print(word_list)

    # 3、词频统计Counter(): 返回Counter({k1: v1, k2: v2, k3: v3...})并按value值降序排序
    wc = Counter(word_list)
    print(type(wc))  # <class 'collections.Counter'>
    print(wc)  # Counter({'发展': 134, '改革': 85, '经济': 71, '推进': 66...})

    # wc.most_common()将Counter({k1: v1, k2: v2...})转换成列表[(k1, v1),(k2, v2)...],参数n相当于topN
    res = wc.most_common(n=10)
    print(type(res))  # <class 'list'>
    print(res)  # [('发展', 134), ('改革', 85), ('经济', 71), ('推进', 66)...]

    # 遍历结果
    for key, value in res:
        print(key, value)
    # 发展 134
    # 改革 85
    # 经济 71
    # 推进 66
    # 建设 59
    # 社会 49
    # 政策 46
    # 企业 46
    # 加强 46
    # 人民 45


if __name__ == "__main__":
    text = crawl()
    statistics(text)