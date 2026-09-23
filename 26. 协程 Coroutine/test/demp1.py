import asyncio
from async_delay import async_delay
from typing import Coroutine


def gather(*aws: Coroutine) -> asyncio.Future:
    # 你的代码
    future = asyncio.Future()
    list = []

    def add(fu: asyncio.Future, iterator):
        list.append(fu.result())
        run(iterator)

    def run(iterator):
        try:
            item = next(iterator)
            task = asyncio.create_task(item)
            task.add_done_callback(lambda fu: add(fu, iterator))
        except StopIteration as e:
            future.set_result(list)

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
