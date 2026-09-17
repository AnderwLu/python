from contextlib import contextmanager

@contextmanager
def demo():
    print("进入")
    yield
    print("正常退出")


with demo():
    print("执行中")
    # raise ValueError("出错了")
    print("这行不会执行")

#进入
#执行中
# 出错了


@contextmanager
def demo():
    print("进入")
    try:
        yield
    except Exception as e:
        print(f"捕获异常: {e}")
    finally:
        print("清理")


with demo():
    print("执行中")
    raise ValueError("出错了")


# #进入
# #执行中
# # 捕获异常 出错了
# #清理