import asyncio
from aiohttp import web
from middlewares.auth import auth
from apps.hello import hello
import ssl

import os

print(os.path.join(os.getcwd(), "ca.cert"))

ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.load_cert_chain("ca.cert", "ca.key")

app = web.Application()
app.add_subapp("/hello", hello)

app.middlewares.append(auth)


if __name__ == "__main__":
    web.run_app(app, ssl_context=ssl_context)
