"""
双链表: 每个节点有两个链接,一个指向前一个节点,若是头节点就指向空值;另一个指向下一个节点,若是尾节点就指向空值
       元素域elem存放具体数据
       链接域pre存放上一个节点位置
       链接域next存放下一个节点位置
常用操作:
is_empty() 链表是否为空
length() 链表长度
travel() 遍历链表
add(item) 链表头部添加
append(item) 链表尾部添加
insert(pos, item) 指定位置添加
remove(item) 删除节点
search(item) 查找节点是否存在
"""

# 节点实现
class Node(object):
    """双链表的节点"""

    def __init__(self, item):
        self.item = item
        self.pre = None
        self.next = None

# 双链表实现
class DoubleLinkedList(object):
    """双链表"""

    def __init__(self, node=None):
        # 链表头
        self.head = None

    # 判断链表是否为空
    def is_empty(self):
        return self.head is None

    # 求链表长度
    def length(self):
        pass

    # 遍历链表
    def travel(self):
        pass

    # 头部添加元素
    def add(self, item):
        pass

    # 尾部添加元素
    def append(self, item):
        pass

    # 指定位置添加元素
    def insert(self, pos, item):
        pass

    # 删除节点
    def remove(self, item):
        pass

    # 查找节点是否存在
    def search(self, item):
        pass

# 测试代码
if __name__ == "__main__":
    pass