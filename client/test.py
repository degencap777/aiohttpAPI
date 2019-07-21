import aiohttp
import asyncio


async def test(name):
    auth = aiohttp.BasicAuth(login="damien", password="test")
    tcpconn = aiohttp.TCPConnector(ssl=False)
    async with aiohttp.ClientSession(auth=auth, connector=tcpconn) as client:
        async with client.get(f"https://localhost:8443/hello/{name}") as r:
            return await r.text()


loop = asyncio.get_event_loop()
msg = loop.run_until_complete(test("damien"))
print(msg)
