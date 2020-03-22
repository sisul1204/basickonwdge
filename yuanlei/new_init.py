# * coding:utf-8 *
# Author:sisul
#创建时间：2020/3/21 14:28

class User:
    def __new__(cls, *args, **kwargs):
        print('in new')
        return super().__new__(cls)

    def __init__(self, name):
        print('in init')
        self.name = name

u = User(name = 'bobby')
