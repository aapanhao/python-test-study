import unittest

import unittest


# 继承unittest.TestCase
class TestStringMethods(unittest.TestCase):

    # test开头
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # 验证抛出的异常
        with self.assertRaises(TypeError):
            s.split(2)

    def setUp(self) -> None:
        print()
        print("测试函数开始前")

    def tearDown(self) -> None:
        print("测试函数开始后")


# if __name__ == '__main__':
#     unittest.main()

# 运行：python -m unittest -v 1_simple_test.py
