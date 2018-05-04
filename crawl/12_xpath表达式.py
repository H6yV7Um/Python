# coding=utf-8
"""
xpath使用路径表达式获取xml文档中的元素和属性
元素: <class 'lxml.etree._Element'>,需要序列化成字符串才能输出
     当xpath表达式返回结果是元素时,可用text函数获取当前标签的文本内容,tag函数获取当前标签的名称
属性: <class 'lxml.etree._ElementUnicodeResult'>,可以直接输出(Python里的字符串是Unicode编码)
     当xpath表达式返回结果是属性时,结果就是当前属性的值
xpath函数: http://www.w3school.com.cn/xpath/xpath_functions.asp

节点:
/ 	从根节点选取
// 	从当前节点选择文档中的节点,而不考虑它们的位置
. 	选取当前节点
.. 	选取当前节点的父节点
@ 	选取属性
bookstore: 选取bookstore元素的所有子节点
/bookstore: 选取根元素bookstore
bookstore/book: 选取属于bookstore的子元素的所有book元素
//book: 选取所有book子元素,而不管它们在文档中的位置
bookstore//book: 选择属于bookstore元素的后代的所有book元素,而不管它们位于bookstore之下的什么位置
//@lang: 选取名为lang的所有属性

谓语: 查找指定条件的节点,嵌在[]中
/bookstore/book[1]: 选取属于bookstore子元素的第一个book元素
/bookstore/book[last()]: 选取属于bookstore子元素的最后一个book元素
/bookstore/book[last()-1]: 选取属于bookstore子元素的倒数第二个book元素
/bookstore/book[position()<3]: 选取最前面的两个属于bookstore元素的子元素的book元素
//title[@lang]: 选取所有具有lang属性的title元素
//title[@lang=’eng’]: 选取所有title元素,且lang属性值为eng
/bookstore/book[price>35.00]: 选取bookstore元素下的book元素,且其中的price元素>35.00
/bookstore/book[price>35.00]/title: 选取bookstore元素下的book元素下的title元素,且book元素的price元素>35.00

通配符: 用来选取未知的XML元素
*: 匹配任何元素节点
@*: 匹配任何属性节点
node(): 匹配任何类型的节点
/bookstore/*: 选取bookstore元素的所有子元素
//*: 选取文档中的所有元素
//title[@*]: 选取所有带有属性的title元素

多路径: 在路径表达式中使用"|"运算符可以选取多个路径
//book/title | //book/price: 选取book元素的所有title和price元素
//title | //price: 选取文档中的所有title和price元素
/bookstore/book/title | //price: 选取属于bookstore元素的book元素的所有title元素及文档中所有的price元素


lxml库的etree模块
etree.HTML(text): 从字符串常量解析HTML文档,返回节点树
                (Parses an HTML document from a string constant.Returns the root node)
etree.parse(source): 解析源文件返回一个节点树
                (Return an ElementTree object loaded with source elements)
etree.tostring(element_or_tree): 将元素序列化成其xml树编码的字符串
                (Serialize an element to an encoded string representation of its XML tree)
备注: python的3引号可用于表示多行字符串或者函数下方的注释
"""

from lxml import etree

"""
etree读取字符串
"""
def test():
    """
    xpath使用案例
    """

    text = """
    <div>
        <ul>
             <li class="item-0"><a href="link1.html">first item</a></li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-inactive"><a href="link3.html">third item</a></li>
             <li class="item-1"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a> # 注意，此处缺少一个 </li> 闭合标签
        </ul>
    </div>
     """

    # 将字符串解析为HTML文档
    data = etree.HTML(text)
    print(type(data))  # <class 'lxml.etree._ElementTree'>

    # 将HTML文档序列化成字符串(etree可以自动修正html代码)
    data_new = etree.tostring(data).decode("utf-8")
    print(type(data_new))  # <class 'str'>

    # xpath表达式解析
    res_list = data.xpath('//li')

    # 遍历列表
    for res in res_list:
        print(type(res))  # <class 'lxml.etree._Element'>
        # 将元素序列化成字符串
        res = etree.tostring(res).decode("utf-8")
        print(res)  # <li class="item-0"><a href="link1.html">first item</a></li>

