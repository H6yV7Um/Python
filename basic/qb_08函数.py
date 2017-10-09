"""
函数: 实现特定功能的代码
"""


def sum_num(num1, num2):
    """
    求和功能
    :param num1: 数字1
    :param num2: 数字2
    :return: 返回结果
    """
    result = num1 + num2
    # print("%d + %d = %d" % (num1, num2, result))
    return result


sum_result = sum_num(10, 20)
print("计算结果是: %d" % sum_result)

"""
eval()函数: 可以将字符串当成有效表达式(取字符串里的内容)并返回计算结果
"""
result = input("输入算术题:")
print(eval(result))
