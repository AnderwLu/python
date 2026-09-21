import asyncio

loop = asyncio.new_event_loop()


def delayed():
    print(1)
    loop.call_later(0, lambda: print(2))
    loop.call_soon(lambda: print(3))


def soon():
    print(4)
    loop.call_soon(lambda: print(5))


loop.call_later(0, delayed)
loop.call_soon(soon)


loop.run_forever()
print("done")
"""
第一轮事件循环
run_forever触发_run_once
就绪队列call_soon ： soon
延时队列call_later： delayed：0
delayed：0是0讲delayed添加到就绪队列call_soon： soon delayed
拷贝就绪队列到执行队列：soon delayed
执行 打印 4 然后将 print(5)添加到就绪队列， 打印 1，print(2)添加到延时队列， 将print(3)添加到就绪队列
进入第二轮循环：
就绪队列call_soon ： print(5) print(3) 
延时队列call_later： print(2)：0
就绪队列call_soon：print(5) print(3) print(2)
拷贝到执行队列 print(5) print(3) print(2)
执行 打印 5 3 2
"""
