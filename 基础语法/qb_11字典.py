"""
字典: 用{}表示,存放键值对,key唯一,可以做增删改查操作,是对象的无序集合,用来存放同一种类型的数据
     [keys]、[values]、(key:value)
"""

dictionary = {"name": "grubby",
              "age": 18,
              "gender": True,
              "height": 1.75,
              "weight": 65.0}  # 一个键值对占有一行代码

# 1、取值
print(dictionary["name"])

# 2、添加/修改
dictionary["age"] = 19  # key存在就修改对应value,不存在就添加键值对

# 3、删除
dictionary.pop("weight")  # pop(): 删除指定key

# 4、统计键值对数量
print(len(dictionary))  # len(): 统计kv对

# 5、合并字典
temp = {"score": 90,
        "age": 20}
dictionary.update(temp)  # 键相同值覆盖

# 6、清空字典
# dictionary.clear()  # clear(): 清空字典中所有键值对

# 7、遍历循环字典
for key in dictionary:
    print("%s : %s" % (key, dictionary[key]))

print(dictionary)

# 8、常见应用: 将多个字典放在一个列表中
card_list = [
    {"name": "grubby",
     "age": 18,
     "phone": 110},
    {"name": "moon",
     "age": 19,
     "phone": 119}
]

for card in card_list:
    print(card)  # 结果也验证了list有序dictionary无序

# 9、完整for循环
name_list = [
    {"name": "grubby"},
    {"name": "moon"},
    {"name": "sky"}
]
find_name = "moon"
for dictionary in name_list:
    print(dictionary)
    if dictionary["name"] == find_name:
        print("找到 %s 同学了" % find_name)
        break
else:
    print("很抱歉呢没有找到 %s 同学" % find_name)  # 如果for循环过程中没有执行到break语句,循环结束后会执行else语句

