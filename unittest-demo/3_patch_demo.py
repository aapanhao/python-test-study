# 1、mock中patch的使用


import unittest
from unittest.mock import Mock, patch


class Request:

    def __init__(self, name):
        self.name = name

    def request_url(self, url):
        pass


class TestStringMethods(unittest.TestCase):

    @patch.object(Request, 'request_url', return_value=200)
    def test_func(self, mock_request):
        request = Request("spec-name")
        result = request.request_url("www.baidu.com")
        assert result == 200
        mock_request.assert_called_once()

    def test_func_2(self):
        with patch.object(Request, 'request_url', side_effect=Mock(return_value=200)) as mock_request:
            request = Request("spec-name")
            result = request.request_url("www.baidu.com")
            assert result == 200
            mock_request.assert_called_once()
            print()
            print(mock_request)
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
            print(mock_request.call_args_list[0].args[0], type(mock_request.call_args_list[0].args[0]))
            assert mock_request.call_args_list[0].args[0].name == "spec-name"