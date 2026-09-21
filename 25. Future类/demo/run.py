import asyncio


def run(func):
    # 创建事件循环
    loop = asyncio.new_event_loop()
    # 绑定事件循环到当前线程
    asyncio.set_event_loop(loop)
    # 添加func到ready队列
    loop.call_soon(func)
    # 运行事件循环
    loop.run_forever()
