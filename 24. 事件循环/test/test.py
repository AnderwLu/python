import asyncio

loop = asyncio.new_event_loop()


def task1():
    print("任务1")


def task2():
    print("任务2")


def task3():
    print("任务3")


loop.call_soon(task1)
print("task1 over")  # task1 ove
loop.call_soon(task2)
print("task2 over")  # task2 ove
loop.call_soon(task3)
print("task3 over")  # task3 ove

loop.run_forever()
# 任务1
# 任务2
# 任务3
print("已结束")  # 不打印
