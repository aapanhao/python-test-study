"""
1、继承AioHTTPTestCase类，重写get_application()方法，获取app
2、setUpAsync、setUp执行测试用例前执行，tearDownAsync、tearDown执行测试用例结束后执行
3、AioHTTPTestCase类的setUp，会创建server、client、loop
4、unittest_run_loop装饰测试用例
"""

from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop
from aiohttp import web


class TestCase(AioHTTPTestCase):

    async def hello(self, request):
        return web.Response(text="hello")

    async def get_application(self) -> web.Application:
        app = web.Application()
        app.router.add_get('/', self.hello)
        return app

    @unittest_run_loop
    async def test_01(self):
        resp = await self.client.get('/')
        print(resp)
        assert resp.status == 200
        text = await resp.text()
        assert text == "hello"

    async def setUpAsync(self) -> None:
        print("before.........")

    async def tearDownAsync(self) -> None:
        print('after..........')

    def setUp(self) -> None:
        print('set up before........')
        super().setUp()

    def tearDown(self) -> None:
        print(' tear down after......')
        super().tearDown()
