"""
1、web测试框架，提供测试服务器，请求服务器客户端
2、aiohttp_client loop 固件
"""

import pytest_aiohttp
from aiohttp import pytest_plugin
from aiohttp.test_utils import *
from aiohttp import web
import pytest


async def hello(request):
    return web.Response(text='Hello, world')


# aiohttp_client/loop 就是固件
async def test_hello(aiohttp_client, loop):
    app = web.Application()
    app.router.add_get('/', hello)
    client = await aiohttp_client(app)

    resp = await client.get('/')
    assert resp.status == 200
    text = await resp.text()
    assert 'Hello, world' in text


# 自定义fixture固件，封装客户端对象
@pytest.fixture
def cli(aiohttp_client, loop):
    app = web.Application()
    app.router.add_get('/', hello)
    client = aiohttp_client(app)
    return loop.run_until_complete(client)


async def test_02(cli):
    resp = await cli.get('/')
    assert resp.status == 200

    text = await resp.text()
    assert text == "Hello, world"
