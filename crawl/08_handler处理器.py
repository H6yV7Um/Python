# coding=utf-8
"""
urlopen()不支持代理和cookie等http/https高级功能的问题:
解决方案: 使用相关handler处理器来创建特定功能的处理器对象(其实urlopen也是一个特殊的opener)

1、通过urllib.request模块创建相关handler处理器对象
2、通过urllib.request模块的build_opener()方法使用这些处理器对象,创建自定义opener对象
3、opener对象调用open()方法发送http请求
"""

import urllib.request
import random

"""
HTTPHandler处理器
"""
# # 创建httphandler处理器,专门处理http请求
# # debuglevel参数默认0,设为1会自动打开Debug log模式,程序执行时会打印收发包信息,方便调试
# http_handler = urllib.request.HTTPHandler(debuglevel=1)
# # 创建opener对象
# opener = urllib.request.build_opener(http_handler)
# # 创建request对象
# request = urllib.request.Request("http://www.baidu.com/")
# # 调用open()方法发送请求
# response = opener.open(request)
# # 输出结果
# print(response.read().decode("utf-8"))

"""
ProxyHandler处理器: 使用代理IP,针对反爬虫
很多网站会通过检测某一时段内IP的访问次数(流量统计、系统日志等),将不正常的IP封掉
所以我们可以设置一些代理服务器,每隔一段时间换一个代理,就算IP被禁止,依然可以换个IP继续爬取
"""
# 代理IP列表
proxy_list = [
    {"http": "113.89.54.209:9999"},
    {"http": "58.220.95.107:8080"},
    {"http": "163.125.17.110:8888"}
]
# 随机选一个
proxy = random.choice(proxy_list)
# 创建代理服务器,有代理IP
httpproxy_handler = urllib.request.ProxyHandler(proxy)
# 创建代理服务器,没有代理IP
noproxy_handler = urllib.request.ProxyHandler({})
# 设置开关
proxySwitch = True
# 判断
if proxySwitch:
    opener = urllib.request.build_opener(httpproxy_handler)
else:
    opener = urllib.request.build_opener(noproxy_handler)
# 创建request对象
request = urllib.request.Request("http://www.baidu.com")
# 发送请求(此时只有opener.open()方法才会使用代理,而urlopen()方法不会使用代理)
response = opener.open(request)
# opener全局设置(此时不管opener.open()还是urlopen()都会使用代理)
urllib.request.install_opener(opener)
# 输出结果
print(response.read().decode("utf-8"))

"""
但是免费代理有很大缺陷,可以花钱买专门的代理,通过用户名/密码授权使用
urllib.request模块:
HTTPPasswordMgrWithDefaultRealm(): 保存私密代理的用户密码
ProxyBasicAuthHandler(): 处理代理的身份验证。
"""
# # 用户和密码
# user = "test"
# passwd = "test"
# # 代理服务器
# proxy = "163.125.17.110:8888"
# # 创建密码管理对象
# passwdMgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
# # 添加账户信息(第一个参数realm是与远程服务器相关的域信息,一般写None,后面三个参数分别是: 代理服务器、用户名、密码)
# passwdMgr.add_password(None, proxy, user, passwd)
# # 创建代理基础用户名/密码的处理器对象
# proxyauth_handler = urllib.request.ProxyBasicAuthHandler(passwdMgr)
# # 创建opener对象
# opener = urllib.request.build_opener(proxyauth_handler)
# # 创建request对象
# request = urllib.request.Request("http://www.baidu.com")
# # 发送请求
# response = opener.open(request)
# # 输出结果
# print(response.read().decode("utf-8"))