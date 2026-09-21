import asyncio
import run


# 定义一个async_delay函数，接受一个int
def async_delay(duration: int):
    # 获取当前线程的事件循环
    loop = asyncio.get_event_loop()
    # 创建一个future
    future = loop.create_future()
    # 添加一个任务到延时队列，这里吧future.set_result函数传进去，到时间后会执行这个函数让future变成成功状态
    # 第三个参数就是future.set_result函数的参数
    loop.call_later(duration, future.set_result, None)
    # 返回 future
    return future


# 定义main函数，执行业务逻辑
def main():
    # 调用async_delay获取一个future，
    # add_done_callback函数会吧这个lambda函数注册到Future 对象内部的回调列表中
    # 线程不等待执行后续逻辑，打印：不影响其他代码的执行
    # 2秒后这个future会被触发future.set_result函数变成成功状态
    # set_result函数变成成功状态后将回调列表中的回调函数放到ready列表中
    # 事件循环执行回调函数
    # 打印 2 seconds have passed
    async_delay(2).add_done_callback(lambda _: print("2 seconds have passed"))
    print("不影响其他代码的执行")


# 将业务逻辑函数传入，事件循环run函数中
# 这里就是将main函数添加到了，ready队列
run.run(main)
