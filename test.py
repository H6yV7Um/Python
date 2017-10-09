# 函数内部赋值操作
gl_num = 55


def test03(num):
    print("函数内部代码:")
    num = 99  # 函数内部的赋值操作不会改变全局变量的值(画内存图)
    print(num)


test03(gl_num)
print(gl_num)

# 函数内部方法操作
gl_list = [1, 2, 3]


def test04(num_list):
    print("函数内部代码:")
    num_list.append(5)  # 函数内部的方法操作会改变全局变量的值(画内存图)
    print(num_list)


test04(gl_list)
print(gl_list)

# 列表的 += 相当于调用extend()方法
gl_num = 10
gl_list = [11, 22, 33]


def test05(num, num_list):
    print("函数内部代码:")
    num += num  # 等同于 num = num + num

    # num_list = num_list + num_list
    num_list += num_list  # 等同于num_list.extend(num_list)

    print(num, num_list)


test05(gl_num, gl_list)
print(gl_num, gl_list)

def test(n):
    if n == 1 or n == 2:
        return 1
    return test(n-1) + test(n-2)


result = test(9)
print(result)
