# * coding:utf-8 *
# Author:sisul
#创建时间：2020/3/21 14:42

def create_class(name):
    if name == 'user':
        class User:
            def __str__(self):
                return 'user'
        return User
    elif name == 'company':
        class Company:
            def __str__(self):
                return 'company'
        return Company

#type动态创建类
# User = type('User', (), {})

def say(self):
    return 'i am sisul'

class BaseClass:
    def answer(self):
        return 'i am baseclass'

class MetaClass(type):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)
#什么是元类，元类是创建类的类

class User(metaclass=MetaClass):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'user'

#python中类的实例化过程，会首先寻找metaclass，通过metaclass去创建User类

if __name__ == '__main__':
    # user = create_class('user')
    # print(user())

    # User = type('User', (BaseClass, ), {'name':'sisul', 'say':say})
    my_obj = User('sisul')
    print(my_obj)

