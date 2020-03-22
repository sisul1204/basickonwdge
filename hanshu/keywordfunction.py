# * coding:utf-8 *
# Author:sisul
#创建时间：2020/3/20 21:10

def data(**kwargs):
    return dict(sorted(kwargs.items(), key=lambda x:x[0], reverse=True))

dict1 = {'name':'wuya', 'age':18, 'address':'xian', 'work':'tester'}
print(data(**dict1))


#匿名函数
data = lambda **kwargs: dict(sorted(kwargs.items(), key=lambda x:x[1]))
print(data(name='sisul', age='aa'))


def logging(func):
    def warrper(*args, **kwargs):
        print('logging')
        func(*args, **kwargs)
    return warrper

@logging
def aa():
    print('after')

aa()


a = [1,2,3,4]
b = [1,2,3,4]

print(id(a))
print(id(b))
print(a is b)
print(a == b)