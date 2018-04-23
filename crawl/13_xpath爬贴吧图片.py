""""
HTML(Hyper Text Markup Language): 超文本标记语言 ---> 展示数据
XML(Extensible Markup Language): 可扩展标记语言 ---> 传输和存储数据,可以持久化
HTML DOM(Document Object Model for HTML): 文档对象模型 ---> 访问和操作HTML文档
XPath(XML Path Language): 是一种在XML文档中查找信息的语言 ---> 遍历XML文档中的元素和属性
                          XPath使用路径表达式来选取XML文档中的节点或者节点集
注意: 在chrome里用xpath helper能匹配到数据,但是在程序里可能匹配不到,因为有些网站对不同浏览器显示不同的页面;
     此时要换成IE内核的浏览器: 遨游、世界之窗、360浏览器、腾讯浏览器、搜狗浏览器、Green Browser等
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
class TiebaSpider(object):

    def getURL(self, name, begin, end):
        """
        拼接完整的URL
        :return:
        """

        # 贴吧URL
        url = "https://tieba.baidu.com/f"
        # 对贴吧名称做URL转码
        kw = urllib.parse.urlencode({"kw": name})
        print(kw)

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

        # HTTP请求头
        ua_list = [
            {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"},
            {"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"},
            {"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)"},
            {"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)"},
            {"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)"},
            {"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)"},
            {"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)"}
        ]
        # 随机选一个
        headers = random.choice(ua_list)

        # 创建请求对象
        request = urllib.request.Request(url, headers=headers)
        # 发送请求,从服务器接收数据
        data = urllib.request.urlopen(request).read()
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
        data = urllib.request.urlopen(request).read()
        # print(type(data))  # <class 'bytes'>

        # 解析HTML文档为HTML DOM(XML)模型
        html = etree.HTML(data)
        # xpath表达式解析XML,获取匹配到的图片链接列表
        link_list = html.xpath('//div/img[@class="BDE_Image"]/@src')
        print(link_list)

        # 遍历列表
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
        filename = url[-9:]
        # 保存到本地
        print("正在下载图片 %s" % filename)
        # with open()会自动调用close()方法
        with open('D://tieba/' + filename, 'wb') as f:
            f.write(image)


if __name__ == "__main__":
    # 用户输入信息
    name = input("输入贴吧名称: ")
    begin = int(input("输入起始页: "))
    end = int(input("输入结束页: "))

    s = TiebaSpider()
    s.getURL(name, begin, end)
