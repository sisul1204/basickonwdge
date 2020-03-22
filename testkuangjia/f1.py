# * coding:utf-8 *
# Author:sisul
#创建时间：2020/3/21 21:42

import pytest

def test_001():
    assert 1 == 1

def test_002():
    assert 1 == 2


class Test1:
    def test_001(self):
        pass


if __name__ == '__main__':
    pytest.main(['-v', 'f1.py'])
