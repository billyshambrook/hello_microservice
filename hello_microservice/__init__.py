from aiohttp import web


def index(request):
    return web.Response(text="Welcome home 2!")


app = web.Application()
app.router.add_route('GET', '/', index)
