""""
HTML(Hyper Text Markup Language): 超文本标记语言;显示数据
XML(Extensible Markup Language): 可扩展标记语言;传输和存储数据
HTML DOM(Document Object Model for HTML): 文档对象模型;可以访问所有HTML元素
XPath(XML Path Language): 是一种在XML文档中查找信息的语言;可以遍历XML文档中的属性和元素
lxml库: 是一个HTML/XML解析器;用来解析和提取HTML/XML数据
掌握要点: XPath语法(可结合XMLQuire工具调试)
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
        headers = {"User-Agent": "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11"}
        # 创建请求对象
        request = urllib.request.Request(url, headers=headers)
        # 发送请求,从服务器接收数据
        html = urllib.request.urlopen(request).read().decode("utf-8")
        # 将HTML页面转为HTML DOM模型
        content = etree.HTML(html)
        print(type(content))

        # 获取匹配到的帖子链接列表
        link_list = content.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href')
        # link_list = content.xpath('//a[@class="j_th_tit"]/@href')
        print(link_list)

        # 循环列表
        for link in link_list:
            print(link)
            # 拼接完整帖子链接
            fulllink = "http://tieba.baidu.com" + link
            print(fulllink)

            # 调用加载图片方法
            self.loadImage(fulllink)

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
        html = urllib.request.urlopen(request).read().decode("utf-8")
        # 将HTML页面转为HTML DOM模型
        content = etree.HTML(html)
        # 获取匹配到的图片链接列表
        link_list = content.xpath('//div/img[@class="BDE_Image"]/@src')
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
        # 保存到本地文件
        f = open("D://filename", "wb")
        f.write(image)
        f.close()
        print("正在下载图片 %s" % filename)


if __name__ == "__main__":
    # 用户输入信息
    name = input("输入贴吧名称: ")
    begin = int(input("输入起始页: "))
    end = int(input("输入结束页: "))

    s = Spider()
    s.getURL(name, begin, end)
