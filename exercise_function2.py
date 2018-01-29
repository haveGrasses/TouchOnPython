# coding=utf-8
"""练习函数参数的定义方法"""
import string
# 用lambda和filter完成功能：输出一个列表，列表里面包括：1-100内的所有偶数。（提示：可以用filter,lambda）
even_num = filter(lambda x: x if x % 2 == 0 else None, [x for x in range(1, 101)])
# even_num = filter(lambda x: x, [x for x in range(1, 101) if x % 2 == 0])
print even_num
# 用位置匹配，关键字匹配，收集匹配(元组收集,字典收集)分别写4个函数，完成功能；
# 传递3个列表参数：
# [1,2,3],[1,5,65],[33,445,22]
# 返回这3个列表中元素最大的那个，结果是：445


def get_max(list1, list2, list3):  # 位置匹配
    list_all = list1 + list2 + list3
    list_all.sort(reverse=True)
    return list_all[0]


print get_max([1, 2, 3], [1, 5, 66], [33, 445, 22])


def get_max2(list1=[], list2=[], list3=[]):   # 关键字参数
    list_all = list1 + list2 + list3
    list_all.sort(reverse=True)
    return list_all[0]


assert get_max2([1, 2, 3], [1, 5, 66], [33, 445, 22]) == 445


def get_max3(*kargs):  # 列表收集匹配
    list_all = []
    for list_arg in kargs:
        for i in list_arg:
            list_all.append(i)
    list_all.sort(reverse=True)
    return list_all[0]


assert get_max3([1, 2, 3], [1, 5, 66], [33, 445, 22]) == 445
'''
定义一个func(name)，该函数效果如下。
assert func("lili") = "Lili"
assert func("hanmei") = "Hanmei"
assert func("Hanmei") = "Hanmei"
'''


def capitalize_str(str):
    return str.capitalize()


assert capitalize_str("lili") == "Lili"
assert capitalize_str("hanmei") == "Hanmei"
assert capitalize_str("Hanmei") == "Hanmei"


"""
定义一个func(name,callback=None),效果如下。
assert func("lilei") == "Lilei"
assert func("LILEI",callback=string.lower) == "lilei"
assert func("lilei",callback=string.upper) == "LILEI"

"""
# import string


def change_str(name, callback=None):
    if isinstance(name, str):
        if callback is not None:
            return callback(name)
        else:
            return name.capitalize()
    else:
        return 'Eroor: name is not a str'


assert change_str("lilei") == "Lilei"
assert change_str("LILEI", callback=string.lower) == "lilei"
assert change_str("lilei", callback=string.upper) == "LILEI"
'''
定义一个func(*kargs)，该函数效果如下。
assert func(222,1111,'xixi','hahahah') == "xixi"
assert func(7,'name','dasere') == 'name'
assert func(1,2,3,4) == None
'''

'''
不建议的做法
def get_short_str(*kargs):
    str_in_kargs = {}
    for item in kargs:
        if type(item) is str:
            str_in_kargs[item] = len(item)
    if str_in_kargs == {}:
        return None
    else:
        # 对字典按值排序，排序结果为一个列表，元素是键，值组成的元组
        str_in_kargs = sorted(str_in_kargs.iteritems(), key=lambda x: x[1])
        return str_in_kargs[0][0]
'''


# 比较简单的实现方法


def get_short_str(*kargs):
    lis = filter(lambda x: isinstance(x, str), kargs)  # 利用filter和lambda过滤出字符串
    lis_len = [len(x) for x in lis]
    if lis_len:  # lis_len != []的简单写法
        min_index = min(lis_len)
        return lis[lis_len.index(min_index)]  # 元素在lis和len_lis中的索引是一样的
    return None


assert get_short_str(222, 1111, 'xixi', 'hahahah') == 'xixi'
assert get_short_str(7, 'name', 'dasere') == 'name'
assert get_short_str(1, 2, 3, 4) is None
"""
定义一个func(name=None,**kargs),该函数效果如下。

assert func(“lilei”) == "lilei"
assert func("lilei",years=4) == "lilei,years:4"
assert func("lilei",years=10,body_weight=20) == "lilei,years:10,body_weight:20"

"""
"""
不建议的做法
def info_str(name=None, **kwargs):
    if kwargs is None:
        return name
    else:
        info = name  # info为初始字符串
        # 对kwargs字典中的对象进行迭代，kwargs.items()是一个字典，元素是键，值元组
        for i in kwargs.items():
            # 在初始字符串的基础上加上每次迭代的元组的键和值，中间用相应的标点连接
            info = info + ',' + str(i[0]) + ':' + str(i[1])
        return info
"""


# 简单的实现方式


def info_str(name=None, **kwargs):
    info = ['%s:%s'% (key, value) for key, value in kwargs.items()]
    info.insert(0, name)
    return ','.join(info)


print info_str("lilei",years=4)
print info_str("lilei")
print info_str("lilei",years=4)
print info_str("lilei",years=10,body_weight=20)