"""
etree读取文件
"""
html = etree.parse("hello.html")
# print(type(html))  # <class 'lxml.etree._ElementTree'>
result = etree.tostring(html).decode("utf-8")
# print(type(result))  # <class 'str'>

def test01():
    """
    获取所有的<li>标签: 当xpath表达式返回结果是元素时,text获取当前标签的文本内容,tag获取当前标签的名称
    """
    res_list = html.xpath('//li')
    for res in res_list:
        print(type(res))  # <class 'lxml.etree._Element'>
        print(res)  # <Element li at 0x22772f98e08>
        print(res.text)
        print(res.tag)  # li
        # 将元素序列化成字符串
        res1 = etree.tostring(res).decode("utf-8")
        print(type(res1))  # <class 'str'>
        print(res1)  # <li class="item-0"><a href="link1.html">first item</a></li>

def test02():
    """
    获取<li>标签下href为link1.html的<a>标签
    """
    res_list = html.xpath('//li/a[@href="link1.html"]')
    for res in res_list:
        print(type(res))  # <class 'lxml.etree._Element'>
        # 将元素序列化成字符串
        res = etree.tostring(res).decode("utf-8")
        print(res)  # <a href="link1.html">first item</a>

def test03():
    """
    获取<li>标签下的所有<span>标签
    """
    res_list = html.xpath('//li//span')
    for res in res_list:
        print(type(res))  # <class 'lxml.etree._Element'>
        # 将元素序列化成字符串
        res = etree.tostring(res).decode("utf-8")
        print(res)  # <span class="bold">third item</span>

def test04():
    """
    获取倒数第二个元素的内容
    """
    res_list = html.xpath('//*[last()-1]')
    for res in res_list:
        print(type(res))  # <class 'lxml.etree._Element'>
        # 将元素序列化成字符串
        res = etree.tostring(res).decode("utf-8")
        print(res)  # <li class="item-1"><a href="link4.html">fourth item</a></li>

def test05():
    """
    获取class值为bold的标签名称
    """
    res_list = html.xpath('//*[@class="bold"]')
    for res in res_list:
        print(type(res))  # <class 'lxml.etree._Element'>
        print(res.text)  # third item
        print(res.tag)  # span
        # 将元素序列化成字符串
        res = etree.tostring(res).decode("utf-8")
        print(res)  # <span class="bold">third item</span>

def test06():
    """
    获取<li>标签的所有class属性
    """
    res_list = html.xpath('//li/@class')
    print(res_list)  # ['item-0', 'item-1', 'item-inactive', 'bold', 'item-1', 'item-0']
    for res in res_list:
        print(type(res))  # <class 'lxml.etree._ElementUnicodeResult'>
        # res = etree.tostring(res).decode("utf-8")
        # TypeError: Type 'lxml.etree._ElementUnicodeResult' cannot be serialized
        print(res)  # item-0

def test07():
    """
    获取<li>标签下的<a>标签里的所有class属性
    """
    res_list = html.xpath('//li/a//@class')
    for res in res_list:
        print(type(res))  # <class 'lxml.etree._ElementUnicodeResult'>
        print(res)  # bold

def test08():
    """
    获取最后一个<li>的<a>的href属性
    """
    res_list = html.xpath('//li[last()]/a/@href')
    for res in res_list:
        print(type(res))  # <class 'lxml.etree._ElementUnicodeResult'>
        print(res)  # link5.html

if __name__ == "__main__":
    test()
    # test01()
    # test02()
    # test03()
    # test04()
    # test05()
    # test06()
    # test07()
    # test08()
