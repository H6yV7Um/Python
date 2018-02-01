import urllib.request
import re
import random
import chardet


class Spider(object):
    # 爬取数据
    def loadPage(self, page):

        # 待爬取url
        url = "http://www.neihanpa.com/article/list_5_" + str(page) + ".html"
        # http请求头
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36"}
        # 创建请求对象
        request = urllib.request.Request(url, headers=headers)

        # 使用代理IP
        proxy_list = [
            {"http": "113.89.54.209:9999"},
            {"http": "61.50.244.179:808"},
            {"http": "58.220.95.107:8080"}
        ]
        proxy = random.choice(proxy_list)
        proxy_handler = urllib.request.ProxyHandler(proxy)
        opener = urllib.request.build_opener(proxy_handler)
        response = opener.open(request)

        # 发送请求
        # response = urllib.request.urlopen(request)

        # chardet可以测试网页编码
        # res = chardet.detect(response.read())
        # print(res)  # {'language': 'Chinese', 'confidence': 0.99, 'encoding': 'GB2312'}

        # 爬网页的时候要注意网页源码的charset,乱码时要用decode()做解码
        # ignore参数表示忽略非gb2312编码的字符,因为网站可能会注入少量其它字符
        html = response.read().decode("gb2312", "ignore")
        print(type(html))  # <class 'str'>
        # print(html)

        # 使用正则过滤数据
        pattern = re.compile('<div class="f18 mb20">(.*?)</div>', re.S)
        result = pattern.findall(html)
        print(type(result))  # <class 'list'>
        # print(result)
        print("*****正在爬取第 %d 页数据*****" % page)
        for item in result:
            item = item.replace("<p>", "").replace("</p>", "").replace("<br />", "")
            self.writeToFile(item)

    # 保存到本地
    def writeToFile(self, item):
        f = open("C://users/qmtv/data.txt", "a", encoding="utf-8")
        f.write(item)
        f.write("=" * 100)
        f.close()

    # 循环爬取
    def work(self, page):
        while True:
            self.loadPage(page)
            page += 1


if __name__ == "__main__":
    s = Spider()
    # s.loadPage(1)
    s.work(1)
