from aiohttp.web import middleware, HTTPUnauthorized
import base64

import asyncio


@middleware
async def auth(request, handler):
    if check(*parse_token(request)):
        return await handler(request)
    else:
        raise HTTPUnauthorized(headers={"WWW-Authenticate": "Basic"})


def parse_token(request):
    header = request.headers.get("authorization", None)
    if not header:
        raise HTTPUnauthorized(headers={"WWW-Authenticate": "Basic"})

    auth_type, token = header.split()

    if not auth_type.lower() == "basic":
        raise HTTPUnauthorized(headers={"WWW-Authenticate": "Basic"})

    username, password = str(base64.b64decode(token), encoding="utf8").split(
        ":", maxsplit=1
    )

    return username, password


def check(username, password):
    if username and password:
        return True
