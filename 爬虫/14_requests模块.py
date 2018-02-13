"""
Requests: 基于urllib3实现,继承了urllib2的所有特性,并且支持HTTP连接保持和连接池,支持使用cookie保持会话
          支持文件上传,支持自动确定响应内容的编码,支持国际化的URL和POST数据自动编码
"""

import requests
import random

"""
get请求
"""
def get():
    # 请求地址
    url = "https://www.baidu.com/s?"
    # 请求头
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1"}
    # 参数
    params = {"wd": "知乎"}
    # 发送get请求(params接收字典/字符串的查询参数,字典类型自动转换为url编码,不需要urlencode())
    response = requests.get(url, params=params, headers=headers)
    # 查看响应数据类型
    print(type(response))  # <class 'requests.models.Response'>
    print(response)  # <Response [200]>
    # 查看请求方式
    print(response.request)  # <PreparedRequest [GET]>
    # 查看完整url地址
    print(response.url)  # https://www.baidu.com/s?wd=%E7%9F%A5%E4%B9%8E
    # 查看请求头
    print(response.headers)
    # {
    #     'Content-Encoding': 'gzip',
    #     'P3p': 'CP=" OTI DSP COR IVA OUR IND COM "',
    #     'Strict-Transport-Security': 'max-age=172800',
    #     'Vary': 'Accept-Encoding',
    #     'Date': 'Tue, 13 Feb 2018 07:09:27 GMT',
    #     'Transfer-Encoding': 'chunked',
    #     'Bdpagetype': '3',
    #     'Set-Cookie': 'BAIDUID=A28C54A277223DDEC1DA99FD5B499BA1:FG=1; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com, BIDUPSID=A28C54A277223DDEC1DA99FD5B499BA1; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com, PSTM=1518505767; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com, BD_CK_SAM=1;path=/, PSINO=5; domain=.baidu.com; path=/, BDSVRTM=8; path=/, H_PS_PSSID=1433_21079_22159; path=/; domain=.baidu.com',
    #     'Ckpacknum': '2',
    #     'X-Ua-Compatible': 'IE=Edge,chrome=1',
    #     'Cache-Control': 'private',
    #     'Content-Type': 'text/html;charset=utf-8',
    #     'Connection': 'Keep-Alive',
    #     'Bdqid': '0xa955f4d40003d70a',
    #     'Ckrndstr': '40003d70a',
    #     'Server': 'BWS/1.1',
    #     'Bduserid': '0',
    #     'X-Powered-By': 'HPHP'
    # }
    # 查看响应头部字符编码
    print(response.status_code)  # utf-8
    # 查看响应吗
    print(response.status_code)  # 200
    # 使用response.text时,Requests会基于HTTP响应的文本编码自动解码响应内容,大多数Unicode字符集都能被无缝解码
    print(type(response.text))  # <class 'str'>
    # 使用response.content时,返回的是服务器响应数据的原始二进制字节流,可以用来保存图片等二进制文件
    print(type(response.content))  # <class 'bytes'>

"""
post请求
"""
def post():
    # 请求地址
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    # 请求头
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1"}
    # 请求数据
    kw = input("输入翻译内容: ")
    formdata = {
    "i": kw,
    "doctype": "json"
    }
    # 发送post请求(data是请求数据)
    response = requests.post(url, data=formdata, headers=headers)
    # 查看响应数据
    print(response.text)
    # {
    #     "type": "EN2ZH_CN",
    #     "errorCode": 0,
    #     "elapsedTime": 1,
    #     "translateResult": [[{"src":"beautiful","tgt":"美丽的"}]]
    # }
    # 如果是json文件可以直接显示
    print(response.json())
    # {
    #     'errorCode': 0,
    #     'translateResult': [[{'tgt': '美丽的', 'src': 'beautiful'}]],
    #     'type': 'EN2ZH_CN',
    #     'elapsedTime': 1
    # }

"""
代理(proxies参数): urllib2处理代理太复杂,Requests相对简单
"""
# 免费代理
def proxy01():
    # 请求地址
    url = "https://nba.hupu.com/"
    # 代理IP列表
    proxies_list = [
        {"http": "113.89.54.209:9999"},
        {"http": "58.220.95.107:8080"},
        {"http": "163.125.17.110:8888"}
    ]
    # 随机选一个
    proxies = random.choice(proxies_list)
    # 发送请求(代理要加上proxies参数)
    response = requests.get(url, proxies=proxies)
    # 查看响应数据
    print(response.text)

# 私密代理
def proxy02():
    # 请求地址
    url = "https://nba.hupu.com/"
    # 私密代理IP
    proxy = {"http": "user:password@ip:port"}
    # 发送请求(代理要加上proxies参数)
    response = requests.get(url, proxies=proxy)
    # 查看响应数据
    print(response.text)

"""
web客户端验证(auth参数)
"""
def web():
    # 请求地址
    url = "http://192.168.199.107"
    # auth = (账户名, 密码)
    auth = ("user", "password")
    # 发送请求
    response = requests.get(url, auth=auth)
    # 查看响应数据
    print(response.text)

"""
Cookie和Session
"""
def cookie():
    # 请求地址
    url = "https://www.zhihu.com/"
    # 发送请求
    response = requests.get(url)
    # 返回CookieJar对象(如果一个响应中包含了cookie,可以利用cookies参数拿到)
    cookiejar = response.cookies
    print(type(cookiejar))  # <class 'requests.cookies.RequestsCookieJar'>
    print(cookiejar)  # <RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>
    # 将cookiejar转为字典类型
    cookiedict = requests.utils.dict_from_cookiejar(cookiejar)
    print(type(cookiedict))  # <class 'dict'>
    print(cookiedict)  # {'BDORZ': '27315'}

def session():
    pass

if __name__ == "__main__":
    # get()
    # post()
    # proxy01()
    # proxy02()
    # web()
    cookie()