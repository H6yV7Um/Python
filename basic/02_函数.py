"""
函数: 封装具有独立功能的代码块
     func表示这是一个函数
     func()表示调用这个函数
区别: 方法在类里面,第一个参数默认self;函数在类外面,没有默认参数
"""


def function():
    pass


"""
缺省参数: 当某个参数多数情况下都是固定值时就可以设置成缺省参数,比如列表的sort方法(默认升序,指定reverse=Ture才是降序 )
注意事项: 缺省参数要放在参数列表的末尾
"""


def test01(name, gender=True):  # gender默认值True,调用函数时可以不写;

    gender_value = "男生"

    if not gender:
        gender_value = "女生"

    print("%s 是 %s" % (name, gender_value))


test01("grubby")
test01("moon", gender=False)

"""
多值参数: 函数要接受的参数个数或类型不确定时使用
         *args表示接受元组
         **kwargs表示接受字典
"""


def test02(num, *args, **kwargs):
    print(num)
    print(args)
    print(kwargs)


test02(1, 2, 3, 4, name="grubby", age=18)


# 累加案例
def test03(*args):
    res = 0
    for n in args:
        res += n
    print(res)


test03(1, 2, 3)

# 元组和字典的拆包(简化变量传递)
gl_tuple = (1, 2, 3)
gl_dict = {"name": "grubby", "age": 19}


def test04(*args, **kwargs):
    print(args)
    print(kwargs)


test04(*gl_tuple, **gl_dict)  # 要在元组和字典前面加上*/**标识,不然都会当成第一个参数传入(注意看参数高亮提示)

"""
递归: 函数调用函数本身
"""


# 累加案例
def sum_num(n):
    if n == 1:
        return 1
    else:
        return sum_num(n - 1) + n


result = sum_num(100)
print(result)  # 5050


# 菲波那切数列
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


result = fibonacci(10)
print(result)  # 55

"""
匿名函数: 默认返回冒号后面的表达式运算结果,只能完成简单功能,复杂功能还是得def
                    参数: 表达式
格式: func = lambda x, y: x + y
      func(x,y)
"""


def test(a, b):
    a + b


func = lambda a, b: a + b

result1 = test(11, 22)  # test函数并没有返回值
print(result1)  # None
result2 = func(11, 22)
print(result2)  # 33

# 案例一: 列表中的字典排序
stu_list = [{"name": "grubby", "age": 18},
            {"name": "moon", "age": 19},
            {"name": "fly", "age": 20}]
print(stu_list)
# stu_list.sort()  # TypeError: unorderable types: dict() < dict()因为列表里存的是字典数据,无法直接排序,可以指定key排序
stu_list.sort(key=lambda x: x["name"])
print(stu_list)  # [{'name': 'fly', 'age': 20}, {'name': 'grubby', 'age': 18}, {'name': 'moon', 'age': 19}]
stu_list.sort(key=lambda x: x["age"])
print(stu_list)  # [{'name': 'grubby', 'age': 18}, {'name': 'moon', 'age': 19}, {'name': 'fly', 'age': 20}]


# 案例二: 将匿名函数作为函数的参数传入
def compute(a, b, func):
    return func(a, b)


result = compute(11, 22, lambda x, y: x + y)
print(result)
result = compute(11, 22, lambda x, y: x - y)
print(result)
result = compute(11, 22, lambda x, y: x * y)
print(result)
result = compute(11, 22, lambda x, y: x / y)
print(result)

#  改进版(上述代码中lambda表达式仍然是写死的,python是动态语言,可以直到运行时才确定要干啥)
func_new = eval(input("请输入匿名函数:"))
result = compute(11, 22, func_new)
print(result)
