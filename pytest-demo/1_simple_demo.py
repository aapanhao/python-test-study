"""
1、pytest fixture 固件的使用
2、可以类似unittest写类测试，也可写函数测试
3、兼容unittest"""

import pytest


def test_01():
    a = 1
    assert a == 1


@pytest.fixture
def pre_define():
    return "Hello"


def test_02(pre_define):
    h = pre_define
    print(h)
    assert h == "Hello"


class TestCase:
    def test_03(self):
        print("hello")
        assert 2 == 2
