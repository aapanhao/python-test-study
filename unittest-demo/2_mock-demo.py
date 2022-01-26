# 1、Mock的使用
# 2、spec参数（True，没有的参数将不在mock，而是报错）
# 3、MagicMock与Mock的区别
# 4、side_effect 与 return_value 一起使用
# 了解用法，场景可能不一定合适
# mock为了模拟外部服务，未实现的功能

import unittest
from unittest.mock import Mock, MagicMock


class Request:
    def request_url(self, url):
        pass

    # 开发好的request_url
    def request_url_new(self, url):
        return 400, url


class TestStringMethods(unittest.TestCase):

    # 1、Mock 使用
    def test_func(self):
        request = Request()
        request.request_url = Mock(return_value=(200, ""))
        result = request.request_url("www.baidu.com")
        assert result[0] == 200

    # 2、spec 参数
    def test_func_1(self):
        request = Request()
        request.request_url = Mock(return_value=(200, ""))
        result = request.request_url("www.baidu.com")
        assert result[0] == 200
        result = request.request_url.Name
        print()
        print(request.request_url)
        print(result)

    def test_func_1_spec(self):
        request = Request()
        request.request_url = Mock(return_value=(200, ""), spec=True)
        result = request.request_url("www.baidu.com")
        assert result[0] == 200
        print()
        print(request.request_url)
        result = request.request_url.Name
        print(result)

    # 3、MagicMock 与 Mock 区别
    def test_func_2(self):
        mock1 = MagicMock()
        print(mock1.__str__())
        mock1.__str__.return_value = "111"
        print(mock1)

    def test_func_3(self):
        mock2 = Mock()
        print(mock2.__str__())
        mock2.__str__ = Mock(return_value="222")
        print(mock2)

    # 4、return_value 和 side_effect 一起使用的情况
    def test_func_4(self):
        request = Request()
        request.request_url = Mock(return_value=(200, ""),
                                   side_effect=request.request_url_new)
        result = request.request_url("www.baidu.com")
        assert result[0] == 400
        assert result[1] == "www.baidu.com"
