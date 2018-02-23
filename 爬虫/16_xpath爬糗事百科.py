"""
需求: 获取糗事百科每个帖子里的用户头像链接、用户姓名、段子内容、点赞次数和评论次数并保存到json文件
"""

import requests
from lxml import etree
import json

class Qiushibaike(object):
    def getUrl(self, begin, end):
        """
        获取完整URL
        :param begin:
        :param end:
        :return:
        """

        # 糗事百科URL
        url = "https://www.qiushibaike.com/8hr/page/"
        # 循环爬取页面
        for page in range(begin, end+1):
            # 完整URL
            full_url = url + str(page)
            print(full_url)
            # 调用加载页面方法
            self.loadPage(full_url)

    def loadPage(self, url):
        # 请求头
        headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"}
        # 发送get请求
        response = requests.get(url,headers=headers)
        # 获取数据
        text = response.text
        # print(type(text))  # <class 'str'>
        # content = response.content
        # print(type(content))  # <class 'bytes'>
        # 解析HTML文档为HTML DOM(XML)模型
        html = etree.HTML(text)
        # 返回所有段子的结点位置,contains()模糊查询: 第一个参数是要匹配的标签,第二个参数是标签名部分内容
        node_list = html.xpath('//div[contains(@id, "qiushi_tag")]')
        # print(node_list)
        # print(type(node_list))  # <class 'list'>
        # 定义一个空字典
        items = {}
        # 遍历列表
        for node in node_list:
            # 用户头像链接(xpath表达式返回的是list,加索引取出数据)
            imgurl = html.xpath('//div[@class="author clearfix"]//img/@src')[0]
            print(imgurl)
            print(type(imgurl))
            # 用户姓名
            username = html.xpath('//div[@class="author clearfix"]//h2')[0].text
            print(username)
            print(type(username))
            # 段子内容
            content = html.xpath('//div[@class="content"]/span')[0].text
            print(content)
            print(type(content))
            # 点赞次数
            vote = html.xpath('//span[@class="stats-vote"]/i')[0].text
            print(vote)
            print(type(vote))
            # 评论次数
            comments = html.xpath('//span[@class="stats-comments"]//i')[0].text
            print(comments)
            print(type(comments))
            # 往字典添加数据
            items = {
                "imgurl": imgurl,
                "username": username,
                "content": content,
                "vote": vote,
                "comments": comments
            }
            # 将Python对象序列化成Json字符串
            obj = json.dumps(items, ensure_ascii=False)
        # 写入本地文件
        with open("C://Users/Public/Downloads/qiubai.json", "a") as f:
            f.write(obj + "\n")


if __name__ == "__main__":
    # 用户输入信息
    begin = int(input("输入起始页: "))
    end = int(input("输入结束页: "))
    q = Qiushibaike()
    q.getUrl(begin, end)