"""
线性表: 某类元素的一个集合,记录着元素之间的顺序关系;线性表是最基本的数据结构之一
线性表根据存储方式不同分为两种:
顺序表: 将元素顺序的存放在一块连续的存储区里
链表: 将元素存放在通过链接构造起来的一系列存储块中
"""

"""
顺序表两种基本实现方式: 
一体式结构: 表信息(容量+元素个数)和元素存放在同一个存储区
分离式结构(常用): 表信息(容量+元素个数)和元素存放在不同的存储区
Python中list就是采用分离式技术实现的动态顺序表
顺序表操作:
增加元素: 1、尾部追加,时间复杂度O(1)
         2、非保序的加入元素(不常用),时间复杂度O(1)
         3、保序的加入元素,时间复杂度O(n)
删除元素: 1、删除尾部元素,时间复杂度O(1)
         2、非保序的元素删除(不常用),时间复杂度O(1)
         3、保序的元素删除,时间复杂度O(n)
"""

"""
顺序表的构建需要预先知道数据大小来申请连续的存储空间,而且在扩充时又需要进行数据的搬迁,很不灵活;
链表结构可以充分利用计算机内存空间,实现灵活的内存动态管理
链表: 属于线性表的一种,是一种常见的数据结构,但是不像顺序表一样连续存储数据,而是在每一个节点(数据存储单元)
     存放下一个节点的位置信息(地址)
"""