from collections.abc import Callable

from async_delay import async_delay
from async_request import async_request
import asyncio


async def test():
    print("main begins")
    resp1 = await async_request("localhost", 5500, "/index.html")
    print("resp1", resp1[:9])
    await async_delay(1)
    print("delayed")
    resp2 = await async_request("localhost", 5500, "/index.html")
    print("resp2", resp2[:9])
    return "ok"


result = asyncio.run(test())
print(result)
