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

