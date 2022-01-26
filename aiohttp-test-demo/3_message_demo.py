from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop
from aiohttp import web
from unittest.mock import patch, AsyncMock


class Permission:

    def check_permission(self, func, n1, n2):
        print("ch!!")
        if n1 == n2:
            raise Exception
        return func()


class TestCase(AioHTTPTestCase):

    async def add(self, *args):
        return sum(args)

    async def hello(self, request):
        result = await Permission().check_permission(self.add, 1, 1)
        return web.Response(text=f"OK~~~{result}")

    async def get_application(self) -> web.Application:
        app = web.Application()
        app.router.add_get('/', self.hello)
        return app

    @unittest_run_loop
    async def test_01(self):
        with patch.object(Permission, 'check_permission', side_effect=AsyncMock(return_value="OK!!!"),
                          autospec=True) as permission_mock:
            a = await Permission().check_permission(self.add, 1, 1)
            print(a)

            _, method, *args = permission_mock.call_args[0]
            print(method)
            print()
            print(args)
            print(await method(*args))

            resp = await self.client.get('/')
            print(resp)
            result = await resp.text()
            print(result)
            assert "OK" in result


# coverage run --source=./message -m pytest --disable-pytest-warnings tests
# coverage report
# coverage html -d covhtml
