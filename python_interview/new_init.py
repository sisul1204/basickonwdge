#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author:sisul
# @time:2020/3/24:9:05

# class magic:
#     def __init__(self, nums):
#         self.nums = nums
#         print('666')
#         print('init: '+self.nums)
#
#     def __new__(cls, nums):
#         cls.nums = nums
#         print('new: '+cls.nums)
#         return super().__new__(cls)
#
# a = magic('A')

class magic:
    def __init__(self, nums):
        self.nums = self.nums
        self.langzi = 'langzi'
        print('666')
        print('init:'+self.nums)

    def __new__(cls, nums):
        print(nums)
        cls.nums = nums + 'BCDEFG'
        cls.langzi = '浪子'
        print('new:'+cls.nums)
        return super().__new__(cls)

a = magic('A')
print ('-'*10)
print (a.langzi)
print (a.nums)