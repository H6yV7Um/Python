"""
列表: 用[]表示,通常存放同一种类型数据,可以做增删改查操作,是对象的有序集合
"""

name_list = ["grubby", "sky", "moon"]
# 1、获取数据
print(name_list[1])
print(name_list.index("sky"))  # index(): 元素索引
print(len(name_list))  # len(): 计算列表长度
print(name_list.count("grubby"))  # count(): 统计列表中某个元素出现的次数

# 2、添加数据
name_list.append("fly")  # append(): 追加数据
name_list.insert(1, "ted")  # insert(): 指定索引插入
temp_list = ["faker", "pawn", "fov"]
name_list.extend(temp_list)  # extend(): 可以追加其他完整列表(扩展)

# 3、修改数据
# name_list[1] = "grubby"  # 指定索引修改元素

# 4、删除数据
name_list.remove("fov")  # remove(): 删除列表中第一次出现的数据
name_list.pop()
name_list.pop(1)  # pop(): 默认删除列表最后一个元素,也可以指定索引删除
# name_list.clear()  # clear(): 清空所有数据
del name_list[1]  # del本质上是将变量从内存中删除(不建议使用,一般都用列表本身删除方法)

# 5、排序
name_list.sort()
name_list.sort(reverse=True)  # sort(): 默认升序,可设置reverse参数为降序
name_list.reverse()  # reverse(): 逆序(翻转)

# 6、遍历
for name in name_list:
    print("我的名字叫 %s" % name)

print(name_list)
