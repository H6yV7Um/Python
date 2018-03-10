"""
需求: 爬取百度贴吧数据
三步骤: 拼接url -- 获取html页面 -- 保存到本地
"""

import urllib.request
import urllib.parse

def spider(url, begin, end):
    """
    作用: 拼接完整的url,向服务器发送http请求获取数据,然后保存到本地
    :param url: url前面部分
    :param begin: 起始页
    :param end: 结束页
    :return:
    """

    for page in range(begin, end + 1):
        # url尾部pn值处理
        pn = (page - 1) * 50
        # 打印文件名
        filename = "第" + str(page) + "页.html"
        # 继续拼接完整的url
        fullurl = url + "&pn=" + str(pn)
        # 输出完整url
        print(fullurl)
        # 根据url向服务器获取html页面
        html = loadPage(fullurl, filename)
        # 输出页面
        print(html)
        # 将html页面保存到本地
        writePage(html, filename)


def loadPage(url, filename):
    """
    作用: 根据url发送请求,获取服务器响应文件
    :param url: 待爬取url地址
    :return: html页面
    """

    # 提示信息
    print("正在下载: " + filename)
    # http报头
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1"}
    # 构造请求对象
    request = urllib.request.Request(url, headers=headers)
    # 向服务器发送请求
    response = urllib.request.urlopen(request)
    # 服务器响应内容
    html = response.read()
    # 看下数据类型
    print(type(html))  # <class 'bytes'>
    # 转成utf-8格式的字符串
    return html.decode("utf-8")


def writePage(html, filename):
    """
    作用: 将爬取的html页面存储到本地文件
    :param html: 服务器相应的html页面
    :return:
    """

    # 提示信息
    print("正在保存: " + filename)
    # 打开文件,指定模式和编码
    f = open("C://users/qmtv/" + filename, "w", encoding="utf-8")
    # 写入数据
    f.write(html)
    # 关闭文件
    f.close()


if __name__ == "__main__":
    # 用户接口输入信息
    keyword = input("输入贴吧名称:")
    begin = int(input("起始页:"))
    end = int(input("结束页:"))

    # url处理
    url = "http://tieba.baidu.com/f"
    kw = urllib.parse.urlencode({"kw": keyword})
    fullurl = url + "?" + kw

    # 爬取页面
    spider(fullurl, begin, end)
