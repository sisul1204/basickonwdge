#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author:sisul
# @time:2020/3/20:16:40

# def extendList(val, list=[]):
#     list.append(val)
#     return list
#
# list1 = extendList(10)
# list2 = extendList(123, [])
# list3 = extendList('a')
#
# print('list1 = %s' %list1)
# print('list2 = %s' %list2)
# print('list3 = %s' %list3)

# def extendList(val, list=None):
#     if list is None:
#         list = []
#     list.append(val)
#     return list
#
# list1 = extendList(10)
# list2 = extendList(123, [])
# list3 = extendList('a')
#
# print('list1 = %s' %list1)
# print('list2 = %s' %list2)
# print('list3 = %s' %list3)

#闭包延迟
def multipliers():
    return [lambda x: i * x for i in range(4)]

print([m(2) for m in multipliers()])


class Parent:
    x = 1

class Child1(Parent):
    pass

class Child2(Parent):
    pass

print(Parent.x, Child1.x, Child2.x)
Child1.x = 2
print(Parent.x, Child1.x, Child2.x)
Parent.x = 3
print(Parent.x, Child1.x, Child2.x)


list = ['a', 'b', 'c', 'd', 'e']
print (list[10:])

print('-----------------------------------')
list = [[]] * 5
print(list)
list[0].append(10)
print(list)
list[1].append(20)
print(list)
list.append(30)
print(list)