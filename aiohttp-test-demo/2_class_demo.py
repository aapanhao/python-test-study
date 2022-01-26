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
