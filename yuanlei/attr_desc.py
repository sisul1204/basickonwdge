# * coding:utf-8 *
# Author:sisul
#创建时间：2020/3/21 11:12

from datetime import date, datetime
import numbers

class IntField:
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError('int value need')
        if value < 0:
            raise ValueError('positive value needed')
        self.value = value

    def __delete__(self, instance):
        pass

class NonDataField:
    def __get__(self, instance, owner):
        return self.value

class User:
    # age = IntField()
    age = NonDataField()

if __name__ == '__main__':
    user = User()
    user.age = 30
    print(user.__dict__)
    print(getattr(user, 'age'))


