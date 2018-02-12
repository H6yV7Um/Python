import urllib.parse
import urllib.request
import random
from lxml import etree

class HupuSpider(object):

    def getUrl(self, begin, end):
        """
        拼接完整的URL
        :param begin:
        :param end:
        :return:
        """

        # 虎扑爆照区URL
        url = "https://bbs.hupu.com/bxj-"
        # 循环爬取页面
        for page in (begin, end+1):
            # 完整url
            full_url = url + str(page)
            print(full_url)
            # 调用加载页面方法
            self.loadPage(full_url)

    def loadPage(self, url):
        """
        获取每个页面的所有帖子
        :param url:
        :return:
        """

        proxy_list = [
            {"http": "113.89.54.209:9999"},
            {"http": "58.220.95.107:8080"},
            {"http": "163.125.17.110:8888"}
        ]
        # 随机选一个
        proxy = random.choice(proxy_list)
        # 创建代理服务器,有代理IP
        httpproxy_handler = urllib.request.ProxyHandler(proxy)
        # 判断
        opener = urllib.request.build_opener(httpproxy_handler)
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1"}
        # 创建请求对象
        request = urllib.request.Request(url, headers=headers)
        # 发送请求并接受数据
        data = opener.open(request).read()
        # 解析HTML文档为XML
        html = etree.HTML(data)
        # print(type(html))
        # xpath表达式匹配数据
        link_list = html.xpath('//div[@class="titlelink box"]/a/@href')
        print(link_list)
        # 循环列表
        for link in link_list:
            # 拼接完整链接
            full_link = "https://bbs.hupu.com" + link
            # 调用加载图片方法
            self.loadImage(full_link)

    def loadImage(self, url):
        """
        获取每个帖子的所有图片
        :param url:
        :return:
        """

        proxy_list = [
            {"http": "113.89.54.209:9999"},
            {"http": "58.220.95.107:8080"},
            {"http": "163.125.17.110:8888"}
        ]
        # 随机选一个
        proxy = random.choice(proxy_list)
        # 创建代理服务器,有代理IP
        httpproxy_handler = urllib.request.ProxyHandler(proxy)
        # 判断
        opener = urllib.request.build_opener(httpproxy_handler)
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1"}
        # 创建请求对象
        request = urllib.request.Request(url, headers=headers)
        # 发送请求并接受数据
        data = opener.open(request).read()
        # 解析HTML文档为XML
        html = etree.HTML(data)
        # xpath表达式匹配数据
        link_list = html.xpath("//p/img/@src")
        # 循环列表
        for link in link_list:
            print(link)
            # 调用下载图片方法
            self.writeImage(link)

    def writeImage(self, url):
        """
        下载图片到本地
        :param url:
        :return:
        """
        proxy_list = [
            {"http": "113.89.54.209:9999"},
            {"http": "58.220.95.107:8080"},
            {"http": "163.125.17.110:8888"}
        ]
        # 随机选一个
        proxy = random.choice(proxy_list)
        # 创建代理服务器,有代理IP
        httpproxy_handler = urllib.request.ProxyHandler(proxy)
        # 判断
        opener = urllib.request.build_opener(httpproxy_handler)
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1"}
        # 创建请求对象
        request = urllib.request.Request(url, headers=headers)
        # 发送请求并接受数据
        image = opener.open(request).read()
        # 给图片命名
        filename = url.split("?")[0][-10:]
        print("正在下载图片 %s" % filename)
        # 保存到本地
        with open('C://Users/Public/Pictures/hupu/' + filename, 'wb') as f:
            f.write(image)


if __name__ == "__main__":
    # 用户输入信息
    begin = int(input("输入起始页: "))
    end = int(input("输入结束页: "))

    s = HupuSpider()
    s.getUrl(begin, end)