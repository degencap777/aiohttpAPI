from aiohttp import web


async def handle(request):
    name = request.match_info.get("name", "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)


routes = [web.get("/", handle), web.get("/{name}", handle)]

hello = web.Application()
hello.add_routes(routes)

# https://aiohttp.readthedocs.io/en/stable/web_advanced.html#aiohttp-web-nested-applications
# https://aiohttp.readthedocs.io/en/stable/web_reference.html#aiohttp-web-route-def
# alternate route handling for decorators

