from collections.abc import Callable
from types import coroutine

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


def create_task(task):
    loop = asyncio.get_running_loop()
    f = loop.create_future()
    f1 = loop.create_future()
    f1.set_result(None)

    def run(fc: asyncio.Future | None) -> None:
        try:
            r = task.send(fc)
            r.add_done_callback(lambda s: run(r.result()))
        except StopIteration as e:
            f.set_result(e.value)

    f1.add_done_callback(lambda fu: run(None))
    return f


def main():
    f = create_task(test())
    print("zijide")

    def runf(f: asyncio.Future):
        print(f.result())
        asyncio.get_running_loop().stop()

    f.add_done_callback(runf)


# 创建一个事件循环，执行man函数
def run(fac: Callable):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.call_soon(fac)
    loop.run_forever()


run(main)
