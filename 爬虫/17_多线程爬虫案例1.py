"""
多线程爬虫:
page_queue: 页码队列(page页码)
data_queue: 采集队列(html源码)
CrawlThread: 采集线程
ParseThread: 解析线程

Queue(maxsize): Create a queue object with a given maximum size
"""

from threading import Thread, Lock
from queue import Queue
import requests
from lxml import etree
import json


def main():
    # 页面队列(限定20页)
    page_queue = Queue(maxsize=20)
    # 采集队列(页面的html源码,参数为空表示不限制大小)
    data_queue = Queue()
    # 创建锁对象
    lock = Lock()
    # 采集线程名称
    crawl_list = ['carwl-1', 'carwl-2', 'carwl-3']
    # 存放采集线程的列表

    # 解析线程名称
    parse_list = ['parse-1', 'parse-2', 'parse-3']


if __name__ == "__main__":
    main()