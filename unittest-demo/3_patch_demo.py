"""
1、mock中patch的使用
2、使用装饰器方式
3、使用with方式
4、使用autospec的好处
"""

import unittest
from unittest.mock import Mock, patch


class Request:

    def __init__(self, name):
        self.name = name

    def request_url(self, url):
        pass

    def request_url_new(self, url):
        pass

class TestStringMethods(unittest.TestCase):

    @patch.object(Request, 'request_url', return_value=200)
    @patch.object(Request, 'request_url_new', return_value=200)
    def test_func(self, asd, dfg):
        request = Request("spec-name")
        result = request.request_url("www.baidu.com")
        assert result == 200
        print(asd)
        print(dfg)
        dfg.assert_called_once()

    def test_func_2(self):
        with patch.object(Request, 'request_url', side_effect=Mock(return_value=200)) as mock_request:
            request = Request("spec-name")
            result = request.request_url("www.baidu.com")
            assert result == 200
            mock_request.assert_called_once()
            print()
            print(mock_request)
            # 可以看到mock_request.call_args_list[0].args[0] 是字符串对象
            print(mock_request.call_args_list[0].args[0], type(mock_request.call_args_list[0].args[0]))

    # 使用autospec的好处
    def test_func_3(self):
        with patch.object(Request, 'request_url', side_effect=Mock(return_value=200), autospec=True) as mock_request:
            request = Request("spec-name")
            result = request.request_url("www.baidu.com")
            assert result == 200
            mock_request.assert_called_once()
            print()
            print(mock_request)
            # 可以看到mock_request.call_args_list[0].args[0] 是request对象，所以在assert可以判断使用参数
            print(mock_request.call_args_list[0].args[0], type(mock_request.call_args_list[0].args[0]))
            assert mock_request.call_args_list[0].args[0].name == "spec-name"
