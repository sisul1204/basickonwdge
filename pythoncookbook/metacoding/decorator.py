#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author:sisul
# @time:2020/3/24:11:41

# class dedcorator:
#
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args):
#         print('__call__')
#         self.func(*args)
#
#
# class C:
#     @dedcorator
#     def method(self,a,b):
#         print(a, b)
#
# c = C()
# c.method(5, 6)


# def decorator(cls):
#     class Wrapper:
#         def __init__(self, *args):
#             self.wrapped = cls(*args)
#         def __getattr__(self, item):
#             return getattr(self.wrapped, item)
#     return Wrapper
#
# @decorator
# class C:
#     def __init__(self, x, y):
#         self.attr = 'spam'
#
# x = C(6,7)
# print(x.attr)

# class tracer:
#     def __init__(self, func):
#         self.calls = 0
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         self.calls += 1
#         print('call %s to %s' %(self.calls, self.func.__name__))
#         self.func(*args, **kwargs)
#
# @tracer
# def spam(a, b,c):
#     print(a+b+c)
#
# spam(1,2,3)
# spam('a','b','c')
# print(type(spam))


# class tracer:
#     def __init__(self, func):
#         self.calls = 0
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         self.calls += 1
#         print('call %s to %s' %(self.calls, self.func.__name__))
#         return self.func(*args, **kwargs)
#
#
# @tracer
# def spam(a, b, c):
#     print(a+b+c)
#
# @tracer
# def egg(x, y):
#     print(x ** y)
#
#
# spam(1,2,3)
# spam(a=4, b=5, c=6)
#
# egg(2, 16)
# egg(4, y=4)


# calls = 0
# def tracer(func):
#     def wrapper(*args, **kwargs):
#         global calls
#         calls += 1
#         print('call %s to %s' %(calls, func.__name__))
#         return func(*args, **kwargs)
#     return wrapper
#
# @tracer
# def spam(a, b, c):
#     print(a+b+c)
#
# @tracer
# def egg(x, y):
#     print(x ** y)
#
#
# spam(1,2,3)
# spam(a=4, b=5, c=6)
#
# egg(2, 16)
# egg(4, y=4)


# class tracer:
#     def __init__(self, func):
#         self.calls = 0
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         self.calls += 1
#         print(self, args, kwargs)
#         print('call %s to %s' %(self.calls, self.func.__name__))
#         return self.func(*args, **kwargs)
#
#
# class Person:
#     def __init__(self, name, pay):
#         self.name = name
#         self.pay = pay
#
#     @tracer
#     def giveRaise(self, percent):
#         self.pay *= (1.0 + percent)
#
#     @tracer
#     def lastName(self):
#         return self.name.split()[-1]
#
# bob = Person('Bob Simth', 50000)
# bob.giveRaise(.25)
# print(bob.lastName())

# def tracer(func):
#     calls = 0
#     def onCall(*args, **kwargs):
#         nonlocal calls
#         calls += 1
#         print('call %s to %s' %(calls, func.__name__))
#         return func(*args, **kwargs)
#     return onCall
#
#
# @tracer
# def spam(a,b,c):
#     print(a+b+c)
#
# spam(1,2,3)
# spam(a=4, b=5, c=6)
#
# class Person:
#     def __init__(self, name, pay):
#         self.name = name
#         self.pay = pay
#
#     @tracer
#     def giveRaise(self, percent):
#         self.pay *= (1.0 + percent)
#
#     @tracer
#     def lastName(self):
#         return self.name.split()[-1]
#
# print('method...')
# bob = Person('Bob Simth', 50000)
# sue = Person('Sue Jones', 1000000)
# print(bob.name, sue.name)
# sue.giveRaise(.10)
# print(sue.pay)
# print(bob.lastName(), sue.lastName())


class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)

    def __get__(self, instance, owner):
        print('先调用我')
        return wrapper(self, instance)

class wrapper:
    def __init__(self, desc, subj):
        self.desc = desc
        self.subj = subj

    def __call__(self, *args, **kwargs):
        print('再调用我')
        return self.desc(self.subj, *args, **kwargs)


class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    @tracer
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    @tracer
    def lastName(self):
        return self.name.split()[-1]

print('method...')
bob = Person('Bob Simth', 50000)
sue = Person('Sue Jones', 1000000)
print(bob.name, sue.name)
sue.giveRaise(.10)
print(sue.pay)
print(bob.lastName(), sue.lastName())








