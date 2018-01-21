# coding=utf-8
"""this is an exercise file consisting of some exercises about function"""

# 1.定义一个方法 func，该func可以引入任意多的整型参数，结果返回其中最大与最小的值。


def max_and_min(*num):
    # make sure that the list only has int type
    for i in num:
        if isinstance(i, int):
            pass
        else:
            return 'error: the type of parameters must be int'
    return max(num), min(num)


# 方法二：filter函数


def max_and_min2(*num):
    num_int = filter(lambda x: isinstance(x, int), num)
    num_int = sorted(num_int)
    return num_int[-1], num_int[0]


# 2.定义一个方法func，该func可以引入任意多的字符串参数，结果返回（长度）最长的字符串


def the_longest_string(*string):
    str_list = [(s, len(s)) for s in string if isinstance(s, str)]
    str_list.sort(reverse=True, key=lambda x: x[1])  # 按(s,len(s))的第二项排序，即len(s)
    return str_list[0][0]


# 方法二


def the_longest_string2(*string):
    for s in string:
        if isinstance(s, str):
            pass
        else:
            return 'error: input contain no str type'
    string_sort = sorted(string, reverse=True, key=lambda x: len(x))
    return string_sort[0]


# 3. 定义一个方法get_doc(module)，module参数为该脚本中导入或定义的模块对象，该函数返回module的帮助文档

import os
def get_doc(module):
    cmd_statement = 'pydoc % s' % module  # 在命令行中执行pydoc module返回该模块的帮助文档
    doc = os.popen('python -m %s' % cmd_statement).read()  # 将命令行后台执行的结果读取后返回给doc
    return doc


# 测试
assert max_and_min(1, 23, 4) == (23, 1)  # assert:断言，用于函数测试
print max_and_min(1, 23, 4)
print max_and_min2(1, 23, 4)
print the_longest_string('summer', 'i', 'the')
print the_longest_string2('summer', 'i', 'the')
print get_doc('string')