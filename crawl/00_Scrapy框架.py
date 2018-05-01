# coding=utf-8
"""
Scrapy是用纯Python编写的应用框架，用于爬取网站数据、提取结构性数据
Scrapy使用了Twisted(主要对手Tornado)异步网络框架处理网络通讯，可以加快下载速度，并且包含各种中间件接口

Windows安装Scrapy：
直接安装很麻烦，要手动安装很多模块(巨多坑)，所以选择用anaconda安装
以管理员身份运行anaconda prompt：conda install scrapy一步搞定
测试：
(base) C:\Windows\System32>scrapy
Scrapy 1.5.0 - no active project

Usage:
  scrapy <command> [options] [args]

Available commands:
  bench         Run quick benchmark test
  fetch         Fetch a URL using the Scrapy downloader
  genspider     Generate new spider using pre-defined templates
  runspider     Run a self-contained spider (without creating a project)
  settings      Get settings values
  shell         Interactive scraping console
  startproject  Create new project
  version       Print Scrapy version
  view          Open URL in browser, as seen by Scrapy
  [ more ]      More commands available when run from project directory
Use "scrapy <command> -h" to see more info about a command

Scrapy项目步骤：
1、新建项目：scrapy startproject myspider(项目名称)
|---myspider
    |---myspider                    # 项目的Python模块，将会从这里引用代码
    |   |---__init__.py
    |   |---items.py                # 项目的目标文件
    |   |---pipelines.py            # 项目的管道文件
    |   |---settings.py             # 项目的设置文件
    |   |---spiders                 # 存放爬虫代码的目录
    |       |---__init__.py
    |---scrapy.cfg                  # 项目的配置文件

2、明确目标(编写items.py)：设置需要保存的数据字段

3、制作爬虫(spiders/xxx.py)：爬取数据
  scrapy genspider itcast(爬虫名称) "www.itcast.cn"(网站域名)：可生成模板

4、存储内容(pipelines.py)：设计管道存储爬取内容，存入文件或数据库
  当Item在Spider中被收集之后，它将会被传递到Item Pipeline，这些Item Pipeline组件按定义的顺序处理Item

运行：scrapy crawl ***
     scrapy crawl *** -o json/csv/xml

将myspider项目导入到pycharm运行，并选择装有scrapy框架的Anaconda3作为Project Interpreter
"""