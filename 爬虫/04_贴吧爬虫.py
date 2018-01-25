import urllib.request
import urllib.parse

"""
需求: 爬取百度贴吧数据
三步骤: 拼接url -- 获取html页面 -- 保存到本地 
"""


def loadPage(url, filename):
    """
    作用: 根据url发送请求,获取服务器响应文件
    :param url: 待爬取url地址
    :return: html页面
    """

    # 提示信息
    print("正在下载: " + filename)
    ua_header = {"User-Agent": "Mozilla....."}
    request = urllib.request.Request(url, headers=ua_header)
    response = urllib.request.urlopen(request)
    return response.read()


def writePage(html, filename):
    """
    作用: 将爬取的html页面存储到本地文件
    :param html: 服务器相应的html页面
    :return:
    """

    # 提示信息
    print("正在保存: " + filename)
    # 写入文件
    f = open("D://" + filename, "w")
    f.write(str(html))


def spider(url, begin, end):
    """
    作用: 拼接完整的url
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
        # 提示信息
        print("谢谢使用！")


if __name__ == "__main__":
    # 用户输入信息
    keyword = input("输入贴吧名称:")
    begin = int(input("起始页:"))
    end = int(input("结束页:"))

    # url处理
    url = "http://tieba.baidu.com/f"
    kw = urllib.parse.urlencode({"kw": keyword})
    fullurl = url + "?" + kw

    # 爬取页面
    spider(fullurl, begin, end)
