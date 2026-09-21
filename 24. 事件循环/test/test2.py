import asyncio

loop = asyncio.new_event_loop()


def first():
    print(1)


def second():
    print(2)
    loop.call_soon(lambda: print(3))
    loop.stop()


def third():
    print(4)


loop.call_soon(first)
loop.call_soon(second)
loop.call_soon(third)

loop.run_forever()
print("循环已停止")
"""
第一轮：
就绪队列： first second third
拷贝执行队列：first second third
执行 first 打印 1 ；second 打印 2 讲print(3)添加到执行队列 修改_stopping = True ；third 打印 4
判断_stopping 循环结束
就绪队列：print(3)
可以再次执行 loop.run_forever()继续下一轮循环

"""
