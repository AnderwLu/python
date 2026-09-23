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


def main():
    task = asyncio.create_task(test())
    print(isinstance(task, asyncio.Future))

    def done_callback(f: asyncio.Future):
        loop = asyncio.get_running_loop()
        loop.stop()
        print(task.result())

    task.add_done_callback(done_callback)


def run(f: Callable):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.call_soon(f)
    loop.run_forever()


run(main)
