import asyncio
from async_delay import async_delay
from typing import Coroutine


def gather(*aws: Coroutine) -> asyncio.Future:
    # 你的代码
    future = asyncio.Future()
    list = [None] * len(aws)
    idx: int = 1

    def add(fu: asyncio.Future, ix: int):
        list[ix - 1] = fu.result()
        if ix == len(aws):
            future.set_result(list)

    def run(iterator):
        try:
            item = next(iterator)
            task = asyncio.create_task(item)
            nonlocal idx
            task.add_done_callback(lambda fu, ix=idx: add(fu, ix))
            idx += 1
            run(iterator)
        except StopIteration as e:
            pass

    run(iter(aws))
    return future


async def coro(name: str, duration: int):
    await async_delay(duration)
    return f"{name} 完成"


async def main():
    results = await gather(
        coro("A", 2),
        coro("B", 1),
        coro("C", 3),
    )
    print(results)  # 预期: ['A 完成', 'B 完成', 'C 完成']


asyncio.run(main())
