""""
HTML(Hyper Text Markup Language): 超文本标记语言 ---> 展示数据
XML(Extensible Markup Language): 可扩展标记语言 ---> 传输和存储数据,可以持久化
HTML DOM(Document Object Model for HTML): 文档对象模型 ---> 访问和操作HTML文档
XPath(XML Path Language): 是一种在XML文档中查找信息的语言 ---> 遍历XML文档中的元素和属性
                          XPath使用路径表达式来选取XML文档中的节点或者节点集
lxml库: 是一款高性能的HTML/XML解析器 ---> 用来解析和提取HTML/XML数据
掌握要点: XPath语法(可结合XPath表达式编辑工具XMLQuire/Chrome插件XPath Helper调试)
etree.HTML(): 将字符串解析为HTML文档
etree.tostring(): 将元素序列化为其XML树编码的字符串表示
"""

import urllib.parse
import urllib.request
import random
from lxml import etree


# 爬取贴吧中的图片
class Spider(object):

    def getURL(self, name, begin, end):
        """
        拼接完整的贴吧URL
        :return:
        """

        # 待爬取URL
        url = "https://tieba.baidu.com/f"
        # 对贴吧名称做URL转码
        kw = urllib.parse.urlencode({"kw": name})
        # print(kw)

        # 遍历循环贴吧所有页面
        for page in range(begin, end + 1):
            # URL尾部pn参数
            pn = (page - 1) * 50
            # 拼接完整的URL
            fullurl = url + "?" + kw + "&pn=" + str(pn)
            # print(fullurl)

            # 调用加载页面方法
            self.loadPage(fullurl)

    def loadPage(self, url):
        """
        获取贴吧里所有帖子的链接
        :return:
        """

        # # HTTP请求头
        # ua_list = [
        #     {"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1"},
        #     {"Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1"},
        #     {"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11"},
        #     {"Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11"}
        # ]
        # # 随机选一个
        # headers = random.choice(ua_list)

        headers = {"User-Agent": "User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"}
        # 创建请求对象
        request = urllib.request.Request(url, headers=headers)
        # 发送请求,从服务器接收数据
        data = urllib.request.urlopen(request).read().decode("utf-8")
        # print(type(data))  # str
        # print(data)

        # 解析HTML文档为HTML DOM(XML)模型
        html = etree.HTML(data)
        # print(type(html))  # <class 'lxml.etree._Element'>
        # xpath表达式解析XML,获取匹配到的帖子链接列表
        link_list = html.xpath('//div[@class="threadlist_lz clearfix"]/div/a[@rel="noreferrer"]/@href')
        print(type(link_list))  # <class 'list'>
        print(link_list)

        # 遍历列表
        for link in link_list:
            # 拼接完整帖子链接
            full_link = "http://tieba.baidu.com" + link
            print(full_link)
            # 调用加载图片方法
            self.loadImage(full_link)

    def loadImage(self, url):
        """
        获取每个帖子里所有图片的链接
        :return:
        """

        # http请求头
        headers = {"User-Agent": "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11"}
        # 创建请求对象
        request = urllib.request.Request(url, headers=headers)
        # 发送请求,从服务器接收数据
        data = urllib.request.urlopen(request).read().decode("utf-8")

        # 解析HTML文档为HTML DOM(XML)模型
        html = etree.HTML(data)
        # xpath表达式解析XML,获取匹配到的图片链接列表
        link_list = html.xpath('//div/img[@class="BDE_Image"]/@src')
        # link_list = content.xpath('//div[@class="post_bubble_middle"]')
        print(link_list)

        # 循环列表
        for link in link_list:
            print(link)
            # 调用保存图片方法
            self.writeImage(link)

    def writeImage(self, url):
        """
        下载图片
        :return:
        """

        # http请求头
        headers = {"User-Agent": "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11"}
        # 创建请求对象
        request = urllib.request.Request(url, headers=headers)
        # 发送请求,从服务器接收数据
        image = urllib.request.urlopen(request).read()
        # 给每个图片命名
        filename = url[-10:]
        # 保存到本地
        print("正在下载图片 %s" % filename)
        with open(filename, "wb") as f:
        # f = open("D://filename", "wb")
            f.write(image)
        # f.close()


if __name__ == "__main__":
    # 用户输入信息
    name = input("输入贴吧名称: ")
    begin = int(input("输入起始页: "))
    end = int(input("输入结束页: "))

    s = Spider()
    s.getURL(name, begin, end)
