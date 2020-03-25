#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author:sisul
# @time:2020/3/23:9:08

# #将"hello world"转换为首字母大写“Hello World”
# arr = 'hello world'
# Arr = arr.title()
# print(Arr)
#
# #如何检测字符串中只含有数字？ isdigit
# s1 = "12223".isdigit()
# print(s1)
# s2 = '123df'.isdigit()
# print(s2)
#
# #将字符串'ilovechina'进行反转
# s = 'ilovechina'
# s1 = s[::-1]
# print(s1)
#
# #有一个字符串开头和末尾都有空格，比如' adakd  '，要求写一个函数把这个字符串的前后空格都去掉
# def strip_func(str):
#     return str.strip()
# s = ' adakd  '
# s1 = strip_func(s)
# print(s1)
#
# #获取字符串"123456"最后的两个字符
# a = "123456"
# print(a[-2::])
# print(a[len(a)-2:len(a)])
# print(a[len(a)-2::])
#
# #一个编码为GBK的字符串S，要将其转成UTF-8编码的字符串，应如何操作？
# a = '中国'.encode('GBK').decode('GBK').encode('UTF-8').decode('UTF-8')
# print(a)
#
# #（1）s="info:xiaoZhang 33 shandong"，用正则切分字符串输出['info', 'xiaoZhang', '33', 'shandong']。
# #（2）a = "你好 中国 "，去除多余空格只留一个空格。
# import re
# s="info:xiaoZhang 33 shandong"
# s_split = re.split(':| ', s)
# print(s_split)
#
# a = "你好 中国 "
# print(' '.join(a.split()))
#
# #已知AList = [1,2,3,1,2],对AList列表元素驱虫，写出具体过程
# AList = [1,2,3,1,2]
# print(list(set(AList)))
#
# #如何实现"1,2,3"变成["1","2","3"]
# a = "1,2,3"
# a_list = a.split(',')
# print(a_list)
#
# #[[1,2],[3,4],[5,6]] 一行代码展开该列表，得出 [1,2,3,4,5,6]
# a = [[1,2],[3,4],[5,6]]
# b = [j for i in a for j in i]
# print(b)
#
# #合并列表[1,5,7,9]和[2,2,6,8]
# a = [1,5,7,9]
# b = [2,2,6,8]
# print(a + b)
# a.extend(b)
# print(a)
#
# #如何打乱一个列表的元素？
# import random
# a = [1,2,3,4,5]
# random.shuffle(a)
# print(a)
#
# '''
# 按照字典的内的年龄排序
# d1 = [
#     {'name':'alice', 'age'：38},
#     {'name':'bob', 'age'：18},
#     {'name':'Carl', 'age'：28},
# ]
# '''
# d1 = [
#     {'name':'alice', 'age':38},
#     {'name':'bob', 'age':18},
#     {'name':'Carl', 'age':28},
# ]
#
# d_sort = sorted(d1, key=lambda x:x['age'])
# print(d_sort)
#
# #请合并下面两个字典a = {"A":1,"B":2},b = {"C":3,"D":4}
# a = {"A":1,"B":2}
# b = {"C":3,"D":4}
# #第一种方法
# print({**a, **b})
# #第二种方法
# a.update(b)
# print(a)
#
# # 需求 3： 把字典的 key 和 value 值调换；
# d = {'a':'1', 'b':'2'}
# print({v: k for k, v in d.items()})
#
# #如何把元组 ("a","b") 和元组 (1,2)，变为字典 {"a":1,"b":2}
# a,b = ("a","b"),(1,2)
# print(dict(zip(a, b)))
#
# #如何交换字典 {"A":1,"B":2}的键和值
# d = {"A":1,"B":2}
# #方法一
# print({v: k for k, v in d.items()})
# #方法二
# print(dict(zip(d.values(), d.keys())))
#
# '''
# 我们知道对于列表可以使用切片操作进行部分元素的选择，那么如何对生成器类型的对象实现相同的功能呢？
# 这个题目考察了 Python 标准库的 itertools 模快的掌握情况，该模块提供了操作生成器的一些方法。
# 对于生成器类型我们使用 islice 方法来实现切片的功能。例子如下
# '''
# from itertools import islice
# gen = iter(range(10))               #iter()函数用来生成迭代器
# for i in islice(gen, 0, 4):         #第一个参数是迭代器，第二个参数起始索引，第三个参数结束索引，不支持负数索引
#     print(i)
#
# #a="hello" 和 b="你好" 编码成 bytes 类型
#
# '''
# json 序列化时，默认遇到中文会转换成 unicode，如果想要保留中文怎么办？
# 可以通过 json.dumps 的 ensure_ascii 参数解决
#
# '''
# import json
#
# a = json.dumps({'name':'张三', 'age':18}, ensure_ascii=False)
# print(a, type(a))
#
# '''
# 有两个磁盘文件 A 和 B，各存放一行字母，
# 要求把这两个文件中的信息合并(按字母顺序排列)，
# 输出到一个新文件 C 中。
# '''
# with open('A.txt', 'r') as f1:
#     f1_txt = f1.readline()
#     print(f1_txt, type(f1_txt))
#
# with open('B.txt', 'r') as f2:
#     f2_txt = f2.readline()
#
# f3_txt = f1_txt + f2_txt
# f3_sorted = sorted(f3_txt)          #返回类型是list
# print(f3_sorted, type(f3_sorted))
#
# with open('C.txt', 'a+') as f3:
#     f3.write(''.join(f3_sorted))
#
# '''
# 写一个函数，接收整数参数 n，返回一个函数，函数的功能是把函数的参数和 n 相乘并把结果返回。
# '''
# #闭包
# def mul_operator(num):
#     def g(val):
#         return val * num
#     return g
#
# m = mul_operator(5)
# print(m(6))
#
#
# #一行代码输出 1-100 之间的所有偶数。
# #第一种方法，列表生成式
# a = [i for i in range(1,101) if i % 2 == 0]
# print(a)
# #第二种方法
# print(list(range(2,101,2)))
#
#
# #Python 字典和 json 字符串相互转化方法
# '''
# 在 Python 中使用 dumps 方法 将 dict 对象转为 Json 对象，
# 使用 loads 方法可以将 Json 对象转为 dict 对象。
# '''
# dic = {'a': 123, 'b': "456", 'c': "中国"}
# dict_to_json = json.dumps(dic, ensure_ascii=False)
# print(dict_to_json, type(dict_to_json))
#
# json_to_dict = json.loads(dict_to_json)
# print(json_to_dict, type(json_to_dict))
#
# #请写一个Python逻辑，计算一个文件中的大写字母数量
# with open('C.txt', 'r') as f:
#     count = 0
#     for s in f.read():
#         if s.isupper():
#             count += 1
# print(count)
#
# #函数装饰器
# from functools import wraps
# def log(label):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             print('装饰器')
#             func(*args, **kwargs)
#         return wrapper
#     return decorator
#
# @log('info')
# def foo(a,b,c):
#      print(a+b+c)
#      print("in foo")
#
# foo(1,2,3)
#
# #hasattr(),getattr(),setattr()的用法
# class Person:
#     def __init__(self):
#         self.name = 'liming'
#         self.age = 12
#
#     def show(self):
#         print(self.name)
#         print(self.age)
#
#     def set_sex(self):
#         setattr(Person, 'sex', '男')
#
#     def get_info(self):
#         print(getattr(self, 'name'))
#         print(getattr(self, 'age'))
#         print(getattr(self, 'sex'))
#
# def run():
#     if hasattr(Person, 'show'):
#         print('Person类有show')
#
#     Person().set_sex()
#     Person().get_info()
#
# if __name__ == '__main__':
#     run()

#使用元类实现一个单例模式
class Singleton(type):
    def __init__(self, *args, **kwargs):
        print('in __init__')
        self.__instance = None
        super(Singleton, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        print('in __call__')
        if self.__instance is None:
            self.__instance = super(Singleton, self).__call__(*args, **kwargs)
        return self.__instance

class Foo(metaclass=Singleton):
    pass

foo1 = Foo()
foo2 = Foo()
print(foo1 is foo2)