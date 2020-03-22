# * coding:utf-8 *
# Author:sisul
#创建时间：2020/3/21 16:35

#什么是迭代协议
#迭代器是什么？迭代器是访问集合内元素的一种方式，一般用来遍历数据
#迭代器和以下标的访问方式不一样，迭代器是不能返回的，迭代器提供了一种惰性方式数据的方式

#Iterable 实现__iter__
#Iterator 实现__next__

from collections.abc import Iterable, Iterator
a = [1,2]
print(isinstance(a, Iterable))
print(isinstance(a, Iterator))
